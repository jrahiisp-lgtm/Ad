import os, asyncio, threading
from flask import Flask
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# --- بياناتك الحقيقية (تأكد من وضعها بدقة) ---
MY_API_ID = 30558508
MY_API_HASH = '7d3c83c0d2e3e5ecb823eb14cd541595' # تأكد من وضع الهاش كاملاً
MY_SESSION = '1BAAOMTQ5LjE1NC4xNjcuOTEAUAaEi07QFQzLNF1MsRvb8YHIzyjy6YQK06ot+kf6bcpCi/3hiFV750lsb5v4RhgOc/qqNUr75mGykKRt6HVYTPmVonds1dNAnHW8GLL4omHH34YIEbBTX+yvkpU4umv2Kk8Gr7ToTShnqYgkIrzvCXg7I7jCRPVtNIaNz99Hs7yNw3z1/d0tnlsWmoW/E1S/u2xmK5jLMDojGJXr39pIhrWuG4FPxGP+dj236NMv6wlEUg8VX+zOFf3eGbt3S5drw5v+a2UCx17ze4NqGYdpxe38eLdE+vNAUuqKOedoDHxjW6fPYQ+HZvw+PYZSGT0YC668aJFG1FccszAd4uRVlD0=' # تأكد من وضع الكود كاملاً
# ------------------------------------------

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Running!"

def run_flask():
    # تشغيل السيرفر على المنفذ المطلوب لـ Railway
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

async def start_telegram_bot():
    print("--- 🚀 محاولة بدء اتصال تليجرام... ---")
    client = TelegramClient(StringSession(MY_SESSION), MY_API_ID, MY_API_HASH)
    
    try:
        await client.start()
        print("--- ✅ تم تسجيل الدخول بنجاح! ---")
        
        # إرسال رسالة لبدء الربح فوراً
        await client.send_message('@ClickBeeBot', '/start')
        print("--- 📩 تم إرسال رسالة البداية لـ ClickBee ---")

        # مراقبة الرسائل الجديدة لتنفيذ المهام
        @client.on(events.NewMessage(chats='@ClickBeeBot'))
        async def handler(event):
            print(f"📩 وصلت رسالة من بوت الربح: {event.raw_text[:20]}...")

        await client.run_until_disconnected()
    except Exception as e:
        print(f"!!! حدث خطأ في تليجرام: {e}")

if __name__ == '__main__':
    # الخطوة السحرية: تشغيل Flask في الخلفية أولاً
    t = threading.Thread(target=run_flask)
    t.daemon = True
    t.start()
    
    # ثم تشغيل تليجرام في المحرك الأساسي
    asyncio.run(start_telegram_bot())
