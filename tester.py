from tgbot import bot
from sys import argv

token=argv[1]
print(token)
proxy="localhost:7890"

# proxy is optional
s=bot(token,proxy)

print(s.getMe()) 
