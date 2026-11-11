/**
 * Akşam hatırlatıcısı: her akşam 22:00'de (pg_cron, 19:00 UTC) abone üyelere telefon bildirimi gönderir.
 * Idempotent: her abonelik gönderimden ÖNCE o gün için işaretlenir (last_sent_on), tekrar çağrı fazladan bildirim atmaz.
 * Gereken tek sır: VAPID_PRIVATE_KEY (Supabase > Edge Functions > Secrets). Açık anahtar aşağıda sabit.
 */
import webpush from "npm:web-push@3.6.7";

const SUPABASE_URL = Deno.env.get("SUPABASE_URL")!;
const SERVICE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
const VAPID_PUBLIC = "BLa6wAr8ue8bOkITfatAinw9KAlFQdWHH9zvPJWgECaI2f99hegInX8M8rxgRjAHZyt5rAeoGEkT6kJmtTFXIiM";
const VAPID_PRIVATE = Deno.env.get("VAPID_PRIVATE_KEY");
const VAPID_SUBJECT = Deno.env.get("VAPID_SUBJECT") ?? "https://vivelong.com";
const TOPLAM = 22;

type Sub = { id: string; user_id: string; endpoint: string; p256dh: string; auth: string };

function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json" } });
}

async function rest(path: string, init: RequestInit = {}) {
  const r = await fetch(`${SUPABASE_URL}/rest/v1/${path}`, {
    ...init,
    headers: {
      apikey: SERVICE_KEY,
      Authorization: `Bearer ${SERVICE_KEY}`,
      "Content-Type": "application/json",
      Prefer: "return=minimal",
      ...(init.headers ?? {}),
    },
  });
  if (!r.ok) throw new Error(`${path.split("?")[0]}: ${r.status} ${await r.text()}`);
  const t = await r.text();
  return t ? JSON.parse(t) : null;
}

function bugunTR() {
  return new Date(Date.now() + 3 * 3600 * 1000).toISOString().slice(0, 10);
}

function metin(n: number) {
  if (n === 0) return "Bugün henüz işaretlemedin. İki dakika ayır, serin bozulmasın.";
  if (n < TOPLAM) return `Bugün ${n}/${TOPLAM} alışkanlık işaretledin. Eksik kalanlara bir bak.`;
  return `Bugün ${TOPLAM}/${TOPLAM}. Harika bir gün; yarın görüşmek üzere.`;
}

Deno.serve(async () => {
  if (!VAPID_PRIVATE) {
    return json({ ok: false, hata: "VAPID_PRIVATE_KEY secret'i tanimli degil. Supabase > Edge Functions > Secrets." });
  }
  webpush.setVapidDetails(VAPID_SUBJECT, VAPID_PUBLIC, VAPID_PRIVATE);
  const gun = bugunTR();

  const subs: Sub[] = (await rest(
    `push_subscriptions?select=id,user_id,endpoint,p256dh,auth&aktif=eq.true&or=(last_sent_on.is.null,last_sent_on.lt.${gun})&limit=1000`,
    { headers: { Prefer: "return=representation" } },
  )) ?? [];
  if (!subs.length) return json({ ok: true, gun, gonderilen: 0 });

  // Önce işaretle: aynı gün ikinci çağrı aynı kişiye tekrar göndermez.
  await rest(`push_subscriptions?id=in.(${subs.map((s) => s.id).join(",")})`, {
    method: "PATCH",
    body: JSON.stringify({ last_sent_on: gun }),
  });

  const kullanicilar = [...new Set(subs.map((s) => s.user_id))];
  const kayitlar: { user_id: string; done: string[] }[] = (await rest(
    `habit_logs?select=user_id,done&day=eq.${gun}&user_id=in.(${kullanicilar.join(",")})`,
    { headers: { Prefer: "return=representation" } },
  )) ?? [];
  const sayi = new Map(kayitlar.map((k) => [k.user_id, (k.done ?? []).length]));

  let gonderilen = 0, silinen = 0, hata = 0;
  await Promise.all(subs.map(async (s) => {
    const payload = JSON.stringify({
      title: "Bugünün longevity alışkanlıkları",
      body: metin(sayi.get(s.user_id) ?? 0),
      url: "/bugun/",
      tag: `vivelong-aksam-${gun}`,
    });
    try {
      await webpush.sendNotification({ endpoint: s.endpoint, keys: { p256dh: s.p256dh, auth: s.auth } }, payload, { TTL: 6 * 3600, urgency: "normal" });
      gonderilen++;
    } catch (e) {
      const kod = (e as { statusCode?: number }).statusCode;
      if (kod === 404 || kod === 410) {
        await rest(`push_subscriptions?id=eq.${s.id}`, { method: "DELETE" }).catch(() => {});
        silinen++;
      } else {
        hata++;
        console.error("push hatasi", kod, (e as Error).message);
      }
    }
  }));

  return json({ ok: true, gun, abone: subs.length, gonderilen, silinen, hata });
});
