import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "25892174"
API_HASH = "f57b0158a1b29c2c6032157a227aea4e"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7852409818:AAFL1Ebto4hOhi9qqid4A-DLUp4tZddLRh8"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://fidixi3663:w7rvlxmDd5lsX9ix@cluster0.0k1an50.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 6000))

# Chat id of a group for logging bot's activities
LOGGER_ID = -1002402719066

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = 5960968099

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/koreansmu/billamusic2.0",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = "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"  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/STORM_TECHH")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/STORM_CORE")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2d3fd5ccdd3d43dda6f17864d8eb7281")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "48d311d8910a4531ae81205e1f754d27")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "BQGLFU4APj5JxF0yUMUv0W_t0p-2g8ntQcqN9q0rHFgbMOUKIMdxk6I8Q9HodyMqAQ0y5VUU3m7PvndnxN1B0ZQU2g9emV7gRn2MWqCvfztXVS7wEGUIM9buAO2GCE2k9hR6sKHTtCNzbZ56-xqBIQpqI0coZx6v_GMGfdi-0yH-vLRC-7_fwhjaGwZwoC1LPPpoFLx1ZyzokG7Cowd6x0AsdWh1e7ayyS1nSR01Iz0e3mS7hCrw8lLzE6pHGwyuK4iz2RECM34e-TqqWksaePWjZsH8t7VBk_pIujC3UgcwpatE0QHdNqJh2_1IJrYkYQWlcs2IlMMJdD1BNuX7ecf4i7nZywAAAAHNzl_uAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/0799b110240ef68c1519b-46d4e55cf4b3b1b908.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/7863333287f805047b707-1db27700cfe5bb71d3.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/850b97892571970594dc0-b005845a1d9c0f175a.jpg"
STATS_IMG_URL = "https://graph.org/file/999be18d2ae22977571f3-f93222d713f41b0146.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/002dc32a43f463fbfed8e-e04d6df2456227531b.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/f4e010d4a88b63d1f6258-dac28211d4296ff886.jpg"
STREAM_IMG_URL = "https://graph.org/file/d6d0d0b2328e9916de696-b5fb5dd3091cbab13e.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
