from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ========== ڕێکخستنەکان ==========
api_id = 33774652
api_hash = "c438941d8f43a0ff59fcc4b3f3c2fb42"
session = session = "1ApWapzMBu0hPg4YXGIf6GL6fgSZ0l9ZSVH48MQUpR7dJuFJSBm767Y71HZkek3MiY1Ib4Id3hZMxfMJdGWAbh0Rtbo3ZAPpMJ83NdinnPtRhckad5aU7hzKqBuAsQQZoJtITGEcBWHqFPtWViBeDjPWirMiGB05kUj6BHeKUGfqRLcYPbGMs-lxp9rjVswU67s0LrdDcp-qa0adD1T1Tc9Bhn44DujwzGtK3JW197hk0j1RTCzyRgrQV0nku4Y0-AWJLnZhnnjqNLXQAiWOphSUl2x6hyqQDOpKQXhJ6_xizfnlklUlAACGAqnsajTQ08zSP40mY61ZHisF5PCg8cjknPFXSQLY="
# ===================================

SOURCE_CHANNEL = "@xforcegroupBOT"   # گروپی سەرچاوە
TARGET_CHANNEL = "@CVC428"           # گروپی ئامانج (گۆڕدرا)
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
    new_text = new_text.replace("@CCsPoster", "@CVC428")

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
