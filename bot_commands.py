from telegram import Update
from telegram.ext import CallbackContext
import datetime

def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hi {update.effective_user.first_name}')
    
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/hi\n/time\n/help\n/sum')

def time_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'{datetime.datetime.now().time()}')

def sum_command(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split() # /sum 123 45678
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')