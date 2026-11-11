/* Vivelong servis çalışanı: yalnızca bildirim. Önbellekleme yapmaz, site her zaman ağdan gelir. */
self.addEventListener('install', function () { self.skipWaiting(); });
self.addEventListener('activate', function (e) { e.waitUntil(self.clients.claim()); });

self.addEventListener('push', function (e) {
  var d = {};
  try { d = e.data ? e.data.json() : {}; } catch (_) { d = { body: e.data ? e.data.text() : '' }; }
  var title = d.title || 'Bugünün longevity alışkanlıkları';
  e.waitUntil(self.registration.showNotification(title, {
    body: d.body || 'İki dakika ayır, bugünü işaretle.',
    icon: '/assets/icons/icon-192.png',
    badge: '/assets/icons/badge-96.png',
    tag: d.tag || 'vivelong-aksam',
    renotify: true,
    data: { url: d.url || '/bugun/' }
  }));
});

self.addEventListener('notificationclick', function (e) {
  e.notification.close();
  var hedef = new URL((e.notification.data && e.notification.data.url) || '/bugun/', self.location.origin).href;
  e.waitUntil(self.clients.matchAll({ type: 'window', includeUncontrolled: true }).then(function (ws) {
    for (var i = 0; i < ws.length; i++) {
      var w = ws[i];
      if (w.url.indexOf(self.location.origin) === 0 && 'focus' in w) {
        return w.focus().then(function (f) { return f && f.navigate ? f.navigate(hedef) : null; });
      }
    }
    return self.clients.openWindow(hedef);
  }));
});
