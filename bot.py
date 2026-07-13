from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio

API_ID = 33790522
API_HASH = "00e4131295f55452e143c06099c1ddae"
SOURCE = "cciraq73"
TARGET = "xforcegroupBOT"

# ===== Sessionە نوێیەکەی تۆ =====
MY_SESSION = "1ApWapzMBu8BWQ3YoC2sKxY4xt3IC4J6CZNejM4OUdDmNTzPyrYsGXOfNmoYmF0-PBYeVVVzXAvHopql-lOR3P-6zQrBu1WVM7Vr-s44_-hSUCmbWqucTVsMHVEVATIJQEjLTBpyD7aT0K7dJWDkCHMWju-7tif8wyVk8pb1CtPkGFQKWd0CRo1ojdBSfiMAbDuQeBBtKWpKyzekGPqjmk8xMV1R4pztJEQ69p4uT8e5GfWKn3trKC5iSttOy7ajWYVNNCKQ3N3GEwIctUPUhFvkcwFlLWDZuNA6FJFFW433UxsK5i_NoBHzrQBFgDynxXU7vKPSDWRFUIg0AQfEs9ttKj5OAVnA=".strip()

client = TelegramClient(StringSession(MY_SESSION), API_ID, API_HASH)

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
    try:
        await client.start()
        print("✅ پەیوەندی بە تێلگرامەوە کرا!")
        print(f"🔄 چاوەڕوانی پەیامە نوێکانی گروپی {SOURCE} دەکات...")
        print("⚠️ تەنها پەیامەکانی ئەدمین CaptainCC_bot دەنێردرێت!")

        @client.on(events.NewMessage(chats=SOURCE))
        async def copy_new(event):
            sender = await event.get_sender()
            if sender and hasattr(sender, 'username') and sender.username == "CaptainCC_bot":
                if await copy_message(TARGET, event.message):
                    print("✅ پەیامێکی نوێ لە لایەن CaptainCC_bot کۆپی کرا و نێردرا!")
            else:
                pass

        await client.run_until_disconnected()

    except Exception as e:
        print("=" * 40)
        print(f"🚨 هەڵەیەک ڕوویدا! ئەم هەڵەیە ببینە:")
        print(f"❌ هەڵەکە: {e}")
        print("=" * 40)

asyncio.run(main())
