class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
OWNER_ID = '6655070772'
sudo_users = ["6655070772", "6090374191", "6655070772", "5297949798", "6655070772", "6655070772"]
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

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
