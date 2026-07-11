from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ========== ڕێکخستنەکان ==========
api_id = 33774652
api_hash = "c438941d8f43a0ff59fcc4b3f3c2fb42"
session = "1ApWapzMBuz9KAAbVRLRzD6z7UujEu-bAOqcYCNgL_nfsG-FbXTnrL_-61YzdgcRhlUDduYA-P57mQcokdZGa2kA6qTbt0jKKb3-smWNzS5xk2bGrJ-C2d_QRoQqHPwzaj4I1mi4QV_4aNdmRIX7fCEL0AZotn_PZNmf-uHcSxRpLU3xuNICr1T59bl_M6vOzcyS_dayFznUKnI0oQVhEX8ICva1s98_uaSzXiA76ccNZCudbK1gO-ONKkXD0XYy5m0xTsZDJcZS6Cl35Yte-WDDgA2vovpcFKcK_soX2thFWdVlKL0yHxJVd0b3O062xA-92bNxI5uakXa64rdQ5Udgzge2gBKA="
# ===================================

SOURCE_CHANNEL = "@xforcegroupBOT"   # گروپی سەرچاوە
TARGET_CHANNEL = "@CVC428"           # گروپی ئامانج
TARGET_ADMIN = "@CC_posterBOT"       # ناوی بۆتی تایبەت

client = TelegramClient(StringSession(session), api_id, api_hash)

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
