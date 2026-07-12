from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import os
import time
import re

# ========== ڕێکخستنەکان ==========
API_ID = 33790522
API_HASH = '00e4131295f55452e143c06099c1ddae'
# نیو سێشن سترینگ (گۆڕدرا بە دوایین دانە)
SESSION_STRING = "1ApWapzMBu7bJu8xOt_YrlzMVwc_12_ivKqkIPeOF0xwdcPIDLdr8fpuHyPXDktcNedOluZWr9PDS0sPIHpS9drB568AH6wt5ADWDQfKPWTfp_4lrSeDkpZFYQ0V9m7S7Mce9ZEmm5iLOPOOJ_EeRRmx0PYhHFXmQSyNSFMUBjWVsH2ZkauEdXZ-Wl_0AbPQnd34HQzjh9OyahFN_aHa29TkO-9X2OzhoKYGLEu9tPa0TUDDobU1M-wxBjJGOpfPY4jhS9AWEiEzMSXHPVMVX7tUBPiaG6_8UXcaEaELpWcDMLzzDloCWC7Q9oXjr2gzFw_XzhpnxbPjaFYdboljUV3iXRpX-tQM="

SOURCE_CHANNEL = "@xforcegroupBOT"   # گروپی سەرچاوە
TARGET_CHANNEL = "@CVC428"           # گروپی ئامانج
TARGET_ADMIN = "CC_posterBOT"        # تەنها پەیامەکانی ئەم ئەدمینە بگوازەرەوە
# ===================================

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

        if not msg.sender:
            return
        sender_username = msg.sender.username
        if sender_username != TARGET_ADMIN:
            print(f"⏳ Ignored: message from @{sender_username} (not {TARGET_ADMIN})")
            return

        # پشکنینی کارت (١٥ یان ١٦ ژمارە)
        if not re.search(r'\d{15,16}', text):
            print(f"⏳ Ignored: This message does NOT contain a Card.")
            return

        print(f"💳 Card detected from: @{sender_username}")

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
