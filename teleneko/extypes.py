__all__ = [
    'UpdateFilter',
    'MessageFilter',
    'InlineQueryFilter',
    'ChosenInlineResultFilter',
    'CallbackQueryFilter',
    'ShippingQueryFilter',
    'PreCheckoutQueryFilter',
    'PollFilter',
    'PollAnswerFilter',
    'ChatMemberUpdatedFilter',
    'ChatJoinRequestFilter',
    'ChatFilter',
    'UserFilter'
]

from .tgtypes import *


class MessageFilter:
    @staticmethod
    def is_type_of(message_type):
        def returned_filter(message: Message):
            if type(message_type) is str:
                message_type_copy = [message_type]
            else:
                message_type_copy = message_type

            for item in message_type_copy:
                if hasattr(message, item):
                    return True

            return False

        return returned_filter

    @staticmethod
    def contain_command(command):
        def returned_filter(message: Message):
            contained_command = dict()
            if hasattr(message, 'entities'):
                for e in message.entities:
                    if e.type == 'bot_command':
                        contained_command[message.text[e.offset:e.offset + e.length]] = True
            else:
                return False

            if not (type(command) is list):
                _command = [command]
            else:
                _command = command
            for com in _command:
                if contained_command.get(com) is not None:
                    return True

            return False

        return returned_filter

    @staticmethod
    def is_reply(user: User):
        pass

    @staticmethod
    def is_mention(user: User):
        pass


class UserFilter:
    pass


class ChatFilter:
    pass


class InlineQueryFilter:
    pass


class ChosenInlineResultFilter:
    pass


class CallbackQueryFilter:
    pass


class ShippingQueryFilter:
    pass


class PreCheckoutQueryFilter:
    pass


class PollFilter:
    pass


class PollAnswerFilter:
    pass


class ChatMemberUpdatedFilter:
    pass


class ChatJoinRequestFilter:
    pass


class UpdateFilter:
    pass
