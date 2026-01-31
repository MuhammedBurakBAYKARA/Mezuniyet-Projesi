
# 🎮 Yapay Zeka Destekli Dil Öğreten Discord Botu

## 📌 Proje Amacı
Bu proje, Discord üzerinde çalışan yapay zeka destekli bir dil öğrenme oyunudur.
Kullanıcıların konuşmalarını analiz ederek doğru telaffuz yapmalarını sağlar ve puanlama sistemi ile öğrenmeyi eğlenceli hale getirir.

Kullanıcılar seçtikleri dilde cümleleri doğru şekilde telaffuz etmeye çalışır ve yapay zeka konuşmayı analiz ederek doğruluğunu kontrol eder.

---

## 🚀 Kullanılan Teknolojiler

🐍 Python  
🤖 discord.py (Discord Botu geliştirme)  
🧠 SpeechRecognition (Konuşma tanıma – Yapay Zeka)  
🎤 sounddevice (Mikrofon kaydı)  
🔊 scipy & numpy (Ses işleme)  
🎲 random (Rastgele kelime seçimi)

---

## 🧠 Yapay Zeka Özellikleri

Projede aşağıdaki yapay zeka teknikleri kullanılmıştır:

✅ Konuşma Tanıma (Speech Recognition)  
✅ Doğal Dil İşleme (NLP)  
✅ Ses analizi  
✅ Metin karşılaştırma algoritması  
✅ Doğru / yanlış otomatik değerlendirme  

Bot, kullanıcının söylediği sesi yazıya çevirir ve hedef cümle ile karşılaştırarak sonucu belirler.

---

## 🎮 Oyun Nasıl Çalışır?

1️⃣ Kullanıcı Discord'da komut yazar  
2️⃣ Dil seçer (İngilizce / Almanca / Fransızca / Rusça)  
3️⃣ Zorluk seviyesi seçer (kolay / orta / zor)  
4️⃣ Bot rastgele bir kelime seçer  
5️⃣ Kelime ile otomatik cümle oluşturur  
6️⃣ Kullanıcı mikrofondan cümleyi söyler  
7️⃣ Yapay zeka konuşmayı analiz eder  
8️⃣ Doğruysa +10 puan kazanır  
9️⃣ Oyun sonunda toplam skor gösterilir  

---

## 🌍 Desteklenen Diller

- 🇬🇧 İngilizce
- 🇩🇪 Almanca
- 🇫🇷 Fransızca
- 🇷🇺 Rusça

---

## 🎯 Zorluk Seviyeleri

| Seviye | Süre | Açıklama |
|-------|------|-----------|
| Kolay | 5 sn | Basit kelimeler |
| Orta  | 4 sn | Orta uzunlukta kelimeler |
| Zor   | 3 sn | Uzun ve zor kelimeler |

---

## 📂 Proje Dosya Yapısı

mezuniyet_projesi/
│
├── bot.py → Discord bot ana dosyası
├── ai_engine.py → Yapay zeka oyun motoru
├── words.py → Kelime ve cümle listeleri
├── requirements.txt → Gerekli kütüphaneler
└── README.md

---

## ⚙️ Kurulum

### 1) Depoyu indir

git clone <repo-link>
cd mezuniyet_projesi

### 2) Gerekli kütüphaneleri yükle

pip install -r requirements.txt

---

## ▶️ Botu Çalıştırma

python bot.py


Bot başlatıldıktan sonra Discord sunucunda komutları kullanabilirsin.

---

## 💡 Örnek Oyun Akışı

🎯 Görev 1
👉 I like apple
🎤 Konuşmaya başla...
📝 Algılanan: I like apple
✅ Doğru! +10 puan


---

## 🎓 Proje Konusu

Bu proje aşağıdaki iki alanın birleştirilmesi ile geliştirilmiştir:

✅ Yapay Zeka  
✅ Discord Botları  

Amaç: Yapay zekayı eğitsel ve eğlenceli bir uygulamada kullanmak.

---

## 👨‍💻 Geliştirici Bilgileri

İsim: M.Burak  
Ders: Kodland/Python - Mezuniyet Projesi  
Alan: Yapay Zeka & Discord Bot Geliştirme  
Yıl: 2026  

---

## ⭐ Gelecekte Eklenebilecek Özellikler

- 🏆 Liderlik tablosu (scoreboard)
- 📈 Seviye sistemi
- 🔊 Sesli geri bildirim
- 🌐 Daha fazla dil desteği
- 🧠 Daha gelişmiş telaffuz analizi
- ☁️ Veritabanı entegrasyonu

---

## 🎉 Sonuç

Bu proje sayesinde:
- Yapay zeka ile konuşma tanıma öğrenildi
- Discord bot geliştirme pratiği yapıldı
- Python ile gerçek bir uygulama geliştirildi

👉 Hem eğitici hem eğlenceli bir dil öğrenme deneyimi sunulmuştur.

🚀 Teşekkürler!


