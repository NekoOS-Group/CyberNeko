import teleneko
from teleneko import bot
from teleneko import handle, event_filter
from teleneko import Message

teleneko.set_debug(True)

# proxy, name are optional
sampleNeko = bot(open('mytoken.txt', "r").read().strip(), proxy="http://localhost:7890", name="Neko")


@handle(sampleNeko.received_message)
@event_filter(Message.is_type_of('text'), Message.contain_command('/hello'))
def qwq(Neko: bot, message: Message):
    Neko.sendMessage(message.chat.id, "Hello World")
