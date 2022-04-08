from tgbot import bot_logger, bot_mainloop
from tgbot.globe import bot_namelist, log_info
from tgbot.tgapi import basic_bot
from tgbot.bits.decorators import *
from tgbot.bits.controller import event


class bot(basic_bot):
    @with_info(log_info, end="bot initialized successfully")
    def __init__(self, token, proxy="", name=None):
        super(bot, self).__init__(self, token, proxy, name)
        self.received_message = event()
        self.send_message_succeed = event()

    def sendMessage(self, chat_id, text, **argv):
        message = super(bot, self).sendMessage(chat_id, text, **argv)
        self.send_message_succeed.happen(message)
        return message
