import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from shivu import shivuu, image_urls

LOG_GROUP_ID = -1002059626060
LOGGER_ID = -1002059626060

photo = image_urls

app = shivuu

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"❀ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ #ɴᴇᴡ_ɢʀᴏᴜᴘ ❀\n\n"
               
                f"๏ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠ {message.chat.title}\n"
                f"๏ ɢʀᴏᴜᴘ ɪᴅ ➠ {message.chat.id}\n"
                f"๏ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ➠ @{message.chat.username}\n"
                f"๏ ɢʀᴏᴜᴘ ʟɪɴᴋ ➠[ʙᴀʙʏ ᴛᴏᴜᴄʜ]({link})\n"
                f"๏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ➠ {count}\n"
                f"๏ ᴀᴅᴅᴇᴅ ʙʏ ➠ {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"↻ sᴇᴇ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɢʀᴏᴜᴘ ↻", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"❀ <b><u>ʙᴏᴛ #ʟᴇғᴛ_ɢʀᴏᴜᴘ ʙʏ ᴀ ᴄʜᴜᴛɪʏᴀ</u></b> ❀\n\n๏ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠ {title}\n\n๏ ɢʀᴏᴜᴘ ɪᴅ ➠ {chat_id}\n\n๏ ʙᴏᴛ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ➠ {remove_by}\n\n๏ ʙᴏᴛ ɴᴀᴍᴇ ➠ @Dark_waifu_Bot"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)

#welcome

@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"❀ ʜᴇʏ {message.from_user.mention} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ ❀\n\n"
                
                f"๏ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠ {message.chat.title}\n"
                f"๏ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ➠ @{message.chat.username}\n"
                f"๏ ʏᴏᴜʀ ɪᴅ ➠ {member.id}\n"
                f"๏ ʏᴏᴜʀ ᴜsᴇʀɴᴀᴍᴇ ➠ @{member.username}\n"
                f"๏ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛᴏᴛᴇʟ {count} ᴍᴇᴍʙᴇʀs"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"↻ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ↻", url=f"https://t.me/Dark_waifu_Bot?startgroup=true")]
         ]))

        
