# Farmakoloji Pulse

Farmakoloji ve eczacılık literatüründen öne çıkan makaleleri PubMed'den çekip,
dergi ağırlığı ve makale tipine göre skorlayıp konu bölümlerine ayırarak listeleyen araç.
Ayrıca "Best of 2026" (etki faktörüne göre) ve YÖK'ten farmakoloji tezleri bölümleri içerir.

## Dosyalar

- `index.html` — site (veriyi `data.json`, `best2026.json`, `tez2026.json`'dan okur)
- `fetch_articles.py` — PubMed'den çekip skorlar, bölümler ve `data.json` + `best2026.json` üretir
- `config.py` — dergiler, tier'lar, etki faktörleri, bölüm anahtar kelimeleri (asıl özelleştirme burada)
- `data.json` / `best2026.json` / `tez2026.json` — veri
- `.github/workflows/update.yml` — her gün otomatik güncelleme (GitHub Actions)

## GitHub Pages'te yayınlama

1. Bu klasörü **ayrı bir** GitHub deposuna yükle (örn. `farmakoloji-pulse`).
2. Depoda **Settings → Pages → Deploy from a branch → main / (root)** seç.
3. Site `https://KULLANICI_ADIN.github.io/farmakoloji-pulse/` adresinde yayında olur.

## Otomatik günlük güncelleme

`.github/workflows/update.yml` her gün 06:00 UTC'de çalışır; PubMed'den çeker, çevirir,
`data.json` ve `best2026.json`'u güncelleyip commit'ler. İlk çalıştırmayı **Actions → Run workflow**
ile elle tetikle ve **Settings → Actions → Workflow permissions**'ı "Read and write" yap.

Tezler (`tez2026.json`) YÖK'ten periyodik olarak elle güncellenir (günlük değişmez).

## Lokal çalıştırma

```bash
pip install -r requirements.txt
python fetch_articles.py
python -m http.server 8000   # sonra http://localhost:8000
```

## Özelleştirme

`config.py` içinde dergi tier'larını, etki faktörlerini, bölüm anahtar kelimelerini
(`SECTION_KEYWORDS`) ve tarih penceresini (`RELDATE_DAYS`) düzenleyebilirsin.
