

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('3kLTRwGFgnWiMAwXD6yNN2Ocb6XrZI1cXeu62xYpizKBsfSUDck6e4B5IGOJ/m7shrWwJIdonzPeeI31yqHwmLsvhCijVcwn7CiINloa7KwB4gyaGXA5XVZmJEE9Ul4WVNlSDFcCjzPUdi1C6VWb+AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0968039610ab61fd79a28170fa875478')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    str = '你吃飯了嗎?'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=str))


if __name__ == "__main__":
    app.run()