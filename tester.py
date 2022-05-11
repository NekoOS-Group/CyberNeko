import teleneko
from teleneko import bot
from teleneko import handle, event_filter
from teleneko import Message, MessageFilter

teleneko.set_debug(True)

# proxy, name are optional
sampleNeko = bot(open('mytoken.txt', "r").read().strip(), proxy="http://localhost:7890", name="Neko")


@handle(sampleNeko.received_message)
@event_filter(MessageFilter.is_type_of('text'), MessageFilter.contain_command('/hello'))
def qwq(Neko: bot, message: Message):
    Neko.sendMessage(message.chat.id, "Hello World")


@handle(sampleNeko.received_message)
@event_filter(MessageFilter.is_mention(sampleNeko.me))
def qaq(Neko: bot, message: Message):
    Neko.sendMessage(message.chat.id, "咬你哦")


@handle(sampleNeko.received_message)
@event_filter(MessageFilter.is_reply(sampleNeko.me))
def qaq(Neko: bot, message: Message):
    Neko.sendMessage(message.chat.id, "咬你哦")
