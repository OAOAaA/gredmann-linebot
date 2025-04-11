from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
from traits.extractor import extract_traits
from traits.matcher import match_pairing
from traits.formatter import format_pairing_output

app = Flask(__name__)
line_bot_api = LineBotApi(os.getenv("kZAI2I7z2ZJBrsuDl1wP93W4ur4ObUo2yeNqIZvv7sSLDQ7XxF6wFddIUZfnfJVcUk/EaLoVJpyq33WgWAfSoTt9DWkS3LZ1lD0M6hVcN7wNA09KGzni4o9mlI7sez3+8PBD2rmCIasm1KZfgMfDuwdB04t89/1O/w1cDnyilFU="))
handler = WebhookHandler(os.getenv("97816f3fbbc069d7f7175f819f1d9d20"))

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers.get('X-Line-Signature')
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except Exception as e:
        print("handle error:", e)
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text.strip()
    if text.startswith("配對："):
        try:
            import re
            pattern = r"配對：(\d{4}/\d{2}/\d{2}) 與 (\d{4}/\d{2}/\d{2})，(\w+)"
            match = re.match(pattern, text)
            if match:
                birth_a, birth_b, relation = match.groups()
                y1, m1, d1 = map(int, birth_a.split("/"))
                y2, m2, d2 = map(int, birth_b.split("/"))
                a_traits = extract_traits(y1, m1, d1)
                b_traits = extract_traits(y2, m2, d2)
                result = match_pairing(a_traits, b_traits, relation)
                text_output = format_pairing_output("A", birth_a, a_traits, "B", birth_b, b_traits, result, relation)
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text_output))
        except Exception as e:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="⚠️ 分析錯誤，請確認輸入格式正確！"))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="請輸入格式：配對：YYYY/MM/DD 與 YYYY/MM/DD，關係類型"))

if __name__ == "__main__":
    app.run()
