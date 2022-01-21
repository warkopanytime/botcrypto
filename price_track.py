import requests
import telegram
import json

from telegram.forcereply import ForceReply
from telegram.ext import Updater
from telegram.ext import CommandHandler
from local_config import TOKEN

telegram_bot_token = TOKEN

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

def harga(update, context):
    chat_id = update.effective_chat.id

    pair = context.args[0]

    base_url = "https://indodax.com/api/ticker"

    coin = f"{base_url}/{pair}idr"

    response = requests.get(coin)

    if response.json().get("ticker"):
        text = response.json().get("ticker").get("last")
        text = "{:0,}".format(float(text))
        text = f"harga {pair} Rp {text} cok!"
    else:
        text = f"{pair} iku token apaan cok ?!"
    context.bot.send_message(chat_id=chat_id, text=text)

def help(update, context):
    chat_id = update.effective_chat.id
    content = "Harga Crypto di bot ini diambil dari INDODAX \n contoh : /harga doge"
    context.bot.send_message(chat_id=chat_id, text=content)

dispatcher.add_handler(CommandHandler("harga", harga))
dispatcher.add_handler(CommandHandler("help", help))

updater.start_polling()
