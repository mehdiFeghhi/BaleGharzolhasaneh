from telegram import Bot

from main_config import BotConfig


def main():
    bot = Bot(token=BotConfig.client_token,
              base_url=BotConfig.base_url,
              base_file_url=BotConfig.base_file_url)
    updater = Updater(bot=bot)

    dp = updater.dispatcher
    # updater.start_polling(poll_interval=1)
    updater.start_webhook(listen=BotConfig.web_hook_ip, port=BotConfig.web_hook_port, url_path=BotConfig.web_hook_path)
    updater.bot.set_webhook(url=BotConfig.web_hook_url)
    updater.idle()