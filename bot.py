from telethon import TelegramClient, events
import asyncio

# ============ زانیارییەکانی تۆ ============
API_ID = 33790522
API_HASH = "00e4131295f55452e143c06099c1ddae"

# ============ ناوی گروپ و چەناڵ ============
SOURCE = "CCsPoster"          # ناوی گروپی سەرچاوە
TARGET = "@CVC428"            # ناوی چەناڵەکەی خۆت (بە @)

client = TelegramClient('my_session', API_ID, API_HASH)

async def copy_message(target, msg):
    """پەیامێک کۆپی دەکات و وەک پەیامی نوێ دەینێرێت (نەک فۆروارد)"""
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
    print("🔄 چاوەڕوانی پەیامە نوێکانی گروپی CCsPoster دەکات... (هیچ پەیامێکی کۆن کۆپی ناکرێت)")

    @client.on(events.NewMessage(chats=SOURCE))
    async def copy_new(event):
        if await copy_message(TARGET, event.message):
            print("✅ پەیامێکی نوێ کۆپی کرا و نێردرا بۆ چەناڵەکەت!")

    await client.run_until_disconnected()

asyncio.run(main())
