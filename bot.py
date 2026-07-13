from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio

API_ID = 33790522
API_HASH = "00e4131295f55452e143c06099c1ddae"

# ========= چەناڵەکان =========
SOURCE = "xforcegroupBOT"  # چەناڵی سەرچاوە (پەیامەکانی لێ دەخوێنرێتەوە)
TARGET = "cciraq73"        # چەناڵی ئامانج (پەیامەکانی بۆ دەنێردرێت)
# =============================

# ===== Sessionە نوێیەکەی تۆ =====
MY_SESSION = "1ApWapzMBu6QGF4svhlJDFY_AemJyFVFfRoFIQUu-EeHJx9pU_9FbzBiN59WmouNp3g0EsKaweex9bB7KOgPIbV6axG3BlQwjWL7U62VmIyby2BRp1zFbu9h8wUj7M4czuGJbycmNsvxsML9miCjCKa5piO3cfDpvUwxqmFjKbF_L8VTYA5872fW_ZT8JmyTvg4g6s2OqanfbL0kY14_i7cdyv2_zEtVOL3WTFbU1dE1IdKr1Gxy7piHDu6-CgqMz6whU0XBh1pF6tLNfH9Orl5z3bcXhCRCUQPloHO0ZNq9Iu4Kp0MfTFSJe9OPh3ESF4h8ntbz-NizdkxSbaAU00OZ8S550xFA=".strip()

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
                    print(f"✅ پەیامێکی نوێ لە لایەن CaptainCC_bot کۆپی کرا و نێردرا بۆ {TARGET}!")
            else:
                pass

        await client.run_until_disconnected()

    except Exception as e:
        print("=" * 40)
        print(f"🚨 هەڵەیەک ڕوویدا! ئەم هەڵەیە ببینە:")
        print(f"❌ هەڵەکە: {e}")
        print("=" * 40)

asyncio.run(main())
