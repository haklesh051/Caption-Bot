import logging
import ntplib
import asyncio
import uvloop
from time import ctime
from config import Config
from pyrogram import Client

# Use uvloop for better event loop handling
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# Logging setup
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Time sync logging only (doesn't fix time)
try:
    client = ntplib.NTPClient()
    response = client.request("pool.ntp.org")
    logger.info(f"[Time Sync] Time synced: {ctime(response.tx_time)}")
except Exception as e:
    logger.warning(f"[Time Sync] NTP time sync failed: {e}")

# Pyrogram Bot Class
class autocaption(Client):
    def __init__(self):
        super().__init__(
            session_name="Captioner",
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            workers=20,
            plugins=dict(root="Plugins")
        )

# Async main function
async def main():
    app = autocaption()
    await app.start()
    logger.info("🤖 Bot started successfully. Waiting for events...")
    await app.idle()

# Run bot
if __name__ == "__main__":
    asyncio.run(main())
