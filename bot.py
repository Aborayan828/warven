from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import os
import time

# ========== ڕێکخستنەکان ==========
API_ID = 33790522
API_HASH = '00e4131295f55452e143c06099c1ddae'
SESSION_STRING = "1ApWapzMBu5DFzHcxacYNypKvKVGapcuFVtBHE_ZcdvSqxGzxZjyBdPjHu_WgVJEZa18cC6C2nPV28J61RKz012E-W5Om896r_szzbXPAg81PkY8OtBGf42e38ayU4HnDScQnedwnnTcO7dEWGEPotkhJlEjLcpGNEDd8uRZA2dpi7jZCJs8Dyqcb5VJyL6T-mBnC7wSiEQcJdICh54yYBkn0kAokC8o2SxXmuuyk-6YAzzyz77RERvgUqyZBqK0czpTYZWG8JLWcDycggWGNrbRNUsazERQyazaBeKowg8tH5WG1v-XnAD6ErfGcPnkGggoXgUEqShG2tanptkKAJ9pJsyvLBRM="

SOURCE_CHANNEL = "@xforcegroupBOT"   # گروپی سەرچاوە
TARGET_CHANNEL = "@CVC428"           # گروپی ئامانج (گۆڕدرا بۆ ناوی تۆ)
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

# گۆڕانکاری لە کۆتاییدا: 'await asyncio.sleep' گۆڕدرا بۆ 'time.sleep'
while True:
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"❌ Bot crashed: {e}")
        time.sleep(10)
