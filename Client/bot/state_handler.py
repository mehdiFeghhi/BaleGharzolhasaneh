from telegram import Bot
from telegram.ext import RegexHandler

from Client.bot.client import *
from Client.constants.client_constants import Keyboards
from Client.constants.client_constants import ConversationStates
from main_config import BotConfig


def main():
    # bot = Bot(token=BotConfig.client_token,
    #           base_url=BotConfig.base_url,
    #           base_file_url=BotConfig.base_file_url)
    # updater = Updater(bot=bot)
    updater = Updater(token=BotConfig.client_token, base_url=BotConfig.base_url)
    dp = updater.dispatcher
    # back_handler = RegexHandler(pattern='^(' + Keyboards.back + ')$', callback=start, pass_user_data=True)
    # start_handler = CommandHandler('start', start, pass_user_data=True)
    # receipt_success_handler = MessageHandler(Filters.successful_payment, success_receipt_handler, pass_user_data=True)
    #
    # common_handlers = [start_handler, back_handler]
    #
    # conversation_handler = ConversationHandler(
    #     entry_points=[start_handler, receipt_success_handler],
    #
    #     states={
    #
    #     },
    #     fallbacks=[CommandHandler('cancel', cancel)]
    #
    # )

    dp.add_handler(CommandHandler('start', start, pass_user_data=True))
    # dp.add_handler(conversation_handler)
    dp.add_error_handler(error)
    updater.start_polling(poll_interval=2)
    # updater.start_webhook(listen=BotConfig.web_hook_ip, port=BotConfig.web_hook_port, url_path=BotConfig.web_hook_path)
    # updater.bot.set_webhook(url=BotConfig.web_hook_url)
    updater.idle()
