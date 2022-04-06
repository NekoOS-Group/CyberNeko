import requests
from tgbot.tgapi import bot
import json
import logging

logging.basicConfig(level=logging.DEBUG)

token = input()
proxy = "localhost:7890"

# proxy is optional
s = bot(token, proxy=proxy, name="Neko", DEBUG=True)

print(s)

_id = s.getUpdates(offset=-1)[0].message.message_id + 1

print("begin at %d" % _id)

while True:
    x = s.getUpdates(limit=100, offset=_id)
    p = 0
    while p < len(x) and x[p].message.message_id < _id:
        p += 1
    if p >= len(x):
        s.getUpdates(offset=-1)
        continue
    x = x[p]
    if x.message.message_id >= _id:
        print("echo messages id: %d" % x.message.message_id)
        _id = x.message.message_id + 1
        try:
            s.sendMessage(x.message.__dict__['from'].id, x.message.text)
        except:
            s.sendMessage(x.message.__dict__['from'].id, "猫猫爆炸!")
        print(x)

exit()
