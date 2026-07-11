from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import os

# ========== ڕێکخستنەکان ==========
API_ID = 33790522
API_HASH = '00e4131295f55452e143c06099c1ddae'
SESSION_STRING = "1ApWapzMBu6FHA0TJuXxK6WEt68lZLodw-AaNiJUDghsVoqZTQu2dvKcfh-tsXst9Dall4nPZSvjrKblvnCo729xM5HpmpxTtSZWQIYWMSkDoeTp64zW4ZCGx-wBEsWle-s7WL80QRkh480AdpKE0o2jBPuevpF-760kMsuJ-4N1IH8rrEMYFL5AeJPo5-8aOLUG-2vjhLmbkTJGH25vXddxzwQtbOzGo51QSDfkZgssamXtwxauNeYl9OtaPjiePgDQ8Cj6YzC28XqNAjUTFSoQjlYlJ3IVUQEOGVJAjSrisI3W0qvl6OaOGRQwnVEABjUlnzwhS_gOdZOvU0JHXRiD146jeUEo="

SOURCE_CHANNEL = "@xforcegroupBOT"   # گروپی سەرچاوە
TARGET_CHANNEL = "@cciraq73"         # گروپی ئامانج
# ===================================

async def main():
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
    await client.start()
    print(f"✅ Bot is running...")
    print(f"📡 Listening to: {SOURCE_CHANNEL}")
    print(f"🎯 Forwarding to: {TARGET_CHANNEL}")

    @client.on(events.NewMessage(chats=SOURCE_CHANNEL))
    async def handler(event):
        msg = event.message
        text = msg.text or ""

        print(f"📩 New message received from: {msg.sender.username if msg.sender else 'Unknown'}")

        try:
            if msg.media:
                data = await msg.download_media(file=bytes)
                await client.send_file(
                    TARGET_CHANNEL,
                    data,
                    caption=text,
                    formatting_entities=msg.entities
                )
                print(f"✅ Media sent to {TARGET_CHANNEL}")
            else:
                await client.send_message(
                    TARGET_CHANNEL,
                    text,
                    formatting_entities=msg.entities
                )
                print(f"✅ Text sent to {TARGET_CHANNEL}")
        except Exception as e:
            print(f"❌ Error sending: {e}")

    try:
        await client.run_until_disconnected()
    except Exception as e:
        print(f"❌ Disconnected: {e}")
        await asyncio.sleep(5)

while True:
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"❌ Bot crashed: {e}")
        await asyncio.sleep(10)
