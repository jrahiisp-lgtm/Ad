import os, asyncio, threading
from flask import Flask
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# --- ضع بياناتك هنا مباشرة بدلاً من النجوم ---
MY_API_ID = 30558508  # ضع رقم الـ API الخاص بك هنا (بدون علامات تنصيص)
MY_API_HASH = '7d3c83c0d2e3e5ecb823eb14cd541595' # ضع الهاش الخاص بك هنا بين علامتي ' '
MY_SESSION = '1BAAOMTQ5LjE1NC4xNjcuOTEAUAaEi07QFQzLNF1MsRvb8YHIzyjy6YQK06ot+kf6bcpCi/3hiFV750lsb5v4RhgOc/qqNUr75mGykKRt6HVYTPmVonds1dNAnHW8GLL4omHH34YIEbBTX+yvkpU4umv2Kk8Gr7ToTShnqYgkIrzvCXg7I7jCRPVtNIaNz99Hs7yNw3z1/d0tnlsWmoW/E1S/u2xmK5jLMDojGJXr39pIhrWuG4FPxGP+dj236NMv6wlEUg8VX+zOFf3eGbt3S5drw5v+a2UCx17ze4NqGYdpxe38eLdE+vNAUuqKOedoDHxjW6fPYQ+HZvw+PYZSGT0YC668aJFG1FccszAd4uRVlD0='
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
