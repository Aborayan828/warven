from telethon import TelegramClient, events
from telethon.sessions import StringSession
import re

# ========== ڕێکخستنەکان ==========
api_id = 33774652
api_hash = "c438941d8f43a0ff59fcc4b3f3c2fb42"
session = "1ApWapzMBu7tnnTN-VB0X7gG4nlVdgNXk00LgF5kodgSZFDzWCPM0TItPt7ZpF1Uo9TKGaF-Y4Icm48oTRkhcRNSmz2cEkMKoRibSCerOFnsv1W-yRIheuNUCxeSGGQMA1eRfyk0a0VX5ZD4W1FfGOSasFjx_QoVrxx36hEkYWrNe1ktIWausmtwHkE57PvkbYuUYU8VPv1eQYnzg4_mPChXeFfwWXBj3U1OwPeq7QYNGrWCnrRJA61hyuBiUP_VVmag-pCDSMAMHeqE_3eVBKFh9s9dSsUPEpN8XEAe1JAtxkLDs1pGesPepQpsAclBa_y-n8qHulQvw_gfV8l8Q82HXAuNEv5g="
# ===================================

# دوو گروپی سەرچاوە (گۆڕانکاری لەم بەشەدا کراوە)
SOURCE_CHANNELS = ["@xforcegroupBOT", "@SlimeChkGroup"]  
TARGET_CHANNEL = "@cciraq73"

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def handler(event):
    msg = event.message
    text = msg.text or ""

    # پشکنینی کارت
    card_pattern = r'(\d{16,19})\|(\d{2})\|(\d{2,4})\|(\d{3,4})'
    if not re.search(card_pattern, text):
        return

    # گۆڕینی ناوەکان
    new_text = text
    new_text = new_text.replace("@About_Warnisx", "@warven_24")
    new_text = new_text.replace("@Warnisx", "@warven_24")

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

print("Bot is running...")
client.start()
client.run_until_disconnected()
