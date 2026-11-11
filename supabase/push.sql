-- Vivelong akşam hatırlatıcısı (web push): abonelik tablosu + her akşam 20:30 (TR) zamanlayıcı
create table if not exists public.push_subscriptions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null default auth.uid() references auth.users(id) on delete cascade,
  endpoint text not null unique,
  p256dh text not null,
  auth text not null,
  ua text,
  aktif boolean not null default true,
  last_sent_on date,
  created_at timestamptz not null default now()
);

alter table public.push_subscriptions enable row level security;

create policy "push: kendi aboneligini okur" on public.push_subscriptions
  for select to authenticated using ((select auth.uid()) = user_id);
create policy "push: kendi aboneligini ekler" on public.push_subscriptions
  for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "push: kendi aboneligini gunceller" on public.push_subscriptions
  for update to authenticated using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);
create policy "push: kendi aboneligini siler" on public.push_subscriptions
  for delete to authenticated using ((select auth.uid()) = user_id);

revoke all on public.push_subscriptions from anon;
grant select, insert, update, delete on public.push_subscriptions to authenticated;

-- Her gün 17:30 UTC = 20:30 Türkiye saati. Fonksiyon günde bir kez gönderir (last_sent_on), tekrar tetiklenmesi zararsız.
select cron.schedule(
  'vivelong-aksam-hatirlatma',
  '30 17 * * *',
  $$
  select net.http_post(
    url := 'https://mdpynseovqlbfipbegij.supabase.co/functions/v1/aksam-hatirlatma',
    headers := jsonb_build_object('Content-Type', 'application/json', 'Authorization', 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1kcHluc2VvdnFsYmZpcGJlZ2lqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODg4NzcyOTIsImV4cCI6MjEwNDQ1MzI5Mn0.l7XcT0vJ-X649E-E5QH-LcMQuu1A0tW9vPIfiELs1zw'),
    body := '{}'::jsonb
  );
  $$
);
