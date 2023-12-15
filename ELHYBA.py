from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from datetime import datetime
from telethon.sync import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
import time
import datetime
import time
import requests
see = Config.SessionTelethon
api_id = 16748685
api_hash = 'f0c8f7e4a7a50b5c64fd5243a256fd2f'
with TelegramClient(StringSession(see), api_id, api_hash) as client:
        ui = client.session.save()
        print(ui)
        
@client.on(events.NewMessage)
async def upd_name(event):
    while True:
        iraq_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3)))
        hours = divmod(iraq_time.hour, 12)[1]
        name = f"\r{hours}:{iraq_time.strftime('%M')}"
        time.sleep(1)
        await client(UpdateProfileRequest(first_name=name))
client.start()
client.run_until_disconnected()
