from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ========== ڕێکخستنەکان ==========
api_id = 33774652
api_hash = "c438941d8f43a0ff59fcc4b3f3c2fb42"
session = "1ApWapzMBu55FFH32tbL7Qe15_IRzlscaRYhiHz_QGKffwE-uEKyG1tZ4-UiC5djhP8OnwIbPXlxPMM9oAM1ILtMK07BaLyOGkPjwtTU0oEaqsawX3w32enHteG1QjbFzBRoAV5rU-DiJmfqC305ZagiNOA8FAD4_LHMciBXldNTnA_y3mHlo9cpECRpZDrSa5QiSmxJcIKZDpy1luABObuVeiUr-hetJhk402ZmFJ2Iky-yqT_dBwaYberLfdQqTyQQoNWpIrwHt0bXsL6UqJCRgnjUGYb5iqMC5arNfofRvCKFGZwoFXWPHrOpYKnvTnnV1fi23tJ_UqJFIk5JLgZ03Nv3xJ3c="
# ===================================

SOURCE_CHANNEL = "@xforcegroupBOT"   # گروپی سەرچاوە
TARGET_CHANNEL = "@cciraq73"         # گروپی ئامانج
TARGET_ADMIN = "@CC_posterBOT"       # ناوی ئەو بۆتەی کە دەتەوێت پەیامەکانی کۆپی بکەیت

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    msg = event.message
    text = msg.text or ""

    # پشکنین: تەنها پەیامێک کە لەلایەن TARGET_ADMINـەوە نێردراوە
    if not event.message.sender:
        return
    sender_username = event.message.sender.username
    if sender_username != "CC_posterBOT":
        return

    # گۆڕینی ناوەکان (بەپێی خواستی تۆ)
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
