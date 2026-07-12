from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import time

# ========== ڕێکخستنەکان ==========
API_ID = 33790522
API_HASH = '00e4131295f55452e143c06099c1ddae'
SESSION_STRING = "1ApWapzMBu6FHA0TJuXxK6WEt68lZLodw-AaNiJUDghsVoqZTQu2dvKcfh-tsXst9Dall4nPZSvjrKblvnCo729xM5HpmpxTtSZWQIYWMSkDoeTp64zW4ZCGx-wBEsWle-s7WL80QRkh480AdpKE0o2jBPuevpF-760kMsuJ-4N1IH8rrEMYFL5AeJPo5-8aOLUG-2vjhLmbkTJGH25vXddxzwQtbOzGo51QSDfkZgssamXtwxauNeYl9OtaPjiePgDQ8Cj6YzC28XqNAjUTFSoQjlYlJ3IVUQEOGVJAjSrisI3W0qvl6OaOGRQwnVEABjUlnzwhS_gOdZOvU0JHXRiD146jeUEo="

SOURCE_CHANNEL = "@xforcegroupBOT"   # چەناڵی سەرچاوە (ئەم بۆتە لێرەوە دەخوێنێت)
TARGET_CHANNEL = "@cciraq73"         # گروپی ئامانج (پەیامەکان دەنێردرێت بۆ ئێرە)
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
        sender = await msg.get_sender()
        
        # ========== پشکنینی ناوی بەکارهێنەر ==========
        # ئەگەر نێردراو نەناسراو بوو یان ناوی بەکارهێنەرەکەی "CC_posterBOT" نەبوو، پەیامەکە ڕەت بکەرەوە
        if not sender or sender.username != "CC_posterBOT":
            return
        # ==========================================

        text = msg.text or ""
        print(f"📩 New message received from target BOT: {sender.username}")

        try:
            if msg.media:
                data = await msg.download_media()
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

# چارەسەری کێشەی پێشوو
while True:
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"❌ Bot crashed: {e}")
        time.sleep(10)
