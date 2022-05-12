import teleneko
from teleneko import bot
from teleneko import handle, event_filter
from teleneko import Message, MessageFilter, MessageTool
from teleneko.bits.strings import refresh_decorator
teleneko.set_debug(True)

# proxy, name are optional
sampleNeko = bot(open('mytoken.txt', "r").read().strip(), proxy="http://localhost:7890", name="Neko")


@handle(sampleNeko.received_message)
@event_filter(MessageFilter.contain_command("/python"), MessageFilter.is_from("atCamber", "Telebzy"))
def python(Neko: bot, message: Message):
    try:
        Neko.sendMessage(message.chat.id, refresh_decorator(str(eval(MessageTool.get_pure_text(message)))))
    except:
        Neko.sendMessage(message.chat.id, "猫猫爆炸")


@handle(sampleNeko.received_message)
@event_filter(MessageFilter.contain_command("/exit"), MessageFilter.is_from("atCamber", "Telebzy"))
def python(Neko: bot, message: Message):
    teleneko.terminal()
