from telegram import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Bot, Update,ReplyKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, CallbackContext, Updater

import json

def start(update:Update, context:CallbackContext):
    chat_id = update.message.chat_id
    text = "Assalomu alaykum shaxsiy botimga xush kelibsiz!! \n Mening messenjerdagi faoliyatimni quyidagilar orqali bilishingiz mumkin👇"
    rasm = "AgACAgIAAxkBAAMyZBnFvDEJESUrPwcofYBbaz6uRc8AApXFMRu0hNFIPwVAx-sO8jQBAAMCAANzAAMvBA"
    key1 = InlineKeyboardButton(text="Telegram", callback_data='tg' )
    key2 = InlineKeyboardButton(text="Instagram", callback_data='ins')
    key3 = InlineKeyboardButton(text="Facebook", callback_data='fc' )
    key4 = InlineKeyboardButton(text="Twitter", callback_data='tw')
    key5 = InlineKeyboardButton(text="Google account", callback_data="ak")
    keb6 = InlineKeyboardButton(text="You tube", callback_data='yt')
    key7 = InlineKeyboardButton(text='Git Hub', callback_data='gt')
    keyboard = InlineKeyboardMarkup([[key1, key2], [key3, key4], [key5, keb6], [key7]])
    bot = context.bot
    print(update.effective_chat.username)
    bot.send_photo(chat_id, rasm)
    bot.send_message(chat_id, text, reply_markup = keyboard)    

def query(update:Update, context: CallbackContext):
    query= update.callback_query
    chat_id = query.message.chat_id
    data = query.data
    bot = context.bot
        
    if data == 'tg':
        bot.sendMessage(chat_id, "@t.me/google_flutter_2003")
        
    if data == 'ins':
        bot.sendMessage(chat_id, "https://www.instagram.com/oktambek_developer2003/")
    
    if data == 'fc':
        bot.sendMessage(chat_id, "https://www.facebook.com/profile.php?id=100090769267876")
    
    if data == 'tw':
        bot.sendMessage(chat_id, "https://twitter.com/AnvarAlimnazar1")
    
    if data == 'ak':
        bot.sendMessage(chat_id, "anvaralimnazarov84@gmail.com")
        
    if data == 'yt':
        bot.sendMessage(chat_id, "https://studio.youtube.com/channel/UCQjX_43ig54pQuPfFN9XNNQ")
    
    if data == 'gt':
        bot.sendMessage(chat_id, "https://github.com/oktambek2003")