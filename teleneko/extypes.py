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
from .bits.typing import *
from .bits import ultility


class MessageFilter:
    @staticmethod
    def is_type_of(
            message_type: single_or_list_of(str)
    ) -> filter_of(Message):
        """"""
        def returned_filter(
                message: Message
        ) -> bool:
            """"""
            return ultility.exist(
                ultility.make_list(message_type),
                lambda x: hasattr(message, x)
            )

        return returned_filter

    @staticmethod
    def contain_command(
            command: single_or_list_of(str)
    ) -> filter_of(Message):
        """"""
        def returned_filter(
                message: Message
        ) -> bool:
            """"""
            contained_command = dict()
            if hasattr(message, 'entities'):
                for e in filter(lambda x: x.type == 'bot_command', message.entities):
                    contained_command[message.text[e.offset:e.offset + e.length]] = True
            else:
                return False

            print( ultility.make_list(command))

            return ultility.exist(
                ultility.make_list(command),
                lambda x: contained_command.get(x) is not None
            )

        return returned_filter

    @staticmethod
    def is_reply(
            user: single_or_list_of(Union[int, User])
    ) -> filter_of(Message):
        """"""
        def returned_filter(
                message: Message
        ) -> bool:
            """"""
            if hasattr(message, 'reply_to_message'):
                pass
            user_copy = ultility.make_list(user)
            pass

        return returned_filter

    @staticmethod
    def is_mention(
            user: single_or_list_of(Union[str, User])
    ) -> filter_of(Message):
        """"""
        def returned_filter(
                message: Message
        ) -> bool:
            """"""
            contained_command = dict()
            if hasattr(message, 'entities'):
                for e in filter(lambda x: x.type == 'mention', message.entities):
                    contained_command[message.text[e.offset:e.offset + e.length]] = True
            else:
                return False

            return ultility.exist(
                map(lambda x: (x.username if isinstance(x, User) else x), ultility.make_list(user)),
                lambda x: contained_command.get(x) is not None
            )

        return returned_filter


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
