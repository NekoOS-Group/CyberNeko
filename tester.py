import teleneko.globe
from teleneko import bot
from teleneko import handle

# proxy, name are optional
sampleNeko = bot(open('mytoken.txt', "r").read().strip(), proxy="http://localhost:7890", name="Neko")

teleneko.globe.bot_debug = False


@handle(sampleNeko.received_message)
def qwq(Neko, message: teleneko.Message):
    print(message)
