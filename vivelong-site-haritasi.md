# Vivelong — Site Haritası ve Geliştirme Geçmişi

**URL:** https://vivelong.com  
**Domain:** vivelong.com  
**Hosting:** Netlify (proje adı: `longeage`)  
**Kaynak dosyalar:** `Desktop/longeage.html` → `Desktop/longeage-deploy/index.html`  
**Teknoloji:** Tek sayfalık HTML (vanilla JS, CSS, Google Fonts)

---

## Ana Sayfa Bölümleri (Scroll ile Gezilen)

Ana sayfa tek bir HTML dosyasından oluşur. Kullanıcı sayfayı aşağı kaydırarak bölümler arasında gezer.

| # | Bölüm Adı | Anchor ID | Açıklama |
|---|-----------|-----------|----------|
| 1 | **Hero** | — | "Daha Uzun, Daha Sağlıklı Yaşayın" — Giriş ekranı, CTA butonları, istatistikler |
| 2 | **Biyolojik Yaş Testi** | `#hesaplama` | 16 faktörlü interaktif hesaplayıcı (yaş, cinsiyet, BMI, 11 soru) → biyolojik yaş sonucu ve faktör katkı grafikleri |
| 3 | **Longevity Alışkanlıkları** | `#aliskanliklar` | 22 günlük takip alışkanlığı, ilerleme çubuğu, gün sonu sıfırlanır (localStorage) |
| 4 | **Mavi Bölgeler** | `#mavi-bolgeler` | 5 mavi bölge kartı (tıklanınca detay sayfası açılır) |
| 5 | **Hücresel Yaş Göstergeleri** | `#biyomarker` | Telomer, inflamasyon, insülin direnci, mitokondri, epigenetik — NCBI PMC11688636 kaynaklı |
| 6 | **Cinsiyet & Uzun Yaşam Paradoksu** | `#paradoks` | Kadın/erkek ömür farkı, sağlık paradoksu özet kartları |
| 7 | **Uzun Yaşamın Dört Temel Taşı** | `#direkleri` | Beslenme, Sosyal Bağ, Hareket, Uyku — detay sayfası açan kartlar |
| 8 | **Bilim Ne Diyor?** | `#bilim` | Araştırma istatistikleri, longevity bulguları |
| 9 | **Blog & Araştırma** | `#blog` | 9 bilim makalesi kartı (tıklanınca detay sayfası açılır) |
| 10 | **Üyelik / Freemium** | `#uyelik` | Ücretsiz & Pro planları, aylık/yıllık toggle (%17 indirim), fiyatlandırma |

---

## Zone Sayfaları (Slide-In Tam Ekran)

Belirli kartlara tıklanınca ekranın sağından kayan tam ekran sayfalar. Her sayfada sol üstte **Vivelong logosu** (ana sayfaya döner) ve **Geri butonu** bulunur.

### Mavi Bölgeler

| ID | Sayfa | Konum |
|----|-------|-------|
| `zp-sardunya` | 🇮🇹 Sardunya, İtalya (Barbagia Vadisi) | Beslenme, yaşam tarzı, aile/topluluk, Power 9 |
| `zp-okinawa` | 🇯🇵 Okinawa, Japonya (Ryukyu) | Hara hachi bu, tatlı patates, Moai, İkigai |
| `zp-nicoya` | 🇨🇷 Nicoya, Kosta Rika (Guanacaste) | Üç Kız Kardeş (fasulye/mısır/kabak), Plan de Vida, sert su |
| `zp-ikaria` | 🇬🇷 Ikaria, Yunanistan (Ege) | Yabani yeşillikler, öğle şekerlemesi, bitki çayları |
| `zp-loma` | 🇺🇸 Loma Linda, California (ABD) | Vejeteryan beslenme, Şabat, Adventist Health Study |

> Her Mavi Bölge sayfasında bölgeler arası geçiş butonları bulunur.

### Cinsiyet

| ID | Sayfa | İçerik |
|----|-------|--------|
| `zp-gender` | Cinsiyet & Uzun Yaşam Paradoksu | Lifespan-healthspan uçurumu, hormonal değişimler (menopoz/andropos), cinsiyete özel longevity stratejileri (Kadınlar İçin / Erkekler İçin), ortak 4 faktör |

### Dört Temel Taş Rehberleri

| ID | Sayfa | İçerik |
|----|-------|--------|
| `zp-beslenme` | Longevity Beslenmesi | Bitkisel beslenme, mikrobiyom, polifenoller, besin yoğunluğu |
| `zp-baglanma` | Sosyal Bağ & Amaç | Sosyal izolasyonun sağlık etkisi, topluluk, yaşam amacı |
| `zp-hareket` | Hareket & Egzersiz | Bölge 2 kardiyo, güç egzersizi, sarkopeni, NEAT, Haftalık Hareket Çerçevesi (Minimum / Optimal hedef) |
| `zp-uyku` | Uyku & Zihin Sağlığı | Uyku mimarisi, sirkadiyen ritim, beyin temizliği (glenfatik sistem), uyku hijyeni |

### Blog & Araştırma

| ID | Makale Başlığı | Okuma |
|----|----------------|-------|
| `zp-blog1` | Telomerler: Yaşam Sürenizin Biyolojik Saati | ~7 dk |
| `zp-blog2` | Otofaji: Hücrenin Öz-Temizleme Mucizesi | ~8 dk |
| `zp-blog3` | Epigenetik: Genleriniz Kaderiniz Değil | ~6 dk |
| `zp-blog4` | Inflammaging: Sizi Sessizce Yaşlandıran İltihap | ~7 dk |
| `zp-blog5` | 100 Yaşında Sağlıklı: Süper Yaşlılardan Dersler | ~8 dk |
| `zp-blog6` | NAD+ ve Sirtuin Genleri: Uzun Yaşamın Moleküler Sırrı | ~9 dk |
| `zp-blog7` | Alkali Beslenme: pH Dengesi ve Uzun Yaşam | ~8 dk |
| `zp-blog8` | Sirkadiyen Beslenme: Ne Zaman Yediğin de Önemli | ~7 dk |
| `zp-blog9` | Mitokondri: Uzun Yaşamın Enerji Merkezi | ~9 dk |

### Pro

| ID | Sayfa | İçerik |
|----|-------|--------|
| `zp-pro` | Vivelong Pro Tanıtım | Pro özellikleri, plan karşılaştırması, fiyatlandırma detayları |

---

## Navigasyon

```
Navbar (sabit, üstte):
  Logo (Vivelong) → Ana sayfa en üstüne scroll
  Yaş Testi       → #hesaplama
  Alışkanlıklar   → #aliskanliklar
  Hücresel Yaş    → #biyomarker
  Mavi Bölgeler   → #mavi-bolgeler
  Cinsiyet        → #paradoks
  4 Temel Taş     → #direkleri
  Blog            → #blog
  [Pro]           → #uyelik
  [Başla]         → #hesaplama
```

---

## Floating Bileşenler

- **Yukarı Çık Butonu** — Sayfa aşağı kaydırıldığında sağ altta görünür, tıklanınca başa döner
- **AI Longevity Asistanı (FAB)** — Sağ altta sohbet butonu; açılınca hazır sorular ve metin girişi

---

## Geliştirme Geçmişi (Bu Konuşmada Yapılanlar)

### 1. Logo → Ana Sayfa Scroll (Doğrulama)
- **Sorun:** Logo tıklandığında ana sayfaya dönmüyor mu?
- **Sonuç:** Kod zaten mevcuttu (`onclick="event.preventDefault();window.scrollTo({top:0,behavior:'smooth'})"`) ve çalışıyordu. Canlı sitede doğrulandı.

### 2. Mavi Bölgeler — Başlık/Açıklama Düzeni Düzeltmesi
- **Sorun:** `.zp-ul li` öğeleri `display:flex` olduğu için `<b>` başlık etiketi ve açıklama metni ayrı flex item'lar haline geliyordu → alt alta görünüm bozukluğu.
- **Çözüm (CSS):**
  ```css
  /* Öncesi */
  .zp-ul li { display:flex; align-items:flex-start; gap:9px; padding:10px 13px; }
  .zp-ul li::before { flex-shrink:0; margin-top:8px; }

  /* Sonrası */
  .zp-ul li { display:block; position:relative; padding:10px 13px 10px 28px; padding-left:28px !important; }
  .zp-ul li::before { position:absolute; left:13px; top:16px; }
  ```
- **Kapsam:** Tüm zone sayfalarındaki `.zp-ul li` öğeleri (Mavi Bölgeler ×5, Cinsiyet, Hareket, Uyku, Beslenme, Sosyal Bağ, Blog ×9)

### 3. Başlık/Açıklama Görsel Ayrımı
- **Sorun:** Başlık (bold) ve açıklama metni aynı satırda akıyordu, görsel hiyerarşi yoktu.
- **Çözüm (CSS):**
  ```css
  .zp-ul li b { display:block; color:var(--primary); font-size:13px; font-weight:700; margin-bottom:3px; }
  ```
- **Sonuç:** Her maddede başlık kendi satırında (yeşil, bold), açıklama altında.

### 4. Bullet/Metin Çakışması — Inline Padding Override
- **Sorun:** Kadınlar/Erkekler İçin ve Haftalık Hareket Çerçevesi'ndeki `<li>` öğeleri `style="padding:7px 10px"` inline stili taşıyordu → CSS'deki `padding-left:28px` override ediliyordu → bullet nokta metinle çakışıyordu.
- **Çözüm:** `padding-left:28px !important` eklendi.

### 5. Tüm Zone Sayfalarına Ana Sayfa Logosu
- **Sorun:** Zone sayfaları açıldığında ana sayfaya dönmek için tek yol navbar'daki geri butonu (önceki section'a döner).
- **Çözüm:**
  - `goHome()` fonksiyonu eklendi: açık tüm zone'ları kapatır + `scrollTo(top:0)`
  - JavaScript ile sayfa yüklenince tüm `.zp-topbar` öğelerine Vivelong logosu enjekte edildi
  - Logo + Geri butonu `div.zp-topbar-left` wrapper içinde gruplanarak layout korundu
  - CSS: `.zp-topbar-left`, `.zp-home-logo` stilleri eklendi

### 6. Netlify Deploy'lar
| Tarih | Deploy URL | Değişiklik |
|-------|------------|------------|
| 2026-06-28 | `6a4184d4cea724a96fe6d73e--longeage.netlify.app` | Mavi Bölgeler başlık/açıklama düzeni |
| 2026-06-28 | `6a4188af042c98f4cf0da7dc--longeage.netlify.app` | Bullet çakışması + Ana sayfa logosu |

---

## Dosya Yapısı

```
Desktop/
├── longeage.html                  ← Kaynak (geliştirme) dosyası
└── longeage-deploy/
    └── index.html                 ← Netlify'a yüklenen dosya
```

> `longeage.html` düzenlendikten sonra değişiklikler `longeage-deploy/index.html` dosyasına da uygulanmalı, ardından `netlify deploy --prod --dir=.` ile yayınlanmalıdır.

---

## Teknik Notlar

- **Scroll davranışı:** `html { scroll-behavior: smooth; }` — tüm anchor linkleri smooth scroll yapar
- **Zone sayfaları:** `position:fixed; transform:translateX(100%)` → `.open` class'ı ile `translateX(0)` → sağdan kayan geçiş animasyonu (0.38s cubic-bezier)
- **Alışkanlık verisi:** `localStorage` ile saklanır, her gün gece yarısı sıfırlanır
- **Biyolojik yaş hesabı:** 16 faktör (yaş, BMI, cinsiyet + 11 yaşam tarzı sorusu) — NCBI araştırma modellerine dayalı
- **Fontlar:** Lora (serif, başlıklar) + Raleway (sans-serif, gövde) — Google Fonts
- **Renk paleti:** Yeşil (`#1A4731`, `#2D6A4F`, `#40916C`) + Altın (`#D4A847`) + Açık yeşil (`#74C69D`)
