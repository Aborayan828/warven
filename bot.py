from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio

API_ID = 33790522
API_HASH = "00e4131295f55452e143c06099c1ddae"

# ========= چەناڵەکان =========
SOURCE = "xforcegroupBOT"  # چەناڵی سەرچاوە (پەیامەکانی لێ دەخوێنرێتەوە)
TARGET = "CVC428"          # گۆڕانکاری: چەناڵی ئامانج (پەیامەکانی بۆ دەنێردرێت)
# =============================

# ===== Sessionە نوێیەکەی تۆ =====
MY_SESSION = "1ApWapzMBu0wO0rFB4DywcEP_xLNQKmo5h6COQHaZys1Vf7Ve0Vn8YFQD3T8HKsiw_6Q0-zEZ-SPqgXwJrT_VQQytn8BDe6i09MuCjJnv2s1V0LSfMg0OWZTEfZ4vzbJ__xUmLJXr0IRfqtYLRR-LO6gpMJfRg0_eiCGrReea6RA1cFZjqtDtVoT10klMyib3VVv2NNRuBG9-CxbmMVRKRGX0DR02O4ROdQl6CZIdzwo7BYOzMZAOG1pla7gzzZsQpl_8OzNZy8aTiG0--X3aDY-OQmi7jGvZGNsZA30TSAYBeQhpl-qjbLTmOSxZZ8N3vJ8ctCu6maJK_AT_Luv6M8FOi5N45nI=".strip()

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
        print("=" * 40)

asyncio.run(main())
