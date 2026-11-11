-- Vivelong üye paneli: üyelerin günlük longevity alışkanlıkları (gün başına tek satır)
create table if not exists public.habit_logs (
  user_id uuid not null default auth.uid() references auth.users(id) on delete cascade,
  day date not null,
  done text[] not null default '{}',
  updated_at timestamptz not null default now(),
  primary key (user_id, day),
  constraint habit_logs_done_len check (cardinality(done) <= 40)
);

alter table public.habit_logs enable row level security;

create policy "habit_logs: kendi kaydini okur" on public.habit_logs
  for select to authenticated using ((select auth.uid()) = user_id);
create policy "habit_logs: kendi kaydini ekler" on public.habit_logs
  for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "habit_logs: kendi kaydini gunceller" on public.habit_logs
  for update to authenticated using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);
create policy "habit_logs: kendi kaydini siler" on public.habit_logs
  for delete to authenticated using ((select auth.uid()) = user_id);

revoke all on public.habit_logs from anon;
grant select, insert, update, delete on public.habit_logs to authenticated;

comment on table public.habit_logs is 'Üye alışkanlık takibi: her gün için işaretlenen alışkanlık kimlikleri (h1..h22). RLS: yalnız kendi satırı.';
