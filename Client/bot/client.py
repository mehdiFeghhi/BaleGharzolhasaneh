import json


from telegram import Bot, Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, \
    LabeledPrice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler

# Enable logging
from DB.db_handler import *
from Client.constants.client_constants import *
from Client.constants.client_constants import ConversationStates

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger()


# ++++++++++++++++++++++++++ choose Gharzolhasaneh scenario ++++++++++++++++++++++++++++

def start(bot: Bot, update: Update, user_data):
    logger.info(start.__name__)
    user = get_user(update.message.chat_id)
    if user is not None:

        kb = [[InlineKeyboardButton(text=Keyboards.date_last_pay,callback_data="DLP")],
              [InlineKeyboardButton(text=Keyboards.dates_of_all_time,callback_data="DOAT")],
              [InlineKeyboardButton(text=Keyboards.amount_of_each_time,callback_data="AOET")],
              [InlineKeyboardButton(text=Keyboards.date_day_must_pay,callback_data="DDMP")],
              [InlineKeyboardButton(text=Keyboards.change_date_of_pay,callback_data="CDOP")],
              [InlineKeyboardButton(text=Keyboards.change_amount_of_pay,callback_data="CAOP")]]
        reply_markup = ReplyKeyboardMarkup(kb)
        update.message.reply_text(BotMessages.start, reply_markup=reply_markup)
        return ConversationStates.CATEGORY
    else:
        kb = [[InlineKeyboardButton(text=Keyboards.register, callback_data="REG")],
              [InlineKeyboardButton(text=Keyboards.read_me, callback_data="REM")]]
        reply_markup = InlineKeyboardMarkup(kb)
        update.message.replay_text(BotMessages.start, reply_markup=reply_markup)
        return ConversationStates.CATEGORY

def see_last_pay(bot, update, user_date):
    logger.info(see_last_pay.__name__)
    data = get_user_receipts(update.message.chat_id)
    update.message.replay_text(data[0])
    return ConversationHandler.END


def see_all_of_pay(bot, update, user_date):
    logger.info(see_all_of_pay.__name__)
    data = get_user_receipts(update.message.chat_id)
    update.message.replay_text(data)
    return ConversationHandler.END


def success_receipt_handler(bot, update, user_data):
    if update.message.chat_id == 11:
        logger.info(success_receipt_handler.__name__)
        successful_payment = update.message.successful_payment
        invoice_payload = json.loads(successful_payment.invoice_payload)
        msg_uid = invoice_payload.get('msgUID').split('-' + invoice_payload.get('msgDate'))[0]
        # order = get_order_by_msg_uid(msg_uid)
        # add_payment(order_id=order.id, amount=successful_payment.total_amount, msg_uid=msg_uid,
        #             traceNo=invoice_payload.get('traceNo'))
        # set_order_shown_order(order.id, False)
        # bot.send_message(chat_id=order.customer_chat_id, text=BotMessages.success_payment)
    return ConversationHandler.END


# ++++++++++++++++++++++++++ cancel ++++++++++++++++++++++++++++
def cancel(bot, update):
    logger.warning(cancel.__name__)
    update.message.reply_text('Bye! I hope we can talk again some day.')
    return ConversationHandler.END


def error(bot, update, error_ex):
    logger.error(error.__name__)
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, update.message)
