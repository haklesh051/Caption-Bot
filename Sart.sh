#!/bin/bash

echo "🔄 Syncing time with NTP server..."
apt update && apt install -y ntpdate
ntpdate -u pool.ntp.org

echo "✅ Time synced. Now starting the bot..."
python bot.py
