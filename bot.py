import logging import ntplib from time import ctime from config import Config from pyrogram import Client import asyncio

Logging setup

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s') logger = logging.getLogger(name) logging.getLogger("pyrogram").setLevel(logging.WARNING)

TIME SYNC LOGGING

try: c = ntplib.NTPClient() response = c.request('pool.ntp.org') logger.info(f"[Time Sync] Time synced: {ctime(response.tx_time)}") except Exception as e: logger.warning(f"[Time Sync] NTP time sync failed: {e}")

Bot Class

class autocaption(Client): def init(self): super().init( session_name="Captioner", bot_token=Config.BOT_TOKEN, api_id=Config.API_ID, api_hash=Config.API_HASH, workers=20, plugins=dict( root="Plugins" ) )

Async main to avoid sync msg_id error

async def main(): app = autocaption() await app.start() logger.info("🤖 Bot started successfully. Waiting for events...") await app.idle()

if name == "main": asyncio.run(main())

