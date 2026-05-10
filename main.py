import os
import asyncio
import threading
from flask import Flask
from telethon import TelegramClient, events, functions, types
from telethon.sessions import StringSession

# إعداد Flask لابقاء الخدمة تعمل على Render
app = Flask(__name__)
@app.route('/')
def home(): return "ClickBee Bot is Online!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# جلب البيانات من إعدادات Render
API_ID = int(os.environ.get("30558508"))
API_HASH = os.environ.get("7d3c83c0d2e3e5ecb823eb14cd541595")
SESSION_STR = os.environ.get("1BAAOMTQ5LjE1NC4xNjcuOTEAUMSv9Wv0PmMPnkN0AaVKfJ/F92LuxFoUdRKalYMPJCM2zlEzJyXY1wVClkXtRn28B5w0LmN7Xva7/dFvnhH2nYA/2j0KFkzdXPl4arPvtutQrzFQ336WmlGSyV9In/exg9q448UkLtBsrGGJPn/mzt89A+JGOeO9YG9y32uv2A3supw8PrES8/Iy57wmh0Xk+T5eGPD99TVwqf3WxGGKBoEaG9bHfdr4A2nqjquifkQzferJWMYTrHWdvkPgFFEfM3LTiXB4ae/J6PBs5A4E0YlBhAXVHSt1skXcWYUZfxOZ0KvzxqQRDq8i61Dl144EaBegBC/XiATiz2XwwN8jm3c=37.4 °F")

client = TelegramClient(StringSession(SESSION_STR), API_ID, API_HASH)

CLICKBEE_USER = '@ClickBeeBot'

@client.on(events.NewMessage(chats=CLICKBEE_USER))
async def handler(event):
    message_text = event.message.message
    
    # 1. إذا كان البوت يعرض قناة للانضمام (Join Chats)
    if "Visit the channel" in message_text or "Join the channel" in message_text:
        for row in event.message.reply_markup.rows:
            for button in row.buttons:
                if "Go to channel" in button.text:
                    channel_url = button.url
                    print(f"جاري الانضمام للقناة: {channel_url}")
                    try:
                        await client(functions.channels.JoinChannelRequest(channel=channel_url))
                        print("تم الانضمام! ننتظر 30 ثانية قبل التأكيد...")
                        await asyncio.sleep(30) # الانتظار الذي طلبته
                        
                        # الضغط على زر التأكيد (بعد الانتظار)
                        for r in event.message.reply_markup.rows:
                            for b in r.buttons:
                                if "Confirm" in b.text or "Success" in b.text:
                                    await event.click(text=b.text)
                    except Exception as e:
                        print(f"خطأ في الانضمام: {e}")

    # 2. إذا كان البوت يعرض بوت لبدئه (Message Bots)
    elif "Start the bot" in message_text:
        for row in event.message.reply_markup.rows:
            for button in row.buttons:
                if "Go to bot" in button.text:
                    bot_url = button.url
                    bot_username = bot_url.split('=')[-1] if '=' in bot_url else bot_url.split('/')[-1]
                    print(f"جاري بدء البوت: {bot_username}")
                    try:
                        await client.send_message(bot_username, '/start')
                        print("تم بدء البوت! ننتظر 30 ثانية...")
                        await asyncio.sleep(30)
                        # العودة لتأكيد العملية في ClickBee
                        await event.click(text="Success")
                    except Exception as e:
                        print(f"خطأ في بدء البوت: {e}")

async def run_bot():
    await client.start()
    print("البوت بدأ العمل... جاري فتح القائمة الرئيسية")
    # إرسال أمر البدء لبوت ClickBee للبدء فوراً
    await client.send_message(CLICKBEE_USER, '/start')
    await client.run_until_disconnected()

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_bot())
