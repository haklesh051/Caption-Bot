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

# TIME SYNC CHECK
import time
import ntplib

try:
    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    ts = response.tx_time
    time_diff = abs(time.time() - ts)

    if time_diff > 5:
        logger.error(f"⚠️ System time is off by {time_diff:.2f} seconds. Please fix your server time.")
        exit("❌ System time not synced. Exiting.")
except Exception as e:
    logger.warning(f"NTP time sync check failed: {e}")

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
