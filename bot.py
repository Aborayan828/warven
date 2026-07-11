from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import time

# ========== ڕێکخستنەکان ==========
api_id = 33774652
api_hash = "c438941d8f43a0ff59fcc4b3f3c2fb42"
session = "1ApWapzMBu4ZtNLp3EZDQrrBRkDtW9sbdz2VmWZc2qzPABGi22sgzNQCjBmjQIxW3096aEsgOy06c4IR37k0NNBH2Vn878Evv0fHDGWOG0KAUvK60ScMsRULv96P3HgQyBFEs1Nn2YeHFTFXZJJAI1z9msxfmbEYmB4CLz976vqfN0_bfRi2yYAIYrCeImLzhYTvORtGO6O_Qn3hirNDeinLkkQsqxw94xCUwgy483Fn8EIxkgyy9qzCq2cBUGrudhLqibUHVg3TbacPfKNgtg57z972qBBotYpa4RaZievxaVfrxgIClOYRogtC64keKnUuna4FR5C03nDDd3RUsTCBMvD5ZuPM="
# ===================================

SOURCE_CHANNEL = "@xforcegroupBOT"   # گروپی سەرچاوە
TARGET_CHANNEL = "@CVC428"           # گروپی ئامانج
TARGET_ADMIN = "@CC_posterBOT"       # ناوی بۆتی تایبەت

async def main():
    client = TelegramClient(StringSession(session), api_id, api_hash)
    await client.start()
    print("✅ Bot is running...")

    @client.on(events.NewMessage(chats=SOURCE_CHANNEL))
    async def handler(event):
        msg = event.message
        text = msg.text or ""

        if not event.message.sender:
            return
        sender_username = event.message.sender.username
        if sender_username != "CC_posterBOT":
            return

        new_text = text
        new_text = new_text.replace("CC POSTER bot", "Warven Scrapper")
        new_text = new_text.replace("@CCsPoster", "@CVC428")

        try:
            if msg.media:
                data = await msg.download_media(file=bytes)
                await client.send_file(
                    TARGET_CHANNEL,
                    data,
                    caption=new_text,
                    formatting_entities=msg.entities
                )
            else:
                await client.send_message(
                    TARGET_CHANNEL,
                    new_text,
                    formatting_entities=msg.entities
                )
        except Exception as e:
            print(f"❌ Error sending: {e}")

    try:
        await client.run_until_disconnected()
    except Exception as e:
        print(f"❌ Disconnected: {e}")
        print("🔄 Reconnecting in 5 seconds...")
        await asyncio.sleep(5)

# گەر بۆتەکە کەوت، خۆکارانە دووبارە دەستپێدەکاتەوە
while True:
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"❌ Bot crashed: {e}")
        print("🔄 Restarting in 10 seconds...")
        time.sleep(10)
