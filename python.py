import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8920369792:AAHpZuBMLSFuOYvXP8AxGc1i8jFrvCBz9vA"

# گرفتن قیمت بیتکوین
def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = data["bitcoin"]["usd"]
    return price

# دستور /btc
async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price = get_btc_price()
    await update.message.reply_text(f"₿ Bitcoin Price: {price} USD")

# ساخت ربات
app = ApplicationBuilder().token("8920369792:AAHpZuBMLSFuOYvXP8AxGc1i8jFrvCBz9vA").build()

app.add_handler(CommandHandler("btc", btc))

print("Bot is running...")
app.run_polling()
