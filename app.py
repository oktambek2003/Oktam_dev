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

@app.route('/', methods=['POST', 'GET'])
def home():
        
        return 'welcome'
if __name__ == '__main__':
    # Run the app in local network
    app.run()