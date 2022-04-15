from teleneko.tgapi import basic_bot
# from teleneko.tgtypes import *
from teleneko.globe import *


class bot(basic_bot):
    @with_info(log_info, end="initialized successfully", report_params=True)
    def __init__(self, token, proxy="", name=None):
        super(bot, self).__init__(token, proxy, name)

        self.message_queue = []

        # events
        self.received_message = event(self, name='received_message')
        self.send_message_succeed = event(self, name='send_message_succeed')
        self.initialized = event(self, name='initialized')

        self.initialized.happen()

    def sendMessage(self, chat_id, text, **argv):
        message = super(bot, self).sendMessage(chat_id, text, **argv)
        self.send_message_succeed.happen(message)
        return message
