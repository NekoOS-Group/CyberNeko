import teleneko.globe
from teleneko import bot
from teleneko import handle

teleneko.set_debug(False)

# proxy, name are optional
sampleNeko = bot(open('mytoken.txt', "r").read().strip(), proxy="http://localhost:7890", name="Neko")


@handle(sampleNeko.received_message)
def qwq(Neko, message: teleneko.Message):
    print(message)
