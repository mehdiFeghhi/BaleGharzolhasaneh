import os


# from local_config import LocalConfig

class BotConfig:
    base_file_url = os.environ.get('BASE_FILE_URL', "https://tapi.bale.ai/file/")
    base_url = os.environ.get('BASE_URL', "https://tapi.bale.ai/")
    bank_card_number = int(os.environ.get('BANK_CARD_NUMBER', ""))
    web_hook_ip = os.getenv('WEB_HOOK_IP', "0.0.0.0")
    web_hook_port = int(os.getenv('WEB_HOOK_PORT', 9696))
    web_hook_domain = os.getenv('WEB_HOOK_DOMAIN', "https://testwebhook.bale.ai")
    web_hook_path = os.getenv('WEB_HOOK_PATH', "/get-upd")
    web_hook_url = "{}{}".format(web_hook_domain, web_hook_path)
    client_token = os.environ.get('CLIENT_TOKEN', "")
