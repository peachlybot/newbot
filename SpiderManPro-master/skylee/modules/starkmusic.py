import os 
import io
import glob
import asyncio
import pybase64
import html
import random, re
from typing import Optional, List
from requests import get
from skylee import client
from io import BytesIO
from random import randint
import requests
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon import functions, types
import asyncio
from skylee.modules import catmusic
from telethon import events

from telegram import (
    Message,
    Chat,
    MessageEntity,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ParseMode,
    ChatAction,
    TelegramError,
)

from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html
from telegram.error import BadRequest

from skylee import (
    dispatcher,
    OWNER_ID,
    SUDO_USERS,
    SUPPORT_USERS,
    WHITELIST_USERS,
)
from skylee.__main__ import STATS, USER_INFO, GDPR
from skylee.modules.disable import DisableAbleCommandHandler
from skylee.modules.helper_funcs.extraction import extract_user
from skylee.modules.helper_funcs.filters import CustomFilters
from skylee.modules.helper_funcs.alternate import typing_action, send_action
from skylee.modules.stark import catmusic
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

@client.on(events.NewMessage(pattern="^/song( (.*)|$)"))
async def song(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply:
        if reply.message:
            query = reply.messag
    else:
        meme = await event.reply("`Enter A Music Name ! Why Not Try /song Alone` ")
        return
    stark = await event.reply(f"`Searching For {query} in YouTube !`")
    try:
        cat = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        cat = Get(cat)
        await event.client(cat)
    except:
        pass
    await catmusic(str(query),"128k",event)
    l = glob.glob("./temp/*.mp3")
    if l:
        upfall = await event.reply(f"{query} Found! Sending To To Ur Chat 💬!")
        await stark.delete()
    else:
        downfall = await event.reply(f"`Sorry..! Didn't Find Any Query Related To {query}`")
        await stark.delete()
        return
    thumbcat = glob.glob("./temp/*.jpg") + glob.glob("./temp/*.webp") 
    if thumbcat:
        catthumb = thumbcat[0]
    else:
        catthumb = None
    loa = l[0]
    wew = f"➥`{query}` \n➥ **Uploaded By @SpiderMan_ProBot** \n"
    await client.send_file(
                event.chat_id,
                loa,
                force_document=False,
                allow_cache=False,
                caption=wew,
                thumb = catthumb,
                supports_streaming=True,
                reply_to=reply_to_id
            )
    await upfall.delete()
    os.system("rm -rf ./temp/*.mp3") 
    os.system("rm -rf ./temp/*.jpg")
    os.system("rm -rf ./temp/*.webp")
    
    __mod_name__ = "Song"

    __help__ = """
This Module Is To Download Any Music From YouTube
✗ `/song <Song-name>`"""

    SONG_HANDLER = DisableAbleCommandHandler("song", song)
    dispatcher.add_handler(SONG_HANDLER)
