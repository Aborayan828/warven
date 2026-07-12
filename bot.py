from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import os
import time  # زیادکرا بۆ چارەسەری کێشەکە

# ========== ڕێکخستنەکان ==========
API_ID = 33790522
API_HASH = '00e4131295f55452e143c06099c1ddae'
SESSION_STRING = "1ApWapzMBuzkxSBUapE5LFtVBuY3Mc8vp26LwBWezyJhnH3qg8jCp7Q4GfPZTmtBEw0S3Q_4ne_uOc67MiVypdXm7876HU8Z6XUZJzH1NfGEWkPID8pb6VU1n7WnimTFC55r1VpDbUD-lKXMZ0h0xLDOuHulO11QDXdHk02KAIWlOcwLzyrWdG6AR-jCmQzU3_T3_YDXhfoOFJu6Xi8Q7yTLV5dt1HdR4CMVCFS6rBkwUPo4vXxVYQG4wih1dTqkjLgyTxbkmIGpje6o2VnFokDJi0XQFbSsIe3vL55TAJK5JLn-vJasbSN-UYm18ji3DPK2uxLons4K92KHJpHc0qfASDzHdtvQ="

SOURCE_CHANNEL = "@xforcegroupBOT"   # گروپی سەرچاوە
TARGET_CHANNEL = "@cciraq73"         # گروپی ئامانج
TARGET_ADMIN = "CC_posterBOT"        # تەنها پەیامەکانی ئەم ئەدمینە بگوازەرەوە
# ===================================

async def main():
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
    await client.start()
    print(f"✅ Bot is running...")
    print(f"📡 Listening to: {SOURCE_CHANNEL}")
    print(f"🎯 Forwarding messages only from: @{TARGET_ADMIN}")
    print(f"📤 Forwarding to: {TARGET_CHANNEL}")

    @client.on(events.NewMessage(chats=SOURCE_CHANNEL))
    async def handler(event):
        msg = event.message
        text = msg.text or ""

        if not msg.sender:
            return
        sender_username = msg.sender.username
        if sender_username != TARGET_ADMIN:
            print(f"⏳ Ignored: message from @{sender_username} (not {TARGET_ADMIN})")
            return

        print(f"📩 New message from: @{sender_username}")

        try:
            if msg.media:
                # گۆڕانکاری: file=bytes لابرا بۆ ئەوەی بەبێ کێشە کار بکات
                data = await msg.download_media()
                await client.send_file(
                    TARGET_CHANNEL,
                    data,
                    caption=text,
                    formatting_entities=msg.entities
                )
                print(f"✅ Media (copy) sent to {TARGET_CHANNEL}")
            else:
                await client.send_message(
                    TARGET_CHANNEL,
                    text,
                    formatting_entities=msg.entities
                )
                print(f"✅ Text (copy) sent to {TARGET_CHANNEL}")
        except Exception as e:
            print(f"❌ Error sending: {e}")

    try:
        await client.run_until_disconnected()
    except Exception as e:
        print(f"❌ Disconnected: {e}")
        await asyncio.sleep(5)

# گۆڕانکاری لە کۆتاییدا: 'await asyncio.sleep' گۆڕدرا بۆ 'time.sleep' (بەبێ await)
while True:
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"❌ Bot crashed: {e}")
        time.sleep(10)  # تێبینی: time.sleep بەکارهاتووە، نەک await asyncio.sleep
