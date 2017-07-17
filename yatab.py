#!/usr/bin/env python3


from telegram import *
import telegram
from telegram.ext import *
from telegram.bot import *
from time import *
from telegram.error import *
import logging
import calendar
import re
import math
import sys

from config import TOKEN, commands, onjoin

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def onJoinHandler(bot,update):
    for mod in onjoin:
        mod.cb(bot,update)

def main():
    #define bot
    bot = telegram.Bot(TOKEN)

    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    #bot.GetUpdate()
    dp = updater.dispatcher
    # on different commands - answer in Telegram
    print("Loading Modules")
    
    #init module
    for mod in commands:
        print(mod.name)
        dp.add_handler(CommandHandler(mod.name,mod.cb,pass_args=mod.args))
    
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members,onJoinHandler))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling(clean=True)

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

