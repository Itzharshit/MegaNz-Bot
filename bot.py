"""
Mega.nz downloader bot
Copyright (C) 2021 @ImJanindu

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# Kang with credits vomro

import os
import logging
from pyrogram import filters, Client, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from mega import Mega
from sample_config import Config

# mega client
mega = Mega()
m = mega.login()

# location
LOCATION = "./"

# logging
bot = Client(
   "MegaNz",
   api_id=Config.API_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.BOT_TOKEN,
)

# start msg
@bot.on_message(filters.command("start") & filters.private)
async def start(_, message):
   user = message.from_user.mention
   return await message.reply_text(f"""𝗛𝗶𝗶 {user},𝗜 𝗮𝗺 𝗠𝗲𝗴𝗮 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿 𝗕𝗼𝘁.

𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝗱 𝗺𝗲 𝗮𝗻𝘆 𝗺𝗲𝗴𝗮.𝗻𝘇 𝗹𝗶𝗻𝗸 𝗜 𝘄𝗶𝗹𝗹 𝗴𝗶𝘃𝗲 𝘆𝗼𝘂 𝗳𝗶𝗹𝗲.""",
   reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("𝗨𝗽𝗱𝗮𝘁𝗲𝘀 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url="https://t.me/pyrogrammers")]]))

# mega download
@bot.on_message(filters.regex(pattern="https://mega.nz/") & filters.private)
async def meganz(_, message):
    input = message.text
    user = message.from_user.mention
    msg = await message.reply_text("📥 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗠𝗲𝗴𝗮 𝗹𝗶𝗻𝗸. 𝗣𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁...")
    try:
        file = m.download_url(input, LOCATION)
    except Exception as e:
        print(str(e))
        return await msg.edit("❌ 𝗢𝗼𝗽𝘀! 𝗬𝗼𝘂𝗿 𝗹𝗶𝗻𝗸 𝗶𝘀 𝗜𝗻𝘃𝗮𝗹𝗶𝗱.")
    await msg.edit("📤 𝗨𝗽𝗹𝗼𝗮𝗱𝗶𝗻𝗴...")
    cap = f"✅ 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 𝗕𝘆 @MegaDLPyBot"
    await bot.send_document(message.chat.id, file, caption=cap)
    await msg.delete()
    os.remove(file)


bot.start()
idle()
