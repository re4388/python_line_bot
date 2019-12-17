from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError
from helper import apple_news, eyny_movie, get_build_result_from_jenkins
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

line_bot_api = LineBotApi(config['line_bot']['Channel_Access_Token'])
# user_id = config['line_bot']['My_User_Id']
profile = line_bot_api.get_profile("U7ee61bf4d1721b77976b3f8ac38b3ff7")

print(profile.display_name)
to = profile.user_id


def run_app(fn):
    content = fn()
    try:
        line_bot_api.push_message(to, TextSendMessage(text=content))
    except LineBotApiError as e:
        raise e


if __name__ == "__main__":
    run_app(get_build_result_from_jenkins)
