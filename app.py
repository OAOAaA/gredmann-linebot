from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from modules.parser import parse_pairing_command
from modules.pairing import generate_pairing_analysis

app = Flask(__name__)

line_bot_api = LineBotApi("kZAI2I7z2ZJBrsuDl1wP93W4ur4ObUo2yeNqIZvv7sSLDQ7XxF6wFddIUZfnfJVcUk/EaLoVJpyq33WgWAfSoTt9DWkS3LZ1lD0M6hVcN7wNA09KGzni4o9mlI7sez3+8PBD2rmCIasm1KZfgMfDuwdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("97816f3fbbc069d7f7175f819f1d9d20")

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
        reply = "請使用指令格式：配對：西元(YYYY)/月(MM)/日(DD) 與西元(YYYY)/月(MM)/日(DD)，朋友/同事/戀人"
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))
