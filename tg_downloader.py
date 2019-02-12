#!/usr/bin/env python3
import os
import sys
import time

# Import the client
from telethon import TelegramClient

# This is a helper method to access environment variables or
# prompt the user to type them in the terminal if missing.
def get_env(name, message, cast=str):
    if name in os.environ:
        return os.environ[name]
    while True:
        value = input(message)
        try:
            return cast(value)
        except ValueError as e:
            print(e, file=sys.stderr)
            time.sleep(1)

# Define some variables so the code reads easier
session = os.environ.get('TG_SESSION', 'tg_downloader')
api_id = get_env('TG_API_ID', 'Enter your API ID: ', int)
api_hash = get_env('TG_API_HASH', 'Enter your API hash: ')
bot_token = get_env('TG_BOT_TOKEN', 'Enter your Telegram BOT token: ')
download_path = get_env('TG_DOWNLOAD_PATH', 'Enter full path to downloads directory: ')
debug_enabled = ('DEBUG_ENABLED' in os.environ)
user_id = get_env('USER_ID', 'Enter the id of the user to chown downloaded files to: ', int)
group_id = get_env('GROUP_ID', 'Enter the id of the group to chown downloaded files to: ', int)
proxy = None  # https://github.com/Anorov/PySocks

client = TelegramClient(session, api_id, api_hash, proxy=proxy)

# This is our update handler. It is called when a new update arrives.
async def handler(update):
    if(debug_enabled):
        print(update)
    if update.message.media is not None:
        print("Download started at %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())))
        download_result = await client.download_media(update.message, download_path)
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        print("Finished downloading file %s at %s" % (download_result,end_time))
        os.chown(download_result, int(user_id), int(group_id))

try:
    # Start client with TG_BOT_TOKEN string
    client.start(bot_token=str(bot_token))
    # Register the update handler so that it gets called
    client.add_event_handler(handler)

    # Run the client until Ctrl+C is pressed, or the client disconnects
    print('Successfully started (Press Ctrl+C to stop)')
    client.run_until_disconnected()
finally:
    client.disconnect()
    print('Stopped!')

