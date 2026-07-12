from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import os
import time
import re

# ========== ڕێکخستنەکان ==========
API_ID = 33790522
API_HASH = '00e4131295f55452e143c06099c1ddae'
SESSION_STRING = "1ApWapzMBu3qEsMI8RAZAKdm1od8rJhSMxsqYEBUEEdsQ83GiOtt5Ca-eJxwetya-i2dknbc0xt0mEyOHoM6Oe_n2Ic-0amO3SnrbGeDqyBuT1kZINDVAlx7-rdUkYCNOKvUvOAu8Gy57XvjwUS7py-UEbEyp63h2NNH9myJAjCP9B9ohWJdwPvQGWbwVQws-6e8ChH16hJRBr4BLGcblZgCtTUuMLOmEvGfcCLBdSJwKBbmzt7sNVhW9uIhDG0HeYsraiOhE37p1xFUIZD87Hd4RH9_90BZss8TBKsbLxecP6TRhTXbv7qGzy660945u3D7K8Xt1WdjKSoMchyJF1nc_5UXi-DY="

SOURCE_CHANNEL = "@xforcegroupBOT"
TARGET_CHANNEL = "@CVC428"
TARGET_ADMIN = "CC_posterBOT"
# ===================================

# کۆمەڵەی ناسنامەی پەیامە نێردراوەکان (بۆ ڕێگەگرتن لە دووجاربوون)
sent_message_ids = set()

async def main():
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
    await client.start()
    print(f"✅ Bot is running...")
    print(f"📡 Listening to: {SOURCE_CHANNEL}")
    print(f"🎯 Only forwarding CARDS from: @{TARGET_ADMIN}")
    print(f"📤 Forwarding to: {TARGET_CHANNEL}")

    @client.on(events.NewMessage(chats=SOURCE_CHANNEL))
    async def handler(event):
        msg = event.message
        text = msg.text or ""

        # پشتگوێخستنی ئەگەر بێ نێرەر یان ئەدمینی دیاریکراو نەبێت
        if not msg.sender:
            return
        sender_username = msg.sender.username
        if sender_username != TARGET_ADMIN:
            print(f"⏳ Ignored: message from @{sender_username} (not {TARGET_ADMIN})")
            return

        # پشکنینی بوونی کارت (١٥ یان ١٦ ژمارە)
        if not re.search(r'\d{15,16}', text):
            print(f"⏳ Ignored: This message does NOT contain a Card.")
            return

        # **ڕێگری لە دووجاربوون**
        msg_id = msg.id
        if msg_id in sent_message_ids:
            print(f"⏳ Duplicate message {msg_id} ignored.")
            return
        sent_message_ids.add(msg_id)

        print(f"💳 Card detected from: @{sender_username} (ID: {msg_id})")

        try:
            if msg.media:
                data = await msg.download_media()
                await client.send_file(
                    TARGET_CHANNEL,
                    data,
                    caption=text,
                    formatting_entities=msg.entities
                )
                print(f"✅ Media + Text sent to {TARGET_CHANNEL}")
            else:
                await client.send_message(
                    TARGET_CHANNEL,
                    text,
                    formatting_entities=msg.entities
                )
                print(f"✅ Text sent to {TARGET_CHANNEL}")
        except Exception as e:
            print(f"❌ Error sending: {e}")

    try:
        await client.run_until_disconnected()
    except Exception as e:
        print(f"❌ Disconnected: {e}")
        await asyncio.sleep(5)

# ڕاگرتنی بۆت لە کاتی کەوتن
while True:
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"❌ Bot crashed: {e}")
        time.sleep(10)
