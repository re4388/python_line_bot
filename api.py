from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError

CHANNEL_ACCESS_TOKEN = "s19Xzrw8j71uvdzTbFRxTyWHotTOS8AV+VPNDzMGi6nI/uRRrHO5giqGDQBH7AFUsu81rAilC+anC0tZpHeo/oLc819o8I4JIX6XQniJPHSKo+5cgoJOUl7jTHxviMHWV733BXr9T2Js2YkcnPzbTgdB04t89/1O/w1cDnyilFU="
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)



profile = line_bot_api.get_profile('@854kvvdc')

print(profile.display_name)
to = profile.user_id


try:
    line_bot_api.push_message(to, TextSendMessage(text='Hello World!'))
except LineBotApiError as e:
    # error handle
    raise e