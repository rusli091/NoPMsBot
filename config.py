import os

# ----------- REQUIRED ----------- #

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "")
DATABASE_URL = os.environ.get("DATABASE_URL", "")

# ----------- OPTIONAL ----------- #

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", 4))
COMMAND_PREFIX = os.environ.get("COMMM_AND_PRE_FIX", "/")
BAN_COMMAND = os.environ.get("BAN_COMMAND", "ban")
UNBAN_COMMAND = os.environ.get("UN_BAN_COMMAND", "unban")
START_COMMAND = os.environ.get("START_COMMAND", "start")
START_OTHER_USERS_TEXT = os.environ.get("START_OTHER_USERS_TEXT", "Saya adalah Bot PM, bukan grup. Silakan mulai saya secara pribadi.")
ONLINE_CHECK_START_TEXT = os.environ.get("ONLINE_CHECK_START_TEXT", "Bot Berhasil Di Aktifkan!")
DERP_USERS_TEXT = os.environ.get("DERP_USER_S_TEXT", "Pengguna ini telah diblokir")
IS_BLACKLISTED_MESSAGE_TEXT = os.environ.get("IS_BLACK_LIST_ED_MESSAGE_TEXT", "Anda telah di-blacklist karena: {reason}")
REASON_DELIMITER = os.environ.get("REASON_DE_LIMIT_ER", " | ")
IS_UNBANNED_MESSAGE_TEXT = os.environ.get("IS_UN_BANED_MESSAGE_TEXT", "Anda telah di-unbanned. Sekarang Anda dapat mengirimi saya pesan.")
BOT_WAS_BLOCKED_BY_USER = os.environ.get("BOT_WS_BLOCKED_BY_USER", "Bot diblokir oleh pengguna")
LOG_FILE = os.environ.get("LOG_FILE_ZZGEVC", "bot.log")
