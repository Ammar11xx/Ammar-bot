import telebot
from flask import Flask
from threading import Thread
import os

# اقرأ التوكن من المتغير البيئي
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# أوامر البوت
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "👋 مرحب بيك في *بوت عمار* – @AstralBright\nحنرسل ليك دعم نفسي، تحفيز، ودعاء يومي 🧡", parse_mode='Markdown')

@bot.message_handler(commands=['motivation'])
def motivation(message):
    bot.reply_to(message, "✨ اقتباس اليوم: النجاح ما صدفة، النجاح إصرار.")

@bot.message_handler(commands=['support'])
def support(message):
    bot.reply_to(message, "🧡 التعب ما عيب، لكن تجاهل نفسك هو العيب. خليك طيب مع روحك.")

@bot.message_handler(commands=['duaa'])
def duaa(message):
    bot.reply_to(message, "🤲 دعاء اليوم: اللهم طمأنينة، ورضا، وصبر جميل.")

# تشغيل سيرفر ويب
app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()
bot.polling()
