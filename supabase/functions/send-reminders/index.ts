/**
 * 30 günlük "tekrar ölç" hatırlatması.
 *
 * pg_cron her gün bir kez çağırır (bkz. reminder_cron migration'ı).
 * Çağrı anon key ile yapılıyor — bu güvenli, çünkü fonksiyon idempotent:
 * her kayıt gönderimden ÖNCE işaretleniyor, dolayısıyla tekrar tetiklemek
 * fazladan mail göndermiyor, sadece boş dönüyor.
 *
 * Gereken tek sır: BREVO_API_KEY (+ doğrulanmış gönderici adresi).
 * Supabase paneli → Edge Functions → Secrets.
 */

const SUPABASE_URL = Deno.env.get("SUPABASE_URL")!;
const SERVICE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
const BREVO_API_KEY = Deno.env.get("BREVO_API_KEY");
const SENDER_EMAIL = Deno.env.get("BREVO_SENDER_EMAIL");
const SENDER_NAME = Deno.env.get("BREVO_SENDER_NAME") ?? "Vivelong";
const SITE = "https://vivelong.com";
const BATCH = 50;

type Due = {
  kind: "lead" | "user";
  ref_id: string;
  email: string;
  display_name: string | null;
  locale: string | null;
  bio_age: number | null;
  last_measured: string;
  unsub_token: string;
};

async function rpc(fn: string, body: unknown) {
  const r = await fetch(`${SUPABASE_URL}/rest/v1/rpc/${fn}`, {
    method: "POST",
    headers: {
      apikey: SERVICE_KEY,
      Authorization: `Bearer ${SERVICE_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });
  if (!r.ok) throw new Error(`${fn}: ${r.status} ${await r.text()}`);
  const text = await r.text();
  return text ? JSON.parse(text) : null;
}

function esc(s: string) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function buildEmail(d: Due) {
  const tr = (d.locale ?? "tr") !== "en";
  const name = d.display_name?.split(" ")[0] ?? "";
  const days = Math.floor(
    (Date.now() - new Date(d.last_measured).getTime()) / 86400000,
  );
  const unsub = tr
    ? `${SITE}/abonelik-iptal/?t=${d.unsub_token}`
    : `${SITE}/en/unsubscribe/?t=${d.unsub_token}`;
  const calc = tr ? `${SITE}/#hesaplama` : `${SITE}/en/#hesaplama`;

  const subject = tr
    ? (d.bio_age
      ? `Biyolojik yaşın ${days} gün önce ${d.bio_age}'di — şimdi ne durumda?`
      : "Biyolojik yaşını tekrar ölçme zamanı")
    : (d.bio_age
      ? `Your biological age was ${d.bio_age}, ${days} days ago — where is it now?`
      : "Time to re-measure your biological age");

  const greeting = tr
    ? (name ? `Merhaba ${esc(name)},` : "Merhaba,")
    : (name ? `Hi ${esc(name)},` : "Hi,");

  const body = tr
    ? `<p style="margin:0 0 16px">${greeting}</p>
       <p style="margin:0 0 16px">${
      d.bio_age
        ? `${days} gün önce Vivelong'da biyolojik yaşını <b>${d.bio_age}</b> olarak ölçmüştün.`
        : `${days} gün önce Vivelong'da biyolojik yaşını ölçmüştün.`
    }</p>
       <p style="margin:0 0 16px">Tek bir ölçüm fazla bir şey söylemez — asıl bilgi <b>değişimde</b>. Uyku, hareket ve beslenmede son bir ayda yaptığın küçük değişiklikler bu sayıyı gerçekten oynatmış olabilir.</p>
       <p style="margin:0 0 24px">Testi tekrar çözmen 2 dakika sürüyor ve iki ölçümü yan yana göreceksin.</p>`
    : `<p style="margin:0 0 16px">${greeting}</p>
       <p style="margin:0 0 16px">${
      d.bio_age
        ? `${days} days ago you measured your biological age on Vivelong: <b>${d.bio_age}</b>.`
        : `You measured your biological age on Vivelong ${days} days ago.`
    }</p>
       <p style="margin:0 0 16px">A single number says little — the signal is in the <b>change</b>. Small shifts in sleep, movement and diet over the past month can genuinely move it.</p>
       <p style="margin:0 0 24px">Retaking the test takes 2 minutes, and you'll see both measurements side by side.</p>`;

  const cta = tr ? "Biyolojik Yaşımı Tekrar Ölç" : "Re-measure My Biological Age";
  const foot = tr
    ? `Bu e-postayı, Vivelong'da biyolojik yaş testini çözerken hatırlatma almayı kabul ettiğin için aldın.<br>
       Vivelong bilgilendirme amaçlıdır, tıbbi tavsiye değildir.`
    : `You're receiving this because you opted in to reminders when you took the biological age test on Vivelong.<br>
       Vivelong is for information only and is not medical advice.`;
  const unsubTxt = tr ? "Bu hatırlatmaları bırak" : "Unsubscribe from these reminders";

  const htmlContent =
    `<!doctype html><html><body style="margin:0;padding:0;background:#F2F5F0;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F2F5F0;padding:28px 12px;">
<tr><td align="center">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:520px;background:#fff;border-radius:16px;overflow:hidden;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;">
    <tr><td style="background:linear-gradient(135deg,#1A4731,#2D6A4F);padding:26px 28px;">
      <div style="color:#fff;font-size:19px;font-weight:700;letter-spacing:.3px;">Vivelong</div>
    </td></tr>
    <tr><td style="padding:28px;color:#1C2B1F;font-size:15px;line-height:1.7;">
      ${body}
      <table role="presentation" cellpadding="0" cellspacing="0"><tr><td style="border-radius:11px;background:#1A4731;">
        <a href="${calc}" style="display:inline-block;padding:14px 28px;color:#fff;text-decoration:none;font-size:15px;font-weight:700;">${cta}</a>
      </td></tr></table>
    </td></tr>
    <tr><td style="padding:18px 28px 26px;border-top:1px solid #E0EDE6;color:#6B8C7A;font-size:11px;line-height:1.7;">
      ${foot}<br><br>
      <a href="${unsub}" style="color:#6B8C7A;">${unsubTxt}</a>
    </td></tr>
  </table>
</td></tr></table>
</body></html>`;

  return { subject, htmlContent };
}

Deno.serve(async () => {
  if (!BREVO_API_KEY || !SENDER_EMAIL) {
    // Yapılandırma eksik: cron'u hataya sokmadan görünür şekilde bildir.
    return Response.json({
      configured: false,
      error:
        "BREVO_API_KEY ve BREVO_SENDER_EMAIL secret'ları tanimli degil. Supabase > Edge Functions > Secrets.",
    });
  }

  let due: Due[];
  try {
    due = await rpc("due_reminders", { p_limit: BATCH });
  } catch (e) {
    return Response.json({ ok: false, step: "due_reminders", error: String(e) }, {
      status: 500,
    });
  }

  let sent = 0;
  const failed: { email: string; error: string }[] = [];

  for (const d of due) {
    // ÖNCE işaretle: bir hatirlatmayi kacirmak, ayni kisiye iki kez
    // gondermekten iyidir. Ayrica fonksiyonu idempotent yapan sey bu.
    try {
      await rpc("mark_reminder_sent", { p_kind: d.kind, p_ref_id: d.ref_id });
    } catch (e) {
      failed.push({ email: d.email, error: "mark: " + String(e) });
      continue;
    }

    const { subject, htmlContent } = buildEmail(d);
    try {
      const r = await fetch("https://api.brevo.com/v3/smtp/email", {
        method: "POST",
        headers: {
          "api-key": BREVO_API_KEY,
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify({
          sender: { name: SENDER_NAME, email: SENDER_EMAIL },
          to: [{ email: d.email, ...(d.display_name ? { name: d.display_name } : {}) }],
          subject,
          htmlContent,
          tags: ["remeasure-30d", d.kind],
        }),
      });
      if (!r.ok) failed.push({ email: d.email, error: `brevo ${r.status}: ${await r.text()}` });
      else sent++;
    } catch (e) {
      failed.push({ email: d.email, error: String(e) });
    }
  }

  return Response.json({ ok: true, due: due.length, sent, failed });
});
