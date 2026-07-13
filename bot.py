from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio

API_ID = 33790522
API_HASH = "00e4131295f55452e143c06099c1ddae"
SOURCE = "cciraq73"
TARGET = "xforcegroupBOT"

# ===== Sessionە نوێیەکەی تۆ ===== 
# .strip() زیاد کردووە بۆ ئەوەی ئەگەر بۆشایی یان خاڵی نوێ لەگەڵدا کۆپی بوو، پاکی بکاتەوە
MY_SESSION = "1ApWapzMBu13SPdFAyIdjFpONStk3c8wBexVdMYzRA8Bw9CWy5qZdRN-FV4rMBSxRMUd2hgIAZ7fszb9D7wMNiOgTXKz5Flw8aGzvGnHKgrbiq9FmMN16bm3OE-LWBjFs62dnZaGptSE6ymMrT-SI3nuixPU6D6TZhFPl-1bVvKUkyINZqrvnwCy_r2dOWRiI7fMBjL3-Zh914VllV5kNRII7QwLh7Dw4bPnNjuodwXKbG0SRuK754f2PsKmS3jCPClD0vMgd9kMTlkjhH9DOccTCqt3Ym0poSDFq2L_D19pzKoMyY6PpEhhbD9kI77rD-IgpFe42596jK39ByOvDgxVOIDwKC8E=".strip()

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
                    print("✅ پەیامێکی نوێ لە لایەن CC_posterBOT کۆپی کرا و نێردرا!")

        await client.run_until_disconnected()

    except Exception as e:
        print("=" * 40)
        print(f"🚨 هەڵەیەک ڕوویدا! ئەم هەڵەیە ببینە:")
        print(f"❌ هەڵەکە: {e}")
        print("=" * 40)

asyncio.run(main())
