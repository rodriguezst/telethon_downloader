Telegram Bot on a Telethon client that auto downloads incoming media files.
(cryptg included to speed up downloads)

Running Telethon Downloader
=================
 Pull or build the docker image and launch it with the following environment variables:

 **TG_API_ID** : <telegram API key generated at ´Generating Telegram API keys´>

 **TG_API_HASH** : <telegram API hash generated at ´Generating Telegram API keys´>

 **TG_BOT_TOKEN** : <telegram BOT token generated at ´Creating a Telegram Bot´>

 **TG_DOWNLOAD_PATH** : <download folder inside the docker container where the files will be downloaded (full path)>
 NOTE: THIS FOLDER SHOULD BE MOUNTED AS A VOLUME TO HAVE ACCESS TO THE DOWNLOADED FILES FROM THE HOST OS

Generating Telegram API keys
=================
Before working with Telegram's API, you need to get your own API ID and hash:

1. Follow `this link <https://my.telegram.org/>`_ and login with your
   phone number.

2. Click under API Development tools.

3. A *Create new application* window will appear. Fill in your application
   details. There is no need to enter any *URL*, and only the first two
   fields (*App title* and *Short name*) can currently be changed later.

4. Click on *Create application* at the end. Remember that your
   **API hash is secret** and Telegram won't let you revoke it.
   Don't post it anywhere!

Creating a Telegram Bot
=================
1. Open a conversation with `@BotFather <https://telegram.me/botfather>` in Telegram

2. Use the /newbot command to create a new bot. The BotFather will ask you for a name and username, then generate an authorization token for your new bot.

   The name of your bot is displayed in contact details and elsewhere.

   The Username is a short name, to be used in mentions and telegram.me links. Usernames are 5-32 characters long and are case insensitive, but may only include Latin characters, numbers, and underscores. Your bot's username must end in ‘bot’, e.g. ‘tetris_bot’ or ‘TetrisBot’.

   The token is a string along the lines of 110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw that is required to authorize the bot and send requests to the Bot API. Keep your token secure and store it safely, it can be used by anyone to control your bot.
