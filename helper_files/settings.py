import sqlite3 # maintain infractions in infractions.db
import logging # maintain logs in bot.log
import json # to read blacklist

logging.basicConfig(filename = 'bot.log', level = logging.INFO, format='%(asctime)s %(message)s', datefmt = '%Y-%m-%d %H:%M:%S')

BOT_NAME = 'Honest Bear'
BOT_AVATAR = 'https://raw.githubusercontent.com/abhatthal/HonestBear/master/images/HonestBear.png'
DESCRIPTION = 'A very honest discord bot'
COMMAND_PREFIX = '.'

DATABASE = 'honestbear.db'

# Thumbnails
ADMIN_IMG = 'https://raw.githubusercontent.com/abhatthal/HonestBear/master/images/admin.png'
ECONOMY_IMG = 'https://raw.githubusercontent.com/abhatthal/HonestBear/master/images/economy.png'
MEMBER_IMG = 'https://raw.githubusercontent.com/abhatthal/HonestBear/master/images/member.png'
MODERATOR_IMG = 'https://raw.githubusercontent.com/abhatthal/HonestBear/master/images/moderator.png'
MUSIC_IMG = 'https://raw.githubusercontent.com/abhatthal/HonestBear/master/images/music.png'

# Channels
## General
DEBATE_CHANNEL = 606880223199363172
SUGGESTIONS_CHANNEL = 607102047195496456
EMOJI_SUGGESTIONS_CHANNEL = 612899402683514880
## Moderators
LOGGING_CHANNEL = 607056829067034634
## Botting
BOT_SPAM_CHANNEL = 606920734693916674
ECONOMY_CHANNEL = 612898538447306752

# Custom Emojis
ASAMI_EMOJI = '<:Asami:610219714140045376>'

# Blacklist
with open('blacklist.json', 'r') as f:
    BLACKLIST = json.load(f)
    f.close()