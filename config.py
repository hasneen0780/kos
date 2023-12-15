import os


class Config(object):
    SessionTelethon = os.environ.get("SessionTelethon", "")

    APP_ID = int(os.environ.get("APP_ID", 21627756))

    API_HASH = os.environ.get("API_HASH", "fe77fbf0cae9f7f5ece37659e2466cf1")
