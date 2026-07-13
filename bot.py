from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import os

API_ID = 33790522
API_HASH = "00e4131295f55452e143c06099c1ddae"
SOURCE = "cciraq73"          # گۆڕدرا بۆ cciraq73
TARGET = "xforcegroupBOT"    # گۆڕدرا بۆ xforcegroupBOT (بەبێ @)

client = TelegramClient(StringSession(os.getenv('SESSION_STRING')), API_ID, API_HASH)

async def copy_message(target, msg):
    try:
        if msg.text and not msg.media:
            await client.send_message(target, msg.text)
        elif msg.media:
            await client.send_file(target, msg.media, caption=msg.text or "")
        else:
            return False
        return True
    except Exception as e:
        print(f"❌ هەڵە لە کۆپیکردن: {e}")
        return False

async def main():
    await client.start()
    print("✅ پەیوەندی بە تێلگرامەوە کرا!")
    print(f"🔄 چاوەڕوانی پەیامە نوێکانی گروپی {SOURCE} دەکات...")

    @client.on(events.NewMessage(chats=SOURCE))
    async def copy_new(event):
        if await copy_message(TARGET, event.message):
            print(f"✅ پەیامێکی نوێ کۆپی کرا و نێردرا بۆ {TARGET}!")

    await client.run_until_disconnected()

asyncio.run(main())
