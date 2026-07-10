from telethon import TelegramClient, events
from telethon.sessions import StringSession
import re

# ========== ڕێکخستنەکان ==========
api_id = 33774652
api_hash = "c438941d8f43a0ff59fcc4b3f3c2fb42"
session = "1ApWapzMBu55FFH32tbL7Qe15_IRzlscaRYhiHz_QGKffwE-uEKyG1tZ4-UiC5djhP8OnwIbPXlxPMM9oAM1ILtMK07BaLyOGkPjwtTU0oEaqsawX3w32enHteG1QjbFzBRoAV5rU-DiJmfqC305ZagiNOA8FAD4_LHMciBXldNTnA_y3mHlo9cpECRpZDrSa5QiSmxJcIKZDpy1luABObuVeiUr-hetJhk402ZmFJ2Iky-yqT_dBwaYberLfdQqTyQQoNWpIrwHt0bXsL6UqJCRgnjUGYb5iqMC5arNfofRvCKFGZwoFXWPHrOpYKnvTnnV1fi23tJ_UqJFIk5JLgZ03Nv3xJ3c="
# ===================================

SOURCE_CHANNEL = "@xforcegroupBOT"   # گروپی سەرچاوە
TARGET_CHANNEL = "@cciraq73"         # گروپی ئامانج

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    msg = event.message
    text = msg.text or ""

    # پشکنینی کارت (تەنها ئەو پەیامانەی کە فۆرماتی کارتیان تێدایە)
    card_pattern = r'(\d{16,19})\|(\d{2})\|(\d{2,4})\|(\d{3,4})'
    if not re.search(card_pattern, text):
        return

    # گۆڕینی ناوەکان بۆ ناوی خۆت
    new_text = text
    new_text = new_text.replace("CC POSTER bot", "Warven Scrapper")
    new_text = new_text.replace("@CCsPoster", "@cciraq73")

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
