from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import time

# ========== ڕێکخستنەکان ==========
api_id = 33774652
api_hash = "c438941d8f43a0ff59fcc4b3f3c2fb42"
session = "1ApWapzMBu8bLXyvUexeoeWtJuBGN17yD0CXU1KZxRmmx_qnTRccKFVcogm7QQmJvAnME5agDdHEsuJH6mOkp1ZJLfK0qr7J9vaKi8au3ha4eylMcfuDyT3dtKYuoOHw-xY4Y5vQirkuaFefSHAlvqhNXXiTixsK22sXKSRCbi5cNFDLq0BXB1IRZvS8D36g7qw52U8joP9dLwpRy_N60_cXA1aisuZhCnzWbpjvyiL39tZ6xxDW0ev_RGw4S8ZIZf-zjmHHAmZJ-GtMwqyI5qIf3vXKspkYnSX17wyRkRLG7lv5xhUHRapIGO3UF0IIW5KJrRaLa3AuebRzndY16SesgFXkkkR8="
# ===================================

SOURCE_CHANNEL = "@xforcegroupBOT"
TARGET_CHANNEL = "@CVC428"
TARGET_ADMIN = "@CC_posterBOT"

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
        # دووبارە دەستپێکردنەوە

# گەر بۆتەکە کەوت، خۆکارانە دووبارە دەستپێدەکاتەوە
while True:
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"❌ Bot crashed: {e}")
        print("🔄 Restarting in 10 seconds...")
        time.sleep(10)
