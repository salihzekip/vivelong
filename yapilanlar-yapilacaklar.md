# Vivelong SEO/GEO Çalışması — Yapılanlar & Yapılacaklar

**Son güncelleme:** 9 Ağustos 2026 (H1 hiyerarşisi + dış kaynak linkleri tamamlandı ve deploy edildi)
**Kapsam:** vivelong.com SEO + GEO denetimi ve uygulanan hızlı aksiyonlar

---

## Rapor

Tam SEO/GEO denetim raporu (bulgular + öncelik sıralı aksiyon takvimi):
**https://claude.ai/code/artifact/1ab47bbb-2cdb-4140-9184-f5ac18385dd2**

**En kritik bulgu:** Site 20 içerik parçasını (5 Mavi Bölge, 4 Temel Taş rehberi, 9 blog makalesi, Cinsiyet sayfası) tek `index.html` altında JS panel olarak saklıyordu — hiçbirinin ayrı URL'si yoktu. Google `site:vivelong.com` sorgusunda sadece 1 sayfa görüyordu. Meta description, Open Graph, canonical, JSON-LD, robots.txt, sitemap.xml, favicon — hiçbiri yoktu.

---

## ✅ Yapılanlar (8-9 Ağustos 2026)

### 1. Teknik SEO temelleri (deploy edildi, canlıda doğrulandı)
- [x] Meta description eklendi
- [x] Canonical tag eklendi
- [x] Open Graph + Twitter Card etiketleri eklendi
- [x] JSON-LD: Organization + WebSite şeması eklendi
- [x] Favicon eklendi (data-URI, mevcut logo SVG'sinden)
- [x] `robots.txt` oluşturuldu (sitemap'e işaret ediyor)
- [x] `sitemap.xml` oluşturuldu

### 2. Çok-URL mimarisine geçiş (en büyük yapısal değişiklik, deploy edildi)
- [x] 5 Mavi Bölge sayfası: `/mavi-bolgeler/{sardunya,okinawa,nicoya,ikaria,loma-linda}/`
- [x] 4 Temel Taş rehberi: `/rehber/{longevity-beslenmesi,sosyal-bag-ve-amac,hareket-ve-egzersiz,uyku-ve-zihin-sagligi}/`
- [x] 9 blog makalesi: `/blog/{9 makale}/`
- [x] Cinsiyet sayfası: `/cinsiyet-ve-uzun-yasam/`
- [x] Her sayfanın kendi title/meta description/canonical/OG/Twitter + Article/BlogPosting+BreadcrumbList JSON-LD'si var
- [x] Ortak `assets/site.css` oluşturuldu (ana sayfa stilinden birebir türetildi)
- [x] Ana sayfadaki 20 kart (`zcard`/`pcard`/`pil`/`bcard`) gerçek `href`'e çevrildi — JS panel davranışı `event.preventDefault()` ile korundu
- [x] `sitemap.xml` 20 URL'e güncellendi

### 3. GEO (AI arama motorları) hızlı kazanımları (deploy edildi)
- [x] `llms.txt` oluşturuldu (ChatGPT/Perplexity/Claude için site özeti + tüm linkler)
- [x] 7 blog makalesine FAQPage JSON-LD eklendi (toplam 14 soru, sayfadaki gerçek metinden birebir çıkarıldı)
  - Soru bulunamayan 2 makale (sirkadiyen-beslenme, mitokondri) atlandı — uydurma yapılmadı

### 4. Yan bulgu: git/deploy drift düzeltildi
- [x] Yerel dosyada git'e hiç commit edilmemiş, canlıya hiç deploy edilmemiş özellikler bulundu: KVKK Aydınlatma modalı, Auth modalı, Forum bölümü. Kullanıcı onayıyla bugünkü deploy'a dahil edildi, canlıda doğrulandı.

### 5. Google Search Console kurulumu (BAŞLADI, TAMAMLANMADI)
- [x] vivelong.com "alan adı" (domain) mülkü olarak eklendi
- [x] Gerekli TXT doğrulama kaydı Netlify DNS'e otomatik eklendi
  - Zone ID: `6a416bae515f867027e00afc`
  - Kayıt ID: `6a7790f149ba949553e25379`
  - Değer: `google-site-verification=XwV1qYoYB4ftjBfNqvFakx5l0Cv6IE_lJD8`
- [x] DNS yayılımı doğrulandı: Netlify'ın kendi NS'i, Google'ın 8.8.8.8'i ve Cloudflare 1.1.1.1 — hepsinde kayıt doğru ve eksiksiz görünüyor
- [x] Netlify API'den ham JSON ile + genel DNS'ten okunan değer karakter karakter karşılaştırıldı: **tam eşleşiyor, veri hatası yok**
- [x] **Google Search Console mülkü doğrulandı** (9 Ağustos, DNS TXT + Domain mülkü 5. denemede de başarısız kalınca URL-öneki (`https://vivelong.com/`) mülk türüne geçildi, Google Analytics doğrulama yöntemiyle anında doğrulandı — GA4'ün zaten aynı Google hesabında kurulu olması sayesinde).

---

## 🔲 Yapılacaklar (yarın devam)

> **Sıradaki oturumda İLK bunlarla başla:** H1 hiyerarşisi düzeltmesi ve dış kaynak linkleri (bkz. Öncelik 3). En yüksek etki/efor oranına sahip olanlar bunlar — ikisi de sadece `index.html`'de küçük düzenlemeler, deploy gerektirir ama yapısal değişiklik değil.

### Öncelik 1 — Search Console'u bitir
- [x] Mülk doğrulandı (9 Ağustos, URL-öneki + Google Analytics yöntemiyle)
- [x] `sitemap.xml` Search Console'a gönderildi (9 Ağustos, Chrome üzerinden claude-in-chrome ile: Site Haritaları → `sitemap.xml` → Gönder → "Site haritası başarıyla gönderildi" onayı alındı). Durum ilk anda "Getirilemedi" gösteriyor — bu normal, Google birkaç saat/gün içinde periyodik taramayla güncelleyecek.
- [ ] Birkaç gün içinde "Kapsam" (Coverage/Pages) raporunda 20 sayfanın indekslendiğini kontrol et — sitemap durumu "Getirilemedi"den "Başarılı"ya dönünce tekrar bak
- **Not (9 Ağustos):** Chrome uzantısı ilk denemede bağlı değildi, ikinci denemede bağlandı ve Search Console + GA4'e erişildi.

### Öncelik 2 — Raporun "Ay 2+" maddeleri
- [x] `netlify/functions/subscribe.js` git'e eklendi (9 Ağustos, commit `88ee712`, push edildi). `.gitignore` eklendi (`.netlify/` yerel önbelleği artık izlenmiyor).
- [~] Backlink stratejisi — ilk araştırma turu yapıldı (WebSearch), henüz kimseyle iletişime geçilmedi. Bulunanlar:
  - **Startup/ürün dizinleri (somut, düşük efor):** [startuplist.com.tr](https://startuplist.com.tr/) (Türkiye girişim kataloğu), [StartupMarket](https://startupmarket.co/) — vivelong'u ürün olarak eklemek gerçek, hızlı bir backlink fırsatı
  - **Aynı konuda otorite sahibi siteler (işbirliği/atıf fırsatı, önce ilişki kurulmalı):** [Longevity Okulu](https://www.longevityokulu.com/) (doğrudan aynı niş, eğitim platformu), [Dr. Mehmet Portakal](https://www.drmehmetportakal.com/) (longevity konulu doktor bloğu), [Ekolife Yaşam Merkezi](https://www.ekolifeyasammerkezi.com.tr/)
  - **Genel sağlıklı yaşam blog toplulukları (misafir yazı ihtimali, doğrulanmadı):** Uplifers, Yesilist.com, TheLifeCo Blog
  - **Rakip biyolojik yaş hesaplayıcıları (backlink değil, rakip/konumlandırma referansı):** hesaplama.lol, hesapratik.com, engelli.com, SuperAge (App Store uygulaması)
  - Sıradaki adım: kullanıcı hangi isimlerle iletişime geçmek istediğine karar vermeli — bu bir öneri listesi, otomatik outreach yapılmadı

### Öncelik 3 — Raporun "Hafta 1: Güven sinyalleri" maddesi
- [x] **H1 hiyerarşisi düzeltildi (9 Ağustos, deploy edildi, canlıda doğrulandı):** ana sayfada 22 `<h1>` vardı, artık sadece hero başlığı `<h1>`, panellerdeki 21 başlık `<h2>`'ye çevrildi (+ `.zp-hero h1` CSS selektörü `.zp-hero h2`'ye güncellendi). `curl vivelong.com | grep -c "<h1"` → 1.
- [x] **Dış kaynak referansları gerçek linklere bağlandı (9 Ağustos, deploy edildi, canlıda doğrulandı):** 0 içerik linkinden 30 gerçek dış linke çıkıldı. WebSearch ile doğrulanan spesifik atıflar: NCBI PMC11688636 (biyomarker bölümü), Harvard Study of Adult Development (adultdevelopmentstudy.org), Sara Lazar 2011 meditasyon çalışması (PubMed), David Sinclair'in Harvard laboratuvarı, Harvard'ın geç yeme/yağ depolama çalışması (hms.harvard.edu), Holt-Lunstad 2015 yalnızlık meta-analizi, US Surgeon General 2023 advisory (hhs.gov PDF). Ayrıca 19 "Kaynak:" kutusundaki kurum/dergi isimleri (WHO, Mayo Clinic, Nature ailesi, Cell ailesi, PNAS, NEJM, JAMA, PREDIMED, bluezones.com, aysegulcoruhlu.com vb.) kendi resmi sayfalarına bağlandı.
  - **Yan düzeltme:** "2050'de 60+ nüfus 2,1 milyar" istatistiği kodda yanlışlıkla "(NCBI 2024)" olarak etiketlenmişti — gerçek kaynağı WHO, düzeltilip who.int'e linklendi.
  - **Kapsam dışı bırakılan (uydurma riski nedeniyle linklenmedi):** Kaynak kutularındaki tekil yazar+yıl atıfları (Pes & Poulain 2004, Willcox 2007, Rosero-Bixby 2013, Panagiotakos 2011, Fraser 2009, Horvath 2013'ün tam DOI'si, PNAS 2004 Epel'in tam DOI'si, Ornish 2013, Yoshino 2018, Franceschi 2018, Perls Centenarian çalışmasının tam atfı, FOXO3/Flachsbart, Schwalfenberg 2012, Mizushima & Komatsu 2011) — bunlar için doğru PubMed/DOI linkini tek tek doğrulamadan eklemek yanlış/kırık link riski taşıyordu, o yüzden düz metin bırakıldı. İleride derinlemesine bir link-doğrulama turu yapılabilir.
- [ ] "Hakkımızda" bölümü ekle — kim yazıyor, editoryal/kaynak süreci nedir bilgisi hâlâ yok (YMYL/sağlık içeriği için önemli, rapor bunu özellikle vurguluyor)
- [ ] Sosyal medya hesabı bağla — sitede Instagram/Facebook/LinkedIn linki hiç yok (`grep` 0 eşleşme verdi); önce hesap var mı yok mu netleşmeli, yoksa açılması değerlendirilmeli

*Not: Sıradaki oturumda buradan devam: "Hakkımızda" bölümü + sosyal medya hesabı kararı.*

### Öncelik 4 — Doğrulama / temizlik
- [ ] Kart tıklama davranışını (Mavi Bölgeler/Blog kartına tıklayınca JS panelinin sayfadan çıkmadan açılması) kullanıcı kendi tarayıcısında bir kez elle test etmeli — Chrome uzantısı bu ağır sayfada otomatik test edemedi (tekrarlayan zaman aşımı)
- [ ] İsteğe bağlı: sirkadiyen-beslenme ve mitokondri makalelerine soru-cevap formatlı bölüm eklenirse FAQPage şeması onlara da eklenebilir
- [ ] İsteğe bağlı: Pro sayfası (`zp-pro`) ve Forum (`zp-forum`) şu an ayrı URL'ye taşınmadı — SEO değeri düşük görüldüğü için kapsam dışı bırakıldı

---

## GA4 durum kontrolü (9 Ağustos 2026)

Chrome üzerinden GA4'e (property 546237084) girildi, son 7 gün: **2 etkin kullanıcı, 9 etkinlik, 0 yeni kullanıcı, 0 önemli faaliyet**. Trafiğin tamamı `Direct/(none)` — organik arama trafiği henüz yok. Görüntülenen tek sayfa ana sayfa; yeni 20 sayfadan (Mavi Bölgeler/Rehber/Blog) hiçbirine henüz ziyaret gelmemiş. Bu beklenen bir durum: site bu hafta yapısal değişiklik geçirdi ve Search Console yeni doğrulandı, Google henüz taramaya/indekslemeye başlamadı. Birkaç gün sonra tekrar kontrol edilmeli.

---

## Search Console doğrulama denemeleri (referans)

| Zaman | Sonuç |
|---|---|
| 8 Ağustos akşamı, ~23:3x | Başarısız |
| 8 Ağustos akşamı (~10 dk sonra) | Başarısız |
| 9 Ağustos, gece yarısından hemen sonra | Başarısız |
| **9 Ağustos, 00:26** | Başarısız |

*Not: İlk iki denemenin dakikası tam loglanmadı, yaklaşık verildi. Veri doğruluğu (DNS kaydı) her denemeden bağımsız olarak ayrıca doğrulandı — sorun veri değil, Google'ın doğrulama servisinin gecikmesi.*
