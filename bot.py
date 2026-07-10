from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ========== ڕێکخستنەکان ==========
api_id = 33774652
api_hash = "c438941d8f43a0ff59fcc4b3f3c2fb42"
session = "1ApWapzMBu55FFH32tbL7Qe15_IRzlscaRYhiHz_QGKffwE-uEKyG1tZ4-UiC5djhP8OnwIbPXlxPMM9oAM1ILtMK07BaLyOGkPjwtTU0oEaqsawX3w32enHteG1QjbFzBRoAV5rU-DiJmfqC305ZagiNOA8FAD4_LHMciBXldNTnA_y3mHlo9cpECRpZDrSa5QiSmxJcIKZDpy1luABObuVeiUr-hetJhk402ZmFJ2Iky-yqT_dBwaYberLfdQqTyQQoNWpIrwHt0bXsL6UqJCRgnjUGYb5iqMC5arNfofRvCKFGZwoFXWPHrOpYKnvTnnV1fi23tJ_UqJFIk5JLgZ03Nv3xJ3c="
# ===================================

SOURCE_CHANNELS = ["@SlimeChkGroup"]   # گروپی سەرچاوە
TARGET_CHANNEL = "@cciraq73"           # گروپی تۆ

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def handler(event):
    msg = event.message
    text = msg.text or ""

    # **پشکنین: تەنها پەیامەکانی "Result" یان "APPROVED/DECLINED"**
    if "Result" not in text and "APPROVED" not in text and "DECLINED" not in text:
        return  # پشتگوێ بخرێت

    # گۆڕینی ناوەکان (ئەگەر پێویست بوو)
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
