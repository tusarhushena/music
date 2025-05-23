# Powered By Team DeadlineTech

import asyncio
from datetime import datetime, timedelta

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

import config
from DeadlineTech import app
from DeadlineTech.core.call import Anony, autoend
from DeadlineTech.utils.database import get_client, is_active_chat, is_autoend
from DeadlineTech.misc import SUDOERS

# Runtime Toggles
AUTO_END_ENABLED = True
AUTO_LEAVE_ENABLED = True


def seconds_until_4am(now):
    target = now.replace(hour=4, minute=0, second=0, microsecond=0)
    if now >= target:
        target += timedelta(days=1)
    return (target - now).total_seconds()


# Command to toggle auto_end
@app.on_message(filters.command("auto_end") & SUDOERS)
async def toggle_auto_end(_, message: Message):
    global AUTO_END_ENABLED
    AUTO_END_ENABLED = not AUTO_END_ENABLED
    state = "enabled" if AUTO_END_ENABLED else "disabled"
    await message.reply_text(f"✅ Auto End has been <b>{state}</b>.")


# Command to toggle auto_leave
@app.on_message(filters.command("auto_leave") & SUDOERS)
async def toggle_auto_leave(_, message: Message):
    global AUTO_LEAVE_ENABLED
    AUTO_LEAVE_ENABLED = not AUTO_LEAVE_ENABLED
    state = "enabled" if AUTO_LEAVE_ENABLED else "disabled"
    await message.reply_text(f"✅ Auto Leave has been <b>{state}</b>.")


# Auto Leave Assistant at 4 AM Daily
async def scheduled_auto_leave():
    while True:
        await asyncio.sleep(seconds_until_4am(datetime.now()))
        if not AUTO_LEAVE_ENABLED:
            continue

        from AnonXMusic.core.userbot import assistants

        for num in assistants:
            client = await get_client(num)
            left = 0
            try:
                async for i in client.get_dialogs():
                    if i.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP, ChatType.CHANNEL]:
                        if i.chat.id not in [config.LOGGER_ID, -1001686672798, -1001549206010]:
                            if left >= 20:
                                break
                            if not await is_active_chat(i.chat.id):
                                try:
                                    await client.leave_chat(i.chat.id)
                                    left += 1
                                except:
                                    continue
            except:
                continue


# Auto End Handler
async def auto_end():
    while True:
        await asyncio.sleep(20)
        if not AUTO_END_ENABLED or not await is_autoend():
            continue

        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue
            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue
                autoend[chat_id] = {}
                try:
                    await Anony.stop_stream(chat_id)
                except:
                    continue
                try:
                    await app.send_message(
                        chat_id,
                        "» ʙᴏᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴇғᴛ ᴠɪᴅᴇᴏᴄʜᴀᴛ ʙᴇᴄᴀᴜsᴇ ɴᴏ ᴏɴᴇ ᴡᴀs ʟɪsᴛᴇɴɪɴɢ.",
                    )
                except:
                    continue


# Start Tasks
asyncio.create_task(scheduled_auto_leave())
asyncio.create_task(auto_end())
