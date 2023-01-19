import os
import time


class Var(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # Get from my.telegram.org
    API_ID = int(os.environ.get("API_ID", 12345))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")


    # To record start time of bot
    BOT_START_TIME = time.time()

    # You Can Get An API Key From https://api.imgbb.com.
    API = os.environ.get("API", None)

    OWNER_ID = int(os.environ.get("OWNER_ID", "853393439"))
    BOT_NAME = os.environ.get("BOT_NAME", "ImgBBRobot")

    START_PIC = "https://i.imgur.com/zYIllxt.jpg"
    HELP_PIC = "https://i.imgur.com/AmxAlix.jpg"


class Tr(object):

    START_TEXT = """
👋 Hi ! {} Selamat Datang di @Foto_ubot

**Dengan Bot Ini Anda Dapat meng-upload Gambar Anda Di web **

Anda Dapat Mengirim Gambar Sebagai Pesan Terusan Dari Obrolan/Saluran Apa Pun Atau Mengunggahnya Sebagai Foto Atau File.
"""

    ABOUT_TEXT = """🤖 **My Name:** [ImgBB](t.me/foto_ubot)

📝 **Language:** [Python 3](https://www.python.org)

📚 **Framework:** [Pyrogram](https://github.com/pyrogram/pyrogram)

👨‍💻 **Developer:** [Amine Soukara](t.me/eueon)


❤ [Donate](t.me/eueon) (euon)
"""

    HELP_TEXT = """💡 Cukup Kirimkan Saya Foto Anda Dan Saya Akan Mengunggahnya Kepada Anda. Itu dia

❤ [Channel](https://t.me/souwon) (Yon)
"""

    ERR_TEXT = "⚠️ API Tidak Ditemukan"

    ERRTOKEN_TEXT = "😶 Token Akses yang Diberikan Kedaluwarsa, Dicabut, Cacat, atau Tidak Valid Karena Alasan Lain. DM @eueon",


    WAIT = "💬 Harap tunggu !!"
