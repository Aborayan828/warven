from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio

API_ID = 33790522
API_HASH = "00e4131295f55452e143c06099c1ddae"
SOURCE = "cciraq73"
TARGET = "xforcegroupBOT"

# ئەگەر ویستت بە Environment Variable بکەیت، ئەمە بەکاربهێنە، ئەگەرنا ڕاستەوخۆ بنووسە
MY_SESSION = "1ApWapzMBu7BaTWOFn9S0rvZIPvBmrs5rvknjLQNql8HIes-hnv6-eS98-LySykCXVBCtF6xVMBPY3FRnNWscQZ8dBs7s5NziCqdmhX-YbxzBR2Ja_fEyXn-AOaJRap9L3qXlVSJjN5-nMW4WIWzsFGm-HOxedvGPLUfRGSbR14WEfKI_DD0icd-gblfPflUVYAWCdvDBl1i9fqgt_gS4jEG6xSJtQvMCPO-mVjCaS__mrGEXTFymsEmNNwuYKhQD6wBG2oUBAP8VUFR2I9s_WIJU6fN9_DVutQX0ZScXxf5xW3Q64g0cLyi2xl7lW0rYDzpz06jkzXI0jyLUX5QNA0MCL12oMTM="

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
    await client.start()
    print("✅ پەیوەندی بە تێلگرامەوە کرا!")
    print(f"🔄 چاوەڕوانی پەیامە نوێکانی گروپی {SOURCE} دەکات...")
    print("⚠️ تەنها پەیامەکانی ئەدمین CC_posterBOT دەنێردرێت!")

    @client.on(events.NewMessage(chats=SOURCE))
    async def copy_new(event):
        # بەدەستهێنانی زانیاری نێرەرەکە (بۆ ئەوەی بزانین کێ ناردوویەتی)
        sender = await event.get_sender()
        
        # پشکنین: ئەگەر نێرەرەکە ناوی بەکارهێنەری "CC_posterBOT" بێت
        if sender and hasattr(sender, 'username') and sender.username == "CC_posterBOT":
            if await copy_message(TARGET, event.message):
                print("✅ پەیامێکی نوێ لە لایەن CC_posterBOT کۆپی کرا و نێردرا بۆ چەناڵەکەت!")
        else:
            # ئەگەر نێرەرەکە کەسێکی تر بێت (ئەدمینی تر یان ئەندام)، پشتگوێ دەخرێت و هیچ نانێردرێت
            pass

    await client.run_until_disconnected()

asyncio.run(main())
