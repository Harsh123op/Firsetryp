import logging  
import os
from pyrogram import Client 
from telegram.ext import Application, Updater
import telegram.ext as tg
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

from shivu.config import Development as Config


OWNER_ID = '7058928258'
sudo_users = ["7058928258", "6942703687", "7058928258", "7058928258", "7058928258", "7058928258"]
GROUP_ID = "-1002059626060"
TOKEN = "7392456702:AAEH7VyQQLxjBM1g4uZ4OjZlKXQT-soZyJw"
mongo_url = "mongodb+srv://waifu12:22792279@cluster0.h9gzbqw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
PHOTO_URL = ["https://telegra.ph/file/aa06eb4b312f456e1fd28.jpg", "https://telegra.ph/file/aa06eb4b312f456e1fd28.jpg"]
SUPPORT_CHAT = "DDW_PFP_02"
UPDATE_CHAT = "DDW_PFP_02"
BOT_USERNAME = "gaming_x_world_bot"
CHARA_CHANNEL_ID = "-1002059626060"
api_id = "26208465"
api_hash = "bd4e2fe9c30486282417cdf9a93333b2"

image_urls = [
    "https://telegra.ph/file/405ee89d4a708d161a41b.jpg",
    "https://telegra.ph/file/a80fae6bc9a09d4bc8cb4.jpg",
    "https://telegra.ph/file/002d4caee6e74370848c0.jpg",
    "https://telegra.ph/file/48b536de686bb20e3068b.jpg",
    "https://telegra.ph/file/a986e00083dae9ad32269.jpg",
    "https://telegra.ph/file/ba318dc0749b495b434b3.jpg",
    "https://telegra.ph/file/badce7884ce06e92cedb5.jpg"
]

DESTINATION_DB_URL = "mongodb+srv://waifu12:waifu12@cluster0.z1pajuv.mongodb.net/?retryWrites=true&w=majority"


lol2 = AsyncIOMotorClient(mongo_url)
destination_db = lol2['Character_catcher']
destination_collection = destination_db['user_collection']
destination_char = destination_db['anime_characters']


application = Application.builder().token(TOKEN).build()
shivuu = Client("Shivu", api_id, api_hash, bot_token=TOKEN)
lol = AsyncIOMotorClient(mongo_url)
db = lol['Character_catcher']
user_totals_collection = db['user_totals']
group_user_totals_collection = db['group_user_total']
top_global_groups_collection = db['top_global_groups']
pm_users = db['total_pm_users']

user_collection = destination_collection
collection = destination_char  # Corrected assignment
