import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from keep_alive import keep_alive

# টোকেন .env ফাইল থেকে নিচ্ছে
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    text = (
        "🔐 *আপনার Twilio SID এবং Token এইভাবে পাঠান:*\n"
        "`ACxxxxxxxxxxxxxxxxxxxx TOKENxxxxxxxxxxxxxxxxxxxx`"
    )
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🌐 Login 🔑", callback_data="login"))
    markup.row(InlineKeyboardButton("🔍 Search Number", callback_data="search"))
    markup.row(InlineKeyboardButton("🌍 Random Area Code", callback_data="random"))
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "login":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🔐 Twilio SID এবং Token পাঠান যেমন:\n`ACxxxx TOKENxxxx`", parse_mode="Markdown")
    elif call.data == "search":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🔍 Area Code দিয়ে নাম্বার সার্চ করতে `/buy <area_code>` লিখুন (যেমন `/buy 672`)")
    elif call.data == "random":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🌍 র‍্যান্ডম এরিয়া কোড থেকে নাম্বার খোঁজা হচ্ছে... (পরবর্তী ধাপে হবে)")

keep_alive()  # Replit 24/7 চালু রাখতে
bot.infinity_polling()
