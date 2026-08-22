# Vivelong SEO/GEO Çalışması — Yapılanlar & Yapılacaklar

**Son güncelleme:** 22 Ağustos 2026 (Mavi Bölgeler veri tartışması eklendi + yeni GLP-1/Ozempic blog yazısı, site 23 sayfaya çıktı)
**Kapsam:** vivelong.com SEO + GEO denetimi ve uygulanan hızlı aksiyonlar

---

## ✅ 22 Ağustos 2026 — Güncel araştırma taraması + yeni içerik

**Görev:** Site kurulduğundan beri eklenebilecek yeni bilimsel gelişme var mı diye araştırıldı + az rekabetli/çok aranan bir konuda yeni blog yazısı eklendi.

### 1. Mavi Bölgeler veri tartışması — şeffaflık eklemesi (kredibilite/YMYL için önemli)
- [x] WebSearch ile araştırıldı: 2024'te UCL demografı Saul Newman, Mavi Bölgeler'deki süper-yaşlı istatistiklerinin bir kısmının kayıt hataları/doğum belgesi eksikliği/emeklilik dolandırıcılığından kaynaklanabileceğini öne sürerek Ig Nobel Ödülü kazandı. Dan Buettner 2025'te *The Gerontologist*'te resmi kayıtlarla reddetti — ama bu makale en tartışmalı bölge olan Loma Linda'yı kapsamıyor.
- [x] `/blog/power-9-mavi-bolgeler/` sayfasına yeni bir bölüm ("Dürüst Olmak Gerekirse: Mavi Bölge Verileri Tartışmalı") + yeni FAQ (görünür + JSON-LD) + 2 yeni kaynak linki (UCL, Science.org) eklendi. Dengeli çerçeve: ham süper-yaşlı istatistiği tartışmalı ama Power 9'daki davranışsal tavsiyeler ayrı literatürle destekleniyor.
- [ ] İsteğe bağlı: aynı not 5 Mavi Bölge sayfasına ve ana sayfanın Mavi Bölgeler bölümüne de kısaca eklenebilir — şimdilik sadece en çok okunan özet sayfaya (Power 9) eklendi, efor/kapsam dengesi için.

### 2. Yeni blog yazısı: GLP-1 ilaçları / Ozempic ve uzun yaşam (düşük rekabet, yüksek arama hacmi)
- [x] Araştırma: Türkçe'de "Ozempic yaşlanma/biyolojik yaş" konusunda sadece haber/köşe yazısı formatında içerik var (Sabah, Karar) — sitenin FAQ+kaynak+yapılandırılmış blog formatında hiç yok. Ozempic Türkiye'de çok yüksek arama hacmine sahip, bu spesifik açı (longevity bilimi) düşük rekabetli.
- [x] `/blog/glp1-ilaclari-uzun-yasam/` oluşturuldu: 2026 Nature Communications epigenetik yaş çalışması (semaglutid, PhenoAge -4,9 yıl, PCGrimAge -3,1 yıl, DunedinPACE %9), mekanizma, rapamisin/NMN karşılaştırması, riskler, 3 FAQ, tam şablon (meta/OG/JSON-LD/disclaimer).
- [x] Ana sayfa blog gridine kart eklendi, `sitemap.xml`'e eklendi (23 URL), `llms.txt`'ye eklendi (ayrıca daha önce eksik kalan power-9 ve biyolojik-yasi-dusurmek girdileri de llms.txt'ye eklendi — 9 Ağustos'ta unutulmuş).
- **Not:** Bu yazı da (son 2 yazı gibi) ana sayfada JS panel olarak yok, sadece standalone sayfa + gerçek `<a href>` kartı var.

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

## Soru-tabanlı içerik genişletmesi (9 Ağustos 2026)

Google/GEO'da sağlıklı yaşam, longevity ve alkali yaşam konusunda gerçekten sorulan sorular araştırıldı (WebSearch), mevcut 19 sayfayla karşılaştırılıp gerçek boşluklar bulundu ve dolduruldu:

- [x] **alkali-beslenme:** 2 yeni FAQ — "Alkali diyet kan pH'ını gerçekten değiştirir mi?" (mit-açıklama, Healthline kaynaklı) ve "Alkali su içmek faydalı mı?" (çok aranan ama sitede hiç olmayan bir konu)
- [x] **nad-sirtuin-genleri:** "NMN takviyesi almak güvenli mi, kimler kullanmamalı?" — pratik doz/güvenlik sorusu, mevcut FAQ sadece etkinliği tartışıyordu
- [x] **sirkadiyen-beslenme:** sayfanın HİÇ sahip olmadığı FAQPage şeması + 4 soruluk "aralıklı oruç" odaklı görünür FAQ bölümü eklendi (bu terim sirkadiyen beslenmeden çok daha yüksek arama hacmine sahip)
- [x] **telomerler-nedir kontrol edildi, atlandı:** "telomer uzatma mümkün mü" sorusu zaten mevcut FAQ'de iyi cevaplanıyordu, tekrar eklenmedi
- [x] Yeni FAQ'ler hem JSON-LD (Google rich snippet) hem de görünür `<details>/<summary>` HTML olarak eklendi — önceki 7 FAQPage'in hepsi SADECE gizli şemaydı, kullanıcı hiç göremiyordu. Bu GEO için önemli: AI motorları çoğunlukla görünür metni okuyor, gizli şemayı değil.
- [x] Bu 3 sayfada eskiden beri eksik olan zp-src/zp-quote dış kaynak linkleri de eklendi (kök index.html'deki 9 Ağustos linkleme çalışması standalone sayfalara hiç yansımamıştı — bu genel bir bulgu, aşağıya not edildi)

**Yan bulgu — TÜM standalone sayfalar linksizdi, ÇÖZÜLDÜ:** kök `index.html`'e eklenen 30 dış link, ayrı blog/rehber/mavi-bölge sayfalarına (aynı içeriğin kopyaları) hiç işlenmemişti. Aynı gün içinde kalan 16 sayfaya da (51 link, Node script ile toplu, aynı doğrulanmış kaynaklar) taşındı. Artık tüm 19 standalone sayfa + kök index.html dış link içeriyor.

## Yeni blog yazıları (9 Ağustos 2026, aynı gün deploy edildi)

Kullanıcı "100 Yaşında Sağlıklı" tarzına benzer popüler konular istedi. WebSearch ile doğrulanan 2 yüksek talepli konu eklendi:

- [x] **"Power 9: Mavi Bölgelerin Ortak 9 Uzun Yaşam İlkesi"** (`/blog/power-9-mavi-bolgeler/`) — Dan Buettner'ın resmi Power 9 çerçevesi (bluezones.com kaynaklı), 9 ilkenin her biri 5 Mavi Bölge'den somut örnekle + "hangi ilke hangi bölgede en belirgin" hızlı bakış tablosuyla anlatılıyor. 5 mavi-bölge sayfasına ve rehberlere iç link veriyor.
- [x] **"Biyolojik Yaşınızı Düşürmek Mümkün mü? 10 Kanıtlanmış Yöntem"** (`/blog/biyolojik-yasi-dusurmek/`) — sitenin mevcut biyolojik yaş testine (`/#hesaplama`) ve 8 farklı iç sayfaya bağlanan, yüksek arama hacimli bir "pratik rehber" makalesi.
- [x] İkisi de FAQPage şeması + görünür FAQ + zp-disclaimer ile tam şablona uyumlu, ana sayfa blog gridine kart eklendi, `sitemap.xml` 22 URL'e çıktı.
- Site artık 22 sayfa (5 mavi bölge + 4 rehber + 11 blog + cinsiyet sayfası + ana sayfa).
- **Not:** Yeni 2 yazı, diğer 9 blog yazısından farklı olarak ana sayfada JS panel olarak yok — sadece standalone sayfa + gerçek `<a href>` linki var (SPA tekrarı yapılmadı, efor/kalite dengesi için). İstenirse ileride ana sayfaya panel olarak da eklenebilir.

**Tıbbi bilgilendirme uyarısı — TÜM 20 sayfaya eklendi (kullanıcı talebiyle, 9 Ağustos):** Daha önce sadece biyolojik yaş hesaplayıcısında "bilgilendirme amaçlıdır, tedavi değildir" uyarısı vardı; 19 makale/rehber sayfasının hiçbirinde yoktu. `.zp-disclaimer` bileşeni (assets/site.css + index.html embedded style) ile her sayfanın sonuna eklendi. NMN dozu, aralıklı oruç uygunluğu gibi eyleme geçirilebilir tavsiyeler artık hekime danışma uyarısıyla birlikte.

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
