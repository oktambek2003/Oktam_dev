from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackQueryHandler, CallbackContext, Updater, Dispatcher
from flask import Flask, request
import requests
from main import (
    start,
    pictures,
    query,

)

app = Flask(__name__)

# bot
TOKEN = "6063934394:AAExwcUz_3z3LICpws1dzUfZjqN7KtOLbMk"
bot = Bot(TOKEN)

@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return 'hello'
    if request.method == "POST":
        data = request.get_json(force=True)

        dispatcher: Dispatcher = Dispatcher(bot, None, workers=0)
        update: Update = Update.de_json(data, bot)

        dispatcher.add_handler(CommandHandler("start", start))

        dispatcher.add_handler(CallbackQueryHandler(query))

        dispatcher.process_update(update)
        return 'welcome'