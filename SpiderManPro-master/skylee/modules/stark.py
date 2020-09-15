# @MusicModule
import os
import re
import time
import shlex
import asyncio
import requests 
import subprocess
from PIL import Image
from asyncio import sleep
from selenium import webdriver
from random import choice
from telethon import events
from os.path import basename
from bs4 import BeautifulSoup
from validators.url import url
from selenium import webdriver
from emoji import get_emoji_regexp
from telethon.tl.types import Channel
from typing import Tuple, List, Optional

async def catmusic(cat , QUALITY,event):
    search = cat
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.binary_location = '/app/.apt/usr/bin/google-chrome'
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.youtube.com/results?search_query='+search)
    user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
    for i in user_data:
        video_link = i.get_attribute('href')
        break
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not video_link:
        await event.reply(f"Sorry. I can't find that song `{search}`")
        return
    try:
        command = ('youtube-dl -o "./temp/%(title)s.%(ext)s" --extract-audio --audio-format mp3 --audio-quality ' + QUALITY + ' ' + video_link)
        os.system(command)
    except Exception as e:
        return await event.reply(f"`Error:\n {e}`") 
    try:
        thumb = ('youtube-dl -o "./temp/%(title)s.%(ext)s" --write-thumbnail --skip-download ' + video_link)
        os.system(thumb)
    except Exception as e:
        return await event.reply(f"`Error:\n {e}`")
