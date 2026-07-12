from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import os
import time  # بۆ چارەسەری کێشەی کۆتایی
import re    # زیادکرا بۆ پشکنینی کارت

# ========== ڕێکخستنەکان ==========
API_ID = 33790522
API_HASH = '00e4131295f55452e143c06099c1ddae'
SESSION_STRING = "1ApWapzMBuzkxSBUapE5LFtVBuY3Mc8vp26LwBWezyJhnH3qg8jCp7Q4GfPZTmtBEw0S3Q_4ne_uOc67MiVypdXm7876HU8Z6XUZJzH1NfGEWkPID8pb6VU1n7WnimTFC55r1VpDbUD-lKXMZ0h0xLDOuHulO11QDXdHk02KAIWlOcwLzyrWdG6AR-jCmQzU3_T3_YDXhfoOFJu6Xi8Q7yTLV5dt1HdR4CMVCFS6rBkwUPo4vXxVYQG4wih1dTqkjLgyTxbkmIGpje6o2VnFokDJi0XQFbSsIe3vL55TAJK5JLn-vJasbSN-UYm18ji3DPK2uxLons4K92KHJpHc0qfASDzHdtvQ="

SOURCE_CHANNEL = "@xforcegroupBOT"   # گروپی سەرچاوە
TARGET_CHANNEL = "@CVC428"           # گروپی ئامانج (گۆڕدرا بۆ ناوی تۆ)
TARGET_ADMIN = "CC_posterBOT"        # تەنها پەیامەکانی ئەم ئەدمینە بگوازەرەوە
# ===================================

async def main():
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
    await client.start()
    print(f"✅ Bot is running...")
    print(f"📡 Listening to: {SOURCE_CHANNEL}")
    print(f"🎯 Only forwarding CARDS from: @{TARGET_ADMIN}")
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

        # ========== پشکنینی کارت ==========
        # ئەگەر ١٥ یان ١٦ ژمارە لە دەقەکەدا نەبوو، پەیامەکە نانێرێت (تەنانەت ئەگەر وێنەش بێت)
        if not re.search(r'\d{15,16}', text):
            print(f"⏳ Ignored: This message does NOT contain a Card.")
            return
        # ==================================

        print(f"💳 Card detected from: @{sender_username}")

        try:
            # ئەم بەشە وێنە و دەقەکە پێکەوە دەنێرێت (ئەگەر کارت بوو)
            if msg.media:
                data = await msg.download_media()
                await client.send_file(
                    TARGET_CHANNEL,
                    data,
                    caption=text,
                    formatting_entities=msg.entities
                )
                print(f"✅ Media + Text sent to {TARGET_CHANNEL}")
            else:
                # ئەگەر کارت بوو بەڵام وێنەی نەبوو، تەنیا دەقەکە دەنێردرێت
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

# چارەسەری کێشەی کۆتایی: بەکارهێنانی time.sleep
while True:
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"❌ Bot crashed: {e}")
        time.sleep(10)
