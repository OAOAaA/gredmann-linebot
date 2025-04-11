from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from modules.parser import parse_pairing_command
from traits.extractor import extract_traits
from traits.matcher import match_pairing
from traits.formatter import format_pairing_output

# 直接寫入 Token 與 Secret（測試用，不建議實際部署時使用）
line_bot_api = LineBotApi("kZAI2I7z2ZJBrsuDl1wP93W4ur4ObUo2yeNqIZvv7sSLDQ7XxF6wFddIUZfnfJVcUk/EaLoVJpyq33WgWAfSoTt9DWkS3LZ1lD0M6hVcN7wNA09KGzni4o9mlI7sez3+8PBD2rmCIasm1KZfgMfDuwdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("97816f3fbbc069d7f7175f819f1d9d20")

app = Flask(__name__)

@app.route("/")
def home():
    return "LINE Bot Webhook is running."

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text.strip()

    if text.startswith("配對："):
        try:
            a_birth, b_birth, relation = parse_pairing_command(text)
            a_traits = extract_traits(a_birth)
            b_traits = extract_traits(b_birth)
            result = match_pairing(a_traits, b_traits, relation)
            reply_text = format_pairing_output(result, relation)
        except Exception as e:
            reply_text = f"⚠️ 分析時發生錯誤：{str(e)}"
    else:
        reply_text = "🌌 請輸入格式：配對：YYYY/MM/DD 與 YYYY/MM/DD，關係類型"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )
