import os

from pyrogram import filters
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC import app


@app.on_message(filters.command("authtoken") & SUDOERS)
async def list_formats(client, message):
    try:
        await message.reply_text(
            "**Go to Logs and verify to google account then save token data in variable**\n\n**If you dont want to generate new token data then just restart bot otherwise bot will stay offline**"
        )

        os.system(f"yt-dlp --username oauth2 --password '' -F https://www.youtube.com/watch?v=LLF3GMfNEYU")

    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
