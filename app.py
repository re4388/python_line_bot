from flask import Flask, request, abort
import configparser
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from helper import apple_news, eyny_movie, get_build_result_from_jenkins



app = Flask(__name__)
config = configparser.ConfigParser()
config.read("config.ini")



# line_bot_api = LineBotApi(config['line_bot']['Channel_Access_Token'])
line_bot_api = LineBotApi("s19Xzrw8j71uvdzTbFRxTyWHotTOS8AV+VPNDzMGi6nI/uRRrHO5giqGDQBH7AFUsu81rAilC+anC0tZpHeo/oLc819o8I4JIX6XQniJPHSKo+5cgoJOUl7jTHxviMHWV733BXr9T2Js2YkcnPzbTgdB04t89/1O/w1cDnyilFU=")
# handler = WebhookHandler(config['line_bot']['Channel_Secret'])
handler = WebhookHandler("17fcbf83f049ae1a15b387a978d27ce3")


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



# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(
#                                 event.reply_token,
#                                 TextSendMessage(text=event.message.text)
#                             )


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user id when reply
    user_id = event.source.user_id
    print("user_id =", user_id)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)

    if event.message.text.lower() == "movie":
        content = eyny_movie()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    
    if event.message.text.lower() == "apple":
        content = apple_news()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0

    if event.message.text.lower() == "jenkins":
        content = get_build_result_from_jenkins()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0







if __name__ == "__main__":
    app.run(port=5001)



