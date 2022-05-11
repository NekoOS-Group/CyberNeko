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
    'UserFilter',
    'MessageTool'
]

import functools

from .tgtypes import *
from .bits.typing import *
from .bits.strings import *
from .bits import ultility


class BasicFilter:
    @staticmethod
    def by_val(
            accepted_val: Any
    ) -> filter_of(Any):
        inner_set = {val: True for val in ultility.make_list(accepted_val)}
        """"""

        def returned_filter(
                input_val: Any
        ) -> bool:
            """"""
            return inner_set.get(input_val) is not None

        return returned_filter


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

        returned_filter.__name__ = f"MessageFilter.is_type_of({str_val(message_type)})"
        return returned_filter

    @staticmethod
    def contain_command(
            command: single_or_list_of(str)
    ) -> filter_of(Message):
        """"""
        inner_filter = BasicFilter.by_val(command)

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

            return ultility.exist(contained_command, inner_filter)

        returned_filter.__name__ = f"MessageFilter.contain_command({str_val(command)})"
        return returned_filter

    @staticmethod
    def is_reply(
            user: single_or_list_of(Union[int, User])
    ) -> filter_of(Message):
        """"""
        inner_filter = UserFilter.by_username(user)

        def returned_filter(
                message: Message
        ) -> bool:
            """"""
            contained_reply = None
            if hasattr(message, 'reply_to_message'):
                contained_reply = message.reply_to_message.__dict__['from'].username
            else:
                return False

            return inner_filter(contained_reply)

        returned_filter.__name__ = f"MessageFilter.is_reply({str_val(user, True)})"
        return returned_filter

    @staticmethod
    def is_mention(
            user: single_or_list_of(Union[str, User])
    ) -> filter_of(Message):
        """"""
        inner_filter = UserFilter.by_username(user)

        def returned_filter(
                message: Message
        ) -> bool:
            """"""
            contained_mention = []
            if hasattr(message, 'entities'):
                for e in filter(lambda x: x.type == 'mention', message.entities):
                    contained_mention.append(message.text[e.offset + 1:e.offset + e.length])
            else:
                return False

            return ultility.exist(contained_mention, inner_filter)

        returned_filter.__name__ = f"MessageFilter.is_mention({str_val(user, True)})"
        return returned_filter

    @staticmethod
    def is_from(
            user: single_or_list_of(Union[str, User])
    ) -> filter_of(Message):
        """"""
        inner_filter = UserFilter.by_username(user)

        def returned_filter(
                message: Message
        ) -> bool:
            """"""
            if hasattr(message, 'from'):
                return inner_filter(message.__dict__['from'])
            else:
                return False

        returned_filter.__name__ = f"MessageFilter.is_from({str_val(user, True)})"
        return returned_filter


class UserFilter:
    @staticmethod
    def by_username(
            name: single_or_list_of(Union[User, str])
    ) -> filter_of(Union[User, str]):
        """"""
        inner_filter = BasicFilter.by_val(
            [x.username if isinstance(x, User) else x for x in ultility.make_list(name)]
        )

        def returned_filter(
                user: Union[User, str]
        ) -> bool:
            """"""
            return inner_filter(user)

        returned_filter.__name__ = f"UserFilter.by_username({str_val(name, True)})"
        return returned_filter

    @staticmethod
    def by_id(
            user_id: single_or_list_of(Union[User, int])
    ) -> filter_of(Union[User, str]):
        """"""
        inner_filter = BasicFilter.by_val(
            [x.id if isinstance(x, User) else x for x in ultility.make_list(user_id)]
        )

        def returned_filter(
                user: Union[User, str]
        ) -> bool:
            """"""
            return inner_filter(user)

        returned_filter.__name__ = f"UserFilter.by_id({str_val(user_id, True)})"
        return returned_filter


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


class MessageTool:
    @staticmethod
    def get_pure_text(message: Message):
        assert MessageFilter.is_type_of('text')(message)
        text = list(message.text)
        if hasattr(message, 'entities'):
            for e in message.entities:
                for i in range(e.offset, e.offset + e.length):
                    text[i] = ''
        return functools.reduce(lambda x, y: x + y, text)
