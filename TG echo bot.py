import logging
import responses
from telegram.ext import *
import os
os.system('cls')

API_key = "TOKEN"

#set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting bot ... ')
#logger = logging.getLogger(__name__)

def start_command(update, context):
    update.message.reply_text('Hi!')

def help_command(update, context):
    update.message.reply_text('Google it!')

def custom_command(update, context):
    update.message.reply_text('This is custom command!, you can add more texts here.')

def handler_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    #bot response
    update.message.reply_text(text)

def echo(update, context):
    update.message.reply_text(update.message.reply_text)

def error(update, context):
    #log errors
    logging.error(f'Update {update} caused error {context.error}')

def main():
    updater = Updater(API_key, use_context=True)
    dp = updater.dispatcher

    #commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    #messages
    dp.add_handler(MessageHandler(Filters.text, echo))
    #it handles our message handlers

    #log all errors
    dp.add_error_handler(error)

    #run the bot
    #this two lines of codes, will start our bot and make sure that it runs continuously
    updater.start_polling(1.0) 
    updater.idle()

 
if __name__ == '__main__':
    main()

#end of code
#now you have echo bot in telegram