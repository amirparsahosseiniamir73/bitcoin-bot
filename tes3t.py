
# import requests

# api_key = "209bad98dd644fc2839c5a9e50fe5a43"

# url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

# params = {
#     "id": "1",   # بیت‌کوین در CoinMarketCap همیشه id=1 است
#     "convert": "USD"
# }

# headers = {
#     "X-CMC_PRO_API_KEY": api_key,
#     "Accept": "application/json"
# }

# response = requests.get(url, params=params, headers=headers)
# data = response.json()
# price = data["data"]["1"]["quote"]["USD"]["price"]
# market_cap = data["data"]["1"]["quote"]["USD"]["market_cap"]
# volume = data["data"]["1"]["quote"]["USD"]["volume_24h"]
# change = data["data"]["1"]["quote"]["USD"]["percent_change_24h"]
# print(f"Bitcoin Price: {price}")
# print(f"Market Cap: {market_cap}")
# print(f"Volume 24h: {volume}")
# print(f"Change 24h: {change}%")
# if change> 3 and volume > 30000000000:
#     print("bazar kheli gaviye")
# if change < -3 and volume > 30000000000 :
#     print("feshar forosh shadid")
# if -3 < change < 3:
#     print("bazarrenge")
# if price > 100000 and change>0:
#     print("bitcoin faz soudi sangin ast")
# import requests
# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# BOT_TOKEN = "8920369792:AAHpZuBMLSFuOYvXP8AxGc1i8jFrvCBz9vA"
# CMC_API = "209bad98dd644fc2839c5a9e50fe5a43"

# # گرفتن قیمت بیتکوین
# def get_btc_price():
#     url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

#     params = {
#         "id": "1",
#         "convert": "USD"
#     }

#     headers = {
#         "X-CMC_PRO_API_KEY": CMC_API,
#         "Accept": "application/json"
#     }

#     response = requests.get(url, params=params, headers=headers)
#     data = response.json()

#     price = data["data"]["1"]["quote"]["USD"]["price"]
#     return price

# # دستور /btc
# async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     price = get_btc_price()
#     await update.message.reply_text(f"₿ Bitcoin Price: {price} USD")

# # ساخت ربات
# app = ApplicationBuilder().token("8920369792:AAHpZuBMLSFuOYvXP8AxGc1i8jFrvCBz9vA").build()

# app.add_handler(CommandHandler("btc", btc))

# print("Bot is running...")
# app.run_polling()
# import requests
# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# BOT_TOKEN = "8920369792:AAHpZuBMLSFuOYvXP8AxGc1i8jFrvCBz9vA"
# CMC_API = "209bad98dd644fc2839c5a9e50fe5a43"

# def get_btc_price():
#     url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

#     params = {
#         "id": "1",
#         "convert": "USD"
#     }

#     headers = {
#         "X-CMC_PRO_API_KEY": CMC_API
#     }

#     response = requests.get(url, params=params, headers=headers)

#     if response.status_code != 200:
#         return f"API Error: {response.status_code}"

#     data = response.json()

#     try:
#         price = data["data"]["1"]["quote"]["USD"]["price"]
#         return round(price, 2)
#     except:
#         return "خطا در دریافت قیمت"

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("سلام! برای قیمت بیت‌کوین /btc را بزن.")

# async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     price = get_btc_price()
#     await update.message.reply_text(f"BTC Price: {price} USD")

# app = ApplicationBuilder().token(BOT_TOKEN).build()

# app.add_handler(CommandHandler("start", start))
# app.add_handler(CommandHandler("btc", btc))

# print("Bot Started")

# app.run_polling()
#in geymat zende bitcoin be dollare!
# import requests
# def get_btc_price():
#     url="https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
#     respons=requests.get(url)
#     data=respons.json()
#     price=data['bitcoin']['usd']

#     return price
# # (f"Bitcoin Price: {get_btc_price()} usd")
# def btc():
#     price=get_btc_price()

#     payam=f"Bitcoin Price: {price} usd"

#     return payam
# x=btc()
# print(x)
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
