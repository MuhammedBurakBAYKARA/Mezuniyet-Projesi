import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
import random

# 🔥 kelimeler artık ayrı dosyadan geliyor
from words import kelimeler, sentence_templates


# ==================================================
# 🎮 ANA OYUN MOTORU (Discord bot burayı çağırır)
# ==================================================
def start_game(language, difficulty):

    sample_rate = 44100
    round_count = 5
    recognizer = sr.Recognizer()
    score = 0

    # ---------------- ZORLUK → SÜRE ----------------
    if difficulty == "kolay":
        duration = 5
    elif difficulty == "orta":
        duration = 4
    else:
        duration = 3

    print("\n🎮 Oyun başladı!")
    print(f"🌍 Dil: {language} | 🎯 Zorluk: {difficulty}")

    # ==================================================
    # 🔁 OYUN DÖNGÜSÜ
    # ==================================================
    for i in range(1, round_count + 1):

        # 🎲 rastgele kelime seç
        word = random.choice(kelimeler[language][difficulty])
        sentence = sentence_templates[language].format(word)

        print("\n-----------------------------")
        print(f"🎯 Görev {i}/{round_count}")
        print("👉 Söyle:", sentence)
        print(f"⏱️ Süre: {duration} saniye")

        recording = []

        # ---------------- SES KAYDI ----------------
        def callback(indata, frames, time, status):
            recording.append(indata.copy())

        with sd.InputStream(
            samplerate=sample_rate,
            channels=1,
            dtype="int16",
            callback=callback
        ):
            sd.sleep(duration * 1000)

        # kayıtları birleştir
        audio_data = np.concatenate(recording, axis=0)
        wav.write("output.wav", sample_rate, audio_data)
        

        # ---------------- KONUŞMA TANIMA (AI) ----------------
        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)

        try:
            recognized = recognizer.recognize_google(audio, language=language)
            recognized = recognized.lower()   # 👈 Kodland ipucu

            print("📝 Algılanan:", recognized)

            # ---------------- DOĞRULUK KONTROL ----------------
            if sentence.lower() in recognized:
                print("✅ Doğru! +10 puan")
                score += 10
            else:
                print("❌ Yanlış")

        except sr.UnknownValueError:
            print("❌ Ses algılanamadı")

        except sr.RequestError as e:
            print(f"❌ Servis hatası: {e}")

    # ==================================================
    # 🏁 OYUN SONU
    # ==================================================
    print("\n🏁 Oyun bitti!")
    print("⭐ Toplam Puan:", score)

    # 🔥 BOT BURADAN SKORU ALIYOR
    return score
