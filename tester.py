from teleneko import bot

# proxy, name are optional
s = bot(open('mytoken.txt', "r").read().strip(), proxy="http://localhost:7890", name="Neko")

_id = s.getUpdates(offset=-1)[0].message.message_id + 1


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
