## usage
1. edit code
2. push to github
3. since github is connected to Heroku, go to Heroku
4. Manual deploy at Heroku
5. it shall work
   
app.py -> the file go to server, heroku
api.py -> you can run locally to invoke the action

## Note
1. you need to have requirement.txt, Procfile and runtime.exe setting as here
2. go to Heroku to deploy and see log if any debug needed
3. if use negok `ngrok http 5001`

## webhook setting
1. Heroku: 
   https://python-line-bot-20191217.herokuapp.com/callback
2. ngrok
   `ngrok http 5001` and check what thr port forward


## change your webhook
https://developers.line.biz/console/channel/1606909913/messaging-api

## if need to manual deploy to heroku
https://dashboard.heroku.com/apps/python-line-bot-20191217/deploy/github


## Ref
linebot
https://xiaosean.github.io/chatbot/2018-04-10-LineChatbot/

code ref:
https://github.com/twtrubiks/line-bot-tutorial/blob/master/app.py