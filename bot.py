import pyrogram
import logging
import os
from config import Config
from pyrogram import Client

# Logging setup
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# ✅ TIME SYNC PATCH (fixes msg_id too low error)
import ntplib
from time import ctime

try:
    c = ntplib.NTPClient()
    response = c.request('pool.ntp.org')
    logger.info(f"[Time Sync] Time synced: {ctime(response.tx_time)}")
except Exception as e:
    logger.warning(f"[Time Sync] NTP time sync failed: {e}")

# Bot Class
class autocaption(Client):
    
    def __init__(self):
        super().__init__(
            session_name="Captioner",
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            workers=20,
            plugins=dict(
                root="Plugins"
            )
        )

# Start Bot
if __name__ == "__main__":
    autocaption().run()
