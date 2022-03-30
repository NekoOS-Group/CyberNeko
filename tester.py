from tgbot import bot
from sys import argv

token=argv[1]
proxy="localhost:7890"

# proxy is optional
s=bot(token,proxy=proxy)

print(s.getUpdates(limit='z')) 
