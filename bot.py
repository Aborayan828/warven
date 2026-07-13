from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio

API_ID = 33790522
API_HASH = "00e4131295f55452e143c06099c1ddae"

SOURCE = "xforcegroupBOT"
TARGET = "CVC428"

MY_SESSION = 

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
        print("⚠️ تەنها پەیامەکانی ئەدمین CC_posterBOT دەنێردرێت!")

        @client.on(events.NewMessage(chats=SOURCE))
        async def copy_new(event):
            sender = await event.get_sender()
            if sender and hasattr(sender, 'username') and sender.username == "CC_posterBOT":
                if await copy_message(TARGET, event.message):
                    print(f"✅ پەیامێکی نوێ لە لایەن CC_posterBOT کۆپی کرا و نێردرا بۆ {TARGET}!")
            else:
                pass

        await client.run_until_disconnected()

    except Exception as e:
        print("=" * 40)
        print(f"🚨 هەڵەیەک ڕوویدا! ئەم هەڵەیە ببینە:")
        print(f"❌ هەڵەکە: {e}")
        print(f"💡 چارەسەر: دەبێت هەژمارەکەت لە مۆبایل یان کۆمپیوتەر دەربچیت، یان لە Settings > Devices تێلێگرام ئەم سێشنه ببەستیت، پاشان دووبارە Deploy بکەیت.")
        print("=" * 40)

asyncio.run(main())
