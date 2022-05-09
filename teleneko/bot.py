from .tgapi import basic_bot
from .globe import *
from .tgtypes import *
from .extypes import *
from queue import Queue

__all__ = ['bot']


class bot(basic_bot):
    @with_info(log_info, end="initialized successfully", report_params=True)
    def __init__(self, token, proxy="", name=None, webhook=None):
        super(bot, self).__init__(token, proxy, name)

        self.__message_queue = Queue()
        self.__chat_list = dict()

        # events
        self.update = event(self, name='update')
        self.received_message = event(self, name='received_message')
        self.received_edited_message = event(self, name='received_edited_message')
        self.received_channel_post = event(self, name='received_channel_post')
        self.received_edited_channel_post = event(self, name='received_edited_channel_post')
        self.received_inline_query = event(self, name='received_inline_query')
        self.received_chosen_inline_result = event(self, name='received_chosen_inline_result')
        self.received_callback_query = event(self, name='received_callback_query')
        self.received_shipping_query = event(self, name='received_shipping_query')
        self.received_pre_checkout_query = event(self, name='received_pre_checkout_query')
        self.received_poll = event(self, name='received_poll')
        self.received_poll_answer = event(self, name='received_poll_answer')
        self.received_chat_join_request = event(self, name='received_chat_join_request')
        self.my_chat_member_updated = event(self, name='my_chat_member_updated')
        self.others_chat_member_updated = event(self, name='others_chat_member_updated')

        self.send_message_succeed = event(self, name='send_message_succeed')
        self.initialized = event(self, name='initialized')

        # mainloop hock
        if webhook is None:
            bot_mainloop.tick.hook(self.__fetch_upstream_messages)
        else:
            pass  # fetch from webhook
        bot_mainloop.tick.hook(self.__pick_top_message)

        self.initialized.happen()

    def sendMessage(self, chat_id, text, **argv):
        message = super(bot, self).sendMessage(chat_id, text, **argv)
        self.send_message_succeed.happen(message)
        return message

    def __fetch_upstream_messages(self, loop):
        _offset = 0
        while True:
            updates = self.getUpdates(offset=_offset, limit=100)
            if len(updates) == 0:
                break
            for u in updates:
                self.__message_queue.put(u)
            _offset = updates[-1].update_id + 1

    def __pick_top_message(self, loop):
        if self.__message_queue.empty():
            return
        message = self.__message_queue.get()
        self.update.happen(message)

        content = None

        if hasattr(message, 'message'):
            content = message.message
            self.received_message.happen(content)
        if hasattr(message, 'edited_message'):
            content = message.edited_message
            self.received_edited_message.happen(content)
        if hasattr(message, 'channel_post'):
            content = message.channel_post
            self.received_channel_post.happen(content)
        if hasattr(message, 'edited_channel_post'):
            content = message.edited_channel_post
            self.received_edited_channel_post.happen(content)
        if hasattr(message, 'inline_query'):
            content = message.inline_query
            self.received_inline_query.happen(content)
        if hasattr(message, 'chosen_inline_result'):
            content = message.chosen_inline_result
            self.received_chosen_inline_result.happen(content)
        if hasattr(message, 'callback_query'):
            content = message.callback_query
            self.received_callback_query.happen(content)
        if hasattr(message, 'shipping_query'):
            content = message.shipping_query
            self.received_shipping_query.happen(content)
        if hasattr(message, 'pre_checkout_query'):
            content = message.pre_checkout_query
            self.received_pre_checkout_query.happen(content)
        if hasattr(message, 'poll'):
            content = message.poll
            self.received_poll.happen(content)
        if hasattr(message, 'poll_answer'):
            content = message.poll_answer
            self.received_poll_answer.happen(content)
        if hasattr(message, 'my_chat_member'):
            content = message.my_chat_member
            self.my_chat_member_updated.happen(content)
        if hasattr(message, 'chat_member'):
            content = message.chat_member
            self.others_chat_member_updated.happen(content)
        if hasattr(message, 'chat_join_request'):
            content = message.chat_join_request
            self.received_chat_join_request.happen(content)

        if type(content) is Message:
            pass
        if type(content) is ChatMemberUpdated:
            pass

    def is_reply_me(self, message: Message):
        return MessageFilter.is_reply(self.me)(message)

    def is_mention_me(self, message: Message):
        return MessageFilter.is_mention(self.me)(message)
