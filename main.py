#python main.py
import os
import telebot
from telethon import TelegramClient, events, utils
import hashlib
#import pyrogram
#from pyrogram import Client
#from telethon import TelegramClient, events, sync
#from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.sync import TelegramClient, events
import asyncio
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# mastrobot_example.py
#from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import time



#https://api.telegram.org/bot2101223986:AAG20DUvLtXZH6NKNlipxNv2WCEi8iU2rMI/setWebhook?url=https://mytelegrambotserverb.herokuapp.com/bot.php

api_id=16292196
TELEGRAM_API_ID = '16292196'
api_hash='23a429d30fdf45ef4b051b26d36588d8'
TELEGRAM_API_HASH = '23a429d30fdf45ef4b051b26d36588d8'
#TOKEN='2101223986:AAG20DUvLtXZH6NKNlipxNv2WCEi8iU2rMI'
T='2101223986:AAG20DUvLtXZH6NKNlipxNv2WCEi8iU2rMI'
APP_NAME='mytelegrambotserverb'

"""
#api_id = 9999900
#api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
"""

client = TelegramClient('anon', api_id, api_hash)
# Create bot
bot = telebot.TeleBot(token=T)

#myChannelIDList = [xxxxxxxxxxx,xxxxxxxxxxx,myChannelName,...]
myChannelIDList = ["https://t.me/s/fireisrael777/0","https://t.me/rtnews/0","https://t.me/s/IranintlTV/0",-1001166797460,"https://t.me/almayadeen/0","https://t.me/Alarabiya/0","https://t.me/Reutersps/0","https://t.me/translateNewsReported"]

destChl="https://t.me/newsExtraReported"

# Enables logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

#PORT = int(os.environ.get('PORT', '8443'))
PORT = int(os.environ.get('PORT', 5000))

# We define command handlers. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Sends a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Sends a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echos the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Logs Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Starts the bot."""
    # Creates the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    TOKEN = '2101223986:AAG20DUvLtXZH6NKNlipxNv2WCEi8iU2rMI'#enter your token here
    APP_NAME='https://mytelegrambotserverb.herokuapp.com/'#Edit the heroku app-name
    
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN, webhook_url=APP_NAME + TOKEN)
    #updater.bot.setWebhook(APP_NAME + TOKEN) 
    updater.idle()


if __name__ == '__main__':
    main()



client.start()
client.run_until_disconnected()

