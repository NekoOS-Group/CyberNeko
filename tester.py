import requests
from tgbot import bot
from sys import argv

token=argv[1]
proxy="localhost:7890"

# proxy is optional
s=bot(token,proxy=proxy)

s.proxy="localhost:1234"

print(s.getUpdates(limit=1)) 

