import teleneko.globe
from teleneko import bot
from teleneko import handle, event_filter

teleneko.set_debug(True)

# proxy, name are optional
sampleNeko = bot(open('mytoken.txt', "r").read().strip(), proxy="http://localhost:7890", name="Neko")


@handle(sampleNeko.received_message)
@event_filter(teleneko.Message.type_filter('text'))
def qwq(Neko, message: teleneko.Message):
    print(message)
