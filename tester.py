import requests
from tgbot import bot
from sys import argv
from tgtypes import tgtype
import json

token=argv[1]
proxy="localhost:7890"

# proxy is optional
s=bot(token,proxy=proxy)

#print(s.getMe())

#print(json.dumps(s.__dict__)) 

s = tgtype()

s.x=1
s.y=2
s.z=[tgtype(),tgtype()]
s.z[0].x=1
s.z[0].y=2
s.uuu='www'
s.k=tgtype()
s.k.qwq=dict()
s.k.tat=set()

print(s)
