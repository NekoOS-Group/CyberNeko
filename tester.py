from tgbot.tgapi import basic_bot

from tgbot import timer
from tgbot import handle

t = timer(0.5)
t.run()


@handle(t.tick)
def qwq(message=None):
    print("awa")


# proxy, name are optional
s = basic_bot(open('mytoken.txt', "r").read().strip(), proxy="localhost:7890", name="Neko")

_id = s.getUpdates(offset=-1)[0].message.message_id + 1

print("begin at %d" % _id)

t.stop()

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
        t.run()
        print("echo messages id: %d" % x.message.message_id)
        _id = x.message.message_id + 1
        try:
            s.sendMessage(x.message.__dict__['from'].id, x.message.text)
        except:
            s.sendMessage(x.message.__dict__['from'].id, "猫猫爆炸!")
        print(x)

exit()
