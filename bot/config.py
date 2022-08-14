#    This file is part of the FileSharing distribution.
#    Copyright (c) 2022 kaif-00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in
# <https://github.com/kaif-00z/FileSharingBot/blob/main/License> .


from decouple import config
from dotenv import load_dotenv

load_dotenv()


class Var:
    STORAGE_CHANNEL = config("STORAGE_CHANNEL", cast=int)
    API_HASH = config("API_HASH", default=None)
    APP_ID = config("APP_ID", cast=int)
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    JOIN_CHAT = config("JOIN_CHAT", default=0, cast=int)
    REDIS_URI = config("REDIS_URI", default=None)
    REDIS_PASS = config("REDIS_PASSWORD", default=None)
    OWNER_ID = config("OWNER_ID", cast=int)
