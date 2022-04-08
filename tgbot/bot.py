from tgbot.globe import *
from tgbot.tgapi import basic_bot
from tgbot.tgtypes import *

from tgbot.bits.decorators import *
from tgbot.globe import event


class bot(basic_bot):
    @with_info(log_info, end="initialized successfully", report_params=True)
    def __init__(self, token, proxy="", name=None):
        super(bot, self).__init__(token, proxy, name)
        self.received_message = event(self, name='received_message')
        self.send_message_succeed = event(self, name='send_message_succeed')

    def sendMessage(self, chat_id, text, **argv):
        message = super(bot, self).sendMessage(chat_id, text, **argv)
        self.send_message_succeed.happen(message)
        return message
