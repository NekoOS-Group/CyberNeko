from tgbot import bot

token="5142944050:AAHmtV0znSTMyPZA92w1XMdhO26jkKTi98Y"
proxy="localhost:7890"

# proxy is optional
s=bot(token,proxy)

print(s.getMe())
