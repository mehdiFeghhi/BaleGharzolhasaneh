import json

import persian
from telegram import (ReplyKeyboardMarkup, LabeledPrice, SuccessfulPayment)
from telegram.ext import *

# Enable logging
from DB.db_handler import *
from Client.constants.client_constants import *
from Client.constants.client_constants import ConversationStates

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger()


# ++++++++++++++++++++++++++ choose Gharzolhasaneh scenario ++++++++++++++++++++++++++++

def start(bot, update, user_data):
    logger.info(start.__name__)
    user = get_user(update.message.chat_id)
    if user is not None:

        kb = [[Keyboards.date_last_pay],[Keyboards.dates_of_all_time],[Keyboards.amount_of_each_time],
              [Keyboards.date_day_must_pay],[Keyboards.change_date_of_pay],[Keyboards.change_amount_of_pay]]
        reply_markup = ReplyKeyboardMarkup(keyboard=kb)
        update.message.replay_text(BotMessages.start,reply_markup=reply_markup)
        #todo add this
        # return ConversationStates.start_1
    else:
        kb =[[Keyboards.register],[Keyboards.read_me]]
        #todo add this
        # return ConversationStates.start_2

def see_last_pay(bot,update,user_date):
    logger.info(see_last_pay.__name__)
    data = get_user_receipts(update.message.chat_id)
    update.message.replay_text(data[0])
    return ConversationHandler.END

def see_all_of_pay(bot,update,user_date):
    logger.info(see_all_of_pay.__name__)
    data = get_user_receipts(update.message.chat_id)
    update.message.replay_text(data)
    return ConversationHandler.END




