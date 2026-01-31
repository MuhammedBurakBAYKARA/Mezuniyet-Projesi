import discord
from discord.ext import commands
import asyncio

# 👇 birazdan ai_engine.py içinden fonksiyon çağıracağız
from ai_engine import start_game


# ---------------- BOT AYARLARI ----------------
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)


# ---------------- BOT AÇILDI ----------------
@bot.event
async def on_ready():
    print(f"🤖 Bot hazır: {bot.user}")


# ---------------- YARDIMCI FONKSİYON ----------------
async def ask_question(ctx, question, valid_answers):
    """
    Kullanıcıdan mesaj bekler ve doğrular
    """
    await ctx.send(question)

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        msg = await bot.wait_for("message", timeout=30.0, check=check)
        answer = msg.content.lower()

        if answer in valid_answers:
            return answer
        else:
            await ctx.send("❌ Geçersiz seçim!")
            return None

    except asyncio.TimeoutError:
        await ctx.send("⏰ Süre doldu!")
        return None


# ---------------- /basla KOMUTU ----------------
@bot.command()
async def basla(ctx):
    await ctx.send("🎮 **Yapay Zeka Destekli Dil Oyunu Başlıyor!** 🚀")

    # 🌍 DİL SEÇİMİ
    language = await ask_question(
        ctx,
        "🌍 Dil seç:\n`en` 🇬🇧 | `de` 🇩🇪 | `fr` 🇫🇷 | `ru` 🇷🇺",
        ["en", "de", "fr", "ru"]
    )

    if not language:
        return

    # 🎯 ZORLUK SEÇİMİ
    difficulty = await ask_question(
        ctx,
        "🎯 Zorluk seç:\n`kolay` 🟢 | `orta` 🟡 | `zor` 🔴",
        ["kolay", "orta", "zor"]
    )

    if not difficulty:
        return

    await ctx.send("⏳ Oyun başlatılıyor... 🎤")

    # 👇 Yapay zeka oyun motorunu çalıştır
    score = start_game(language, difficulty)

    await ctx.send(f"🏁 Oyun bitti!\n⭐ Toplam puanın: **{score}**")


# ---------------- TOKEN ----------------
bot.run("BURAYA_TOKENUNU_YAPIŞTIR")
