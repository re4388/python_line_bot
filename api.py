from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError
from helper import apple_news, eyny_movie, jenkins


CHANNEL_ACCESS_TOKEN = "s19Xzrw8j71uvdzTbFRxTyWHotTOS8AV+VPNDzMGi6nI/uRRrHO5giqGDQBH7AFUsu81rAilC+anC0tZpHeo/oLc819o8I4JIX6XQniJPHSKo+5cgoJOUl7jTHxviMHWV733BXr9T2Js2YkcnPzbTgdB04t89/1O/w1cDnyilFU="
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
profile = line_bot_api.get_profile('U7ee61bf4d1721b77976b3f8ac38b3ff7')

print(profile.display_name)
to = profile.user_id


try:
    # line_bot_api.push_message(to, TextSendMessage(text='Hello World!'))
    # line_bot_api.push_message(to, TextSendMessage(text=apple_news()))
    # line_bot_api.push_message(to, TextSendMessage(text=eyny_movie()))
    line_bot_api.push_message(to, TextSendMessage(text=jenkins()))
except LineBotApiError as e:
    raise e
