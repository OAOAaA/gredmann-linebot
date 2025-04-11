from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from modules.parser import parse_pairing_command
from modules.pairing import generate_pairing_analysis

app = Flask(__name__)

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text.strip()
    if text.startswith("配對："):
        try:
            person1, person2, relation = parse_pairing_command(text)
            reply = generate_pairing_analysis(person1, person2, relation)
        except Exception as e:
            reply = f"⚠️ 錯誤：{str(e)}"
    else:
        reply = "請使用指令格式：配對：1990/01/01 與 1995/05/05，朋友"
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))
