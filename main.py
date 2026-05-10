import os, asyncio, threading
from flask import Flask
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# --- ضع بياناتك هنا مباشرة بدلاً من النجوم ---
MY_API_ID = 30558508  # ضع رقم الـ API الخاص بك هنا (بدون علامات تنصيص)
MY_API_HASH = '7d3c83c0d2e3e5ecb823eb14cd541595' # ضع الهاش الخاص بك هنا بين علامتي ' '
MY_SESSION = '1BAAOMTQ5LjE1NC4xNjcuOTEAUMSv9Wv0PmMPnkN0AaVKfJ/F92LuxFoUdRKalYMPJCM2zlEzJyXY1wVClkXtRn28B5w0LmN7Xva7/dFvnhH2nYA/2j0KFkzdXPl4arPvtutQrzFQ336WmlGSyV9In/exg9q448UkLtBsrGGJPn/mzt89A+JGOeO9YG9y32uv2A3supw8PrES8/Iy57wmh0Xk+T5eGPD99TVwqf3WxGGKBoEaG9bHfdr4A2nqjquifkQzferJWMYTrHWdvkPgFFEfM3LTiXB4ae/J6PBs5A4E0YlBhAXVHSt1skXcWYUZfxOZ0KvzxqQRDq8i61Dl144EaBegBC/XiATiz2XwwN8jm3c=37.4 °F' # ضع كود الـ 1BAA الطويل هنا بين علامتي ' '
# ------------------------------------------

app = Flask(__name__)
@app.route('/')
def home(): return "Bot is Online"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

async def start_bot():
    print("--- محاولة التشغيل بالبيانات المباشرة ---")
    try:
        client = TelegramClient(StringSession(MY_SESSION), MY_API_ID, MY_API_HASH)
        await client.start()
        print("--- ✅ تم تسجيل الدخول بنجاح! ---")
        await client.send_message('@ClickBeeBot', '/start')
        await client.run_until_disconnected()
    except Exception as e:
        print(f"!!! حدث خطأ: {e}")

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    asyncio.get_event_loop().run_until_complete(start_bot())
