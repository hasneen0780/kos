from config import Config 
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from datetime import datetime
from telethon.sync import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
import time
import datetime
import time
import pytz

import requests
SessionTelethon = Config.SessionTelethon
api_id = 16748685
api_hash = 'f0c8f7e4a7a50b5c64fd5243a256fd2f'
with TelegramClient(StringSession(SessionTelethon), api_id, api_hash) as client:
        ui = client.session.save()
        print(ui)
        
@client.on(events.NewMessage)
async def upd_name(event):
    while True:
        iraq_timezone = pytz.timezone("Asia/Baghdad")
        current_time =datetime.now(tz=iraq_timezone)
        name = current_time.strftime("%H:%M")
        
        time.sleep(1)
        await client(UpdateProfileRequest(first_name=name))
client.start()
client.run_until_disconnected()
