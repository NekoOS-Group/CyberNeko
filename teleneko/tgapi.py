from .tgtypes import *
from .globe import *

__all__ = ['basic_bot']


def _log_api(message, *args):
    if len(args) > 2:
        params = ", ".join([f"{k}={v!r}" for k, v in args[-1].items()])
    else:
        params = ""
    log_debug(f"{repr(args[0])} calling for API {decorating(args[1], 32, 0)}({params})")


class basic_bot:
    @log_exceptions
    def __init__(self, token, proxy="", name: str = None):
        self.__token = token
        self.__proxy = {'https': proxy, 'http': proxy}
        self.__name = name

        if name is None:
            name = hex(id(self))

        if bot_namelist.get(name) is not None:
            raise Exception("Can't register bot in same name twice")
        else:
            bot_namelist[name] = self

        try:
            self.me = self.getMe()
        except Exception:
            raise Exception("Can't connect telegram service or token is invalid.")

    def __str__(self):
        return str(self.me)

    def __repr__(self):
        return f"bot<{self.__name}>"

    @with_info(_log_api, begin='', report_params=True)
    @log_exceptions
    def __post(self, command, params=None):
        r = post(self.url + command, params, self.proxy)
        if not r['ok']:
            raise Exception('Bad Requests')
        return r['result']

    def shutdown(self):
        del self
    # properties

    @property
    def token(self):
        return self.__token

    @property
    def proxy(self):
        return self.__proxy

    @property
    def url(self):
        return f"https://api.telegram.org/bot{self.__token}/"

    # API functions
    @with_return(User)
    def getMe(self):
        return self.__post('getMe')

    def getUpdates(self, **argv):
        params_table = {
            'offset': int,
            'limit': int,
            'timeout': int,
            'allowed_updates': list,
        }
        verify_params(params_table, argv)
        return [Update(x) for x in self.__post('getUpdates', argv)]

    def setWebhook(self, url, **argv):
        params_table = {
            'url': str,
            'certificate': InputFile,
            'ip_address': str,
            'max_connections': int,
            'allowed_updates': list,
            'drop_pending_updates': bool,
        }
        argv['url'] = url
        verify_params(params_table, argv)
        return self.__post('setWebhook', argv)

    def deleteWebhook(self, **argv):
        params_table = {
            'drop_pending_updates': bool,
        }
        verify_params(params_table, argv)
        return self.__post('deleteWebhook', argv)

    def getWebhookInfo(self):
        return WebhookInfo(self.__post('getWebhookInfo'))

    def sendMessage(self, chat_id, text, **argv):
        params_table = {
            'chat_id': [int, str],
            'text': str,
            'parse_mode': str,
            'entities': list,
            'disable_web_page_preview': bool,
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
            'reply_markup': [InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply],
        }
        argv['chat_id'] = chat_id
        argv['text'] = text
        verify_params(params_table, argv)
        return Message(self.__post('sendMessage', argv))

    def forwardMessage(self, chat_id, from_chat_id, message_id, **argv):
        params_table = {
            'chat_id': [int, str],
            'from_chat_id': [int, str],
            'disable_notification': bool,
            'protect_content': bool,
            'message_id': int,
        }
        argv['chat_id'] = chat_id
        argv['from_chat_id'] = from_chat_id
        argv['message_id'] = message_id
        verify_params(params_table, argv)
        return Message(self.__post('forwardMessage', argv))

    def copyMessage(self, chat_id, from_chat_id, message_id, **argv):
        params_table = {
            'chat_id': [int, str],
            'from_chat_id': [int, str],
            'message_id': int,
            'caption': str,
            'parse_mode': str,
            'caption_entities': list,
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
            'reply_markup': [InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply],
        }
        argv['chat_id'] = chat_id
        argv['from_chat_id'] = from_chat_id
        argv['message_id'] = message_id
        verify_params(params_table, argv)
        return MessageId(self.__post('copyMessage', argv))

    def sendPhoto(self, chat_id, photo, **argv):
        params_table = {
            'chat_id': [int, str],
            'photo': [InputFile, str],
            'caption': str,
            'parse_mode': str,
            'caption_entities': list,
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
            'reply_markup': [InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply],
        }
        argv['chat_id'] = chat_id
        argv['photo'] = photo
        verify_params(params_table, argv)
        return Message(self.__post('sendPhoto', argv))

    def sendAudio(self, chat_id, audio, **argv):
        params_table = {
            'chat_id': [int, str],
            'audio': [InputFile, str],
            'caption': str,
            'parse_mode': str,
            'caption_entities': list,
            'duration': int,
            'performer': str,
            'title': str,
            'thumb': [InputFile, str],
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
            'reply_markup': [InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply],
        }
        argv['chat_id'] = chat_id
        argv['audio'] = audio
        verify_params(params_table, argv)
        return Message(self.__post('sendAudio', argv))

    def sendDocument(self, chat_id, document, **argv):
        params_table = {
            'chat_id': [int, str],
            'document': [InputFile, str],
            'thumb': [InputFile, str],
            'caption': str,
            'parse_mode': str,
            'caption_entities': list,
            'disable_content_type_detection': bool,
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
            'reply_markup': [InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply],
        }
        argv['chat_id'] = chat_id
        argv['document'] = document
        verify_params(params_table, argv)
        return Message(self.__post('sendDocument', argv))

    def sendVideo(self, chat_id, video, **argv):
        params_table = {
            'chat_id': [int, str],
            'video': [InputFile, str],
            'duration': int,
            'width': int,
            'height': int,
            'thumb': [InputFile, str],
            'caption': str,
            'parse_mode': str,
            'caption_entities': list,
            'supports_streaming': bool,
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
            'reply_markup': [InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply],
        }
        argv['chat_id'] = chat_id
        argv['video'] = video
        verify_params(params_table, argv)
        return Message(self.__post('sendVideo', argv))

    def sendAnimation(self, chat_id, animation, **argv):
        params_table = {
            'chat_id': [int, str],
            'animation': [InputFile, str],
            'duration': int,
            'width': int,
            'height': int,
            'thumb': [InputFile, str],
            'caption': str,
            'parse_mode': str,
            'caption_entities': list,
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
            'reply_markup': [InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply],
        }
        argv['chat_id'] = chat_id
        argv['animation'] = animation
        verify_params(params_table, argv)
        return Message(self.__post('sendAnimation', argv))

    def sendVoice(self, chat_id, voice, **argv):
        params_table = {
            'chat_id': [int, str],
            'voice': [InputFile, str],
            'caption': str,
            'parse_mode': str,
            'caption_entities': list,
            'duration': int,
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
            'reply_markup': [InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply],
        }
        argv['chat_id'] = chat_id
        argv['voice'] = voice
        verify_params(params_table, argv)
        return Message(self.__post('sendVoice', argv))

    def sendVideoNote(self, chat_id, video_note, **argv):
        params_table = {
            'chat_id': [int, str],
            'video_note': [InputFile, str],
            'duration': int,
            'length': int,
            'thumb': [InputFile, str],
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
            'reply_markup': [InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply],
        }
        argv['chat_id'] = chat_id
        argv['video_note'] = video_note
        verify_params(params_table, argv)
        return Message(self.__post('sendVideoNote', argv))

    def sendMediaGroup(self, chat_id, media, **argv):
        params_table = {
            'chat_id': [int, str],
            'media': list,
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
        }
        argv['chat_id'] = chat_id
        argv['media'] = media
        verify_params(params_table, argv)
        return Message(self.__post('sendMediaGroup', argv))

    def sendLocation(self, chat_id, latitude, longitude, **argv):
        params_table = {
            'chat_id': [int, str],
            'latitude': float,
            'longitude': float,
            'horizontal_accuracy': float,
            'live_period': int,
            'heading': int,
            'proximity_alert_radius': int,
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
            'reply_markup': [InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply],
        }
        argv['chat_id'] = chat_id
        argv['latitude'] = latitude
        argv['longitude'] = longitude
        verify_params(params_table, argv)
        return Message(self.__post('sendLocation', argv))

    def editMessageLiveLocation(self, latitude, longitude, **argv):
        params_table = {
            'chat_id': [int, str],
            'message_id': int,
            'inline_message_id': str,
            'latitude': float,
            'longitude': float,
            'horizontal_accuracy': float,
            'heading': int,
            'proximity_alert_radius': int,
            'reply_markup': InlineKeyboardMarkup,
        }
        argv['latitude'] = latitude
        argv['longitude'] = longitude
        verify_params(params_table, argv)
        return self.__post('editMessageLiveLocation', argv)

    def stopMessageLiveLocation(self, **argv):
        params_table = {
            'chat_id': [int, str],
            'message_id': int,
            'inline_message_id': str,
            'reply_markup': InlineKeyboardMarkup,
        }
        verify_params(params_table, argv)
        return self.__post('stopMessageLiveLocation', argv)

    def sendVenue(self, chat_id, latitude, longitude, title, address, **argv):
        params_table = {
            'chat_id': [int, str],
            'latitude': float,
            'longitude': float,
            'title': str,
            'address': str,
            'foursquare_id': str,
            'foursquare_type': str,
            'google_place_id': str,
            'google_place_type': str,
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
            'reply_markup': [InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply],
        }
        argv['chat_id'] = chat_id
        argv['latitude'] = latitude
        argv['longitude'] = longitude
        argv['title'] = title
        argv['address'] = address
        verify_params(params_table, argv)
        return Message(self.__post('sendVenue', argv))

    def sendContact(self, chat_id, phone_number, first_name, **argv):
        params_table = {
            'chat_id': [int, str],
            'phone_number': str,
            'first_name': str,
            'last_name': str,
            'vcard': str,
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
            'reply_markup': [InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply],
        }
        argv['chat_id'] = chat_id
        argv['phone_number'] = phone_number
        argv['first_name'] = first_name
        verify_params(params_table, argv)
        return Message(self.__post('sendContact', argv))

    def sendPoll(self, chat_id, question, options, **argv):
        params_table = {
            'chat_id': [int, str],
            'question': str,
            'options': list,
            'is_anonymous': bool,
            'type': str,
            'allows_multiple_answers': bool,
            'correct_option_id': int,
            'explanation': str,
            'explanation_parse_mode': str,
            'explanation_entities': list,
            'open_period': int,
            'close_date': int,
            'is_closed': bool,
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
            'reply_markup': [InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply],
        }
        argv['chat_id'] = chat_id
        argv['question'] = question
        argv['options'] = options
        verify_params(params_table, argv)
        return Message(self.__post('sendPoll', argv))

    def sendDice(self, chat_id, **argv):
        params_table = {
            'chat_id': [int, str],
            'emoji': str,
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
            'reply_markup': [InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply],
        }
        argv['chat_id'] = chat_id
        verify_params(params_table, argv)
        return Message(self.__post('sendDice', argv))

    def sendChatAction(self, chat_id, action, **argv):
        params_table = {
            'chat_id': [int, str],
            'action': str,
        }
        argv['chat_id'] = chat_id
        argv['action'] = action
        verify_params(params_table, argv)
        return self.__post('sendChatAction', argv)

    def getUserProfilePhotos(self, user_id, **argv):
        params_table = {
            'user_id': int,
            'offset': int,
            'limit': int,
        }
        argv['user_id'] = user_id
        verify_params(params_table, argv)
        return UserProfilePhotos(self.__post('getUserProfilePhotos', argv))

    def getFile(self, file_id, **argv):
        params_table = {
            'file_id': str,
        }
        argv['file_id'] = file_id
        verify_params(params_table, argv)
        return File(self.__post('getFile', argv))

    def banChatMember(self, chat_id, user_id, **argv):
        params_table = {
            'chat_id': [int, str],
            'user_id': int,
            'until_date': int,
            'revoke_messages': bool,
        }
        argv['chat_id'] = chat_id
        argv['user_id'] = user_id
        verify_params(params_table, argv)
        return self.__post('banChatMember', argv)

    def unbanChatMember(self, chat_id, user_id, **argv):
        params_table = {
            'chat_id': [int, str],
            'user_id': int,
            'only_if_banned': bool,
        }
        argv['chat_id'] = chat_id
        argv['user_id'] = user_id
        verify_params(params_table, argv)
        return self.__post('unbanChatMember', argv)

    def restrictChatMember(self, chat_id, user_id, permissions, **argv):
        params_table = {
            'chat_id': [int, str],
            'user_id': int,
            'permissions': ChatPermissions,
            'until_date': int,
        }
        argv['chat_id'] = chat_id
        argv['user_id'] = user_id
        argv['permissions'] = permissions
        verify_params(params_table, argv)
        return self.__post('restrictChatMember', argv)

    def promoteChatMember(self, chat_id, user_id, **argv):
        params_table = {
            'chat_id': [int, str],
            'user_id': int,
            'is_anonymous': bool,
            'can_manage_chat': bool,
            'can_post_messages': bool,
            'can_edit_messages': bool,
            'can_delete_messages': bool,
            'can_manage_voice_chats': bool,
            'can_restrict_members': bool,
            'can_promote_members': bool,
            'can_change_info': bool,
            'can_invite_users': bool,
            'can_pin_messages': bool,
        }
        argv['chat_id'] = chat_id
        argv['user_id'] = user_id
        verify_params(params_table, argv)
        return self.__post('promoteChatMember', argv)

    def setChatAdministratorCustomTitle(self, chat_id, user_id, custom_title, **argv):
        params_table = {
            'chat_id': [int, str],
            'user_id': int,
            'custom_title': str,
        }
        argv['chat_id'] = chat_id
        argv['user_id'] = user_id
        argv['custom_title'] = custom_title
        verify_params(params_table, argv)
        return self.__post('setChatAdministratorCustomTitle', argv)

    def banChatSenderChat(self, chat_id, sender_chat_id, **argv):
        params_table = {
            'chat_id': [int, str],
            'sender_chat_id': int,
        }
        argv['chat_id'] = chat_id
        argv['sender_chat_id'] = sender_chat_id
        verify_params(params_table, argv)
        return self.__post('banChatSenderChat', argv)

    def unbanChatSenderChat(self, chat_id, sender_chat_id, **argv):
        params_table = {
            'chat_id': [int, str],
            'sender_chat_id': int,
        }
        argv['chat_id'] = chat_id
        argv['sender_chat_id'] = sender_chat_id
        verify_params(params_table, argv)
        return self.__post('unbanChatSenderChat', argv)

    def setChatPermissions(self, chat_id, permissions, **argv):
        params_table = {
            'chat_id': [int, str],
            'permissions': ChatPermissions,
        }
        argv['chat_id'] = chat_id
        argv['permissions'] = permissions
        verify_params(params_table, argv)
        return self.__post('setChatPermissions', argv)

    def exportChatInviteLink(self, chat_id, **argv):
        params_table = {
            'chat_id': [int, str],
        }
        argv['chat_id'] = chat_id
        verify_params(params_table, argv)
        return self.__post('exportChatInviteLink', argv)

    def createChatInviteLink(self, chat_id, **argv):
        params_table = {
            'chat_id': [int, str],
            'name': str,
            'expire_date': int,
            'member_limit': int,
            'creates_join_request': bool,
        }
        argv['chat_id'] = chat_id
        verify_params(params_table, argv)
        return ChatInviteLink(self.__post('createChatInviteLink', argv))

    def editChatInviteLink(self, chat_id, invite_link, **argv):
        params_table = {
            'chat_id': [int, str],
            'invite_link': str,
            'name': str,
            'expire_date': int,
            'member_limit': int,
            'creates_join_request': bool,
        }
        argv['chat_id'] = chat_id
        argv['invite_link'] = invite_link
        verify_params(params_table, argv)
        return ChatInviteLink(self.__post('editChatInviteLink', argv))

    def revokeChatInviteLink(self, chat_id, invite_link, **argv):
        params_table = {
            'chat_id': [int, str],
            'invite_link': str,
        }
        argv['chat_id'] = chat_id
        argv['invite_link'] = invite_link
        verify_params(params_table, argv)
        return ChatInviteLink(self.__post('revokeChatInviteLink', argv))

    def approveChatJoinRequest(self, chat_id, user_id, **argv):
        params_table = {
            'chat_id': [int, str],
            'user_id': int,
        }
        argv['chat_id'] = chat_id
        argv['user_id'] = user_id
        verify_params(params_table, argv)
        return self.__post('approveChatJoinRequest', argv)

    def declineChatJoinRequest(self, chat_id, user_id, **argv):
        params_table = {
            'chat_id': [int, str],
            'user_id': int,
        }
        argv['chat_id'] = chat_id
        argv['user_id'] = user_id
        verify_params(params_table, argv)
        return self.__post('declineChatJoinRequest', argv)

    def setChatPhoto(self, chat_id, photo, **argv):
        params_table = {
            'chat_id': [int, str],
            'photo': InputFile,
        }
        argv['chat_id'] = chat_id
        argv['photo'] = photo
        verify_params(params_table, argv)
        return self.__post('setChatPhoto', argv)

    def deleteChatPhoto(self, chat_id, **argv):
        params_table = {
            'chat_id': [int, str],
        }
        argv['chat_id'] = chat_id
        verify_params(params_table, argv)
        return self.__post('deleteChatPhoto', argv)

    def setChatTitle(self, chat_id, title, **argv):
        params_table = {
            'chat_id': [int, str],
            'title': str,
        }
        argv['chat_id'] = chat_id
        argv['title'] = title
        verify_params(params_table, argv)
        return self.__post('setChatTitle', argv)

    def setChatDescription(self, chat_id, **argv):
        params_table = {
            'chat_id': [int, str],
            'description': str,
        }
        argv['chat_id'] = chat_id
        verify_params(params_table, argv)
        return self.__post('setChatDescription', argv)

    def pinChatMessage(self, chat_id, message_id, **argv):
        params_table = {
            'chat_id': [int, str],
            'message_id': int,
            'disable_notification': bool,
        }
        argv['chat_id'] = chat_id
        argv['message_id'] = message_id
        verify_params(params_table, argv)
        return self.__post('pinChatMessage', argv)

    def unpinChatMessage(self, chat_id, **argv):
        params_table = {
            'chat_id': [int, str],
            'message_id': int,
        }
        argv['chat_id'] = chat_id
        verify_params(params_table, argv)
        return self.__post('unpinChatMessage', argv)

    def unpinAllChatMessages(self, chat_id, **argv):
        params_table = {
            'chat_id': [int, str],
        }
        argv['chat_id'] = chat_id
        verify_params(params_table, argv)
        return self.__post('unpinAllChatMessages', argv)

    def leaveChat(self, chat_id, **argv):
        params_table = {
            'chat_id': [int, str],
        }
        argv['chat_id'] = chat_id
        verify_params(params_table, argv)
        return self.__post('leaveChat', argv)

    def getChat(self, chat_id, **argv):
        params_table = {
            'chat_id': [int, str],
        }
        argv['chat_id'] = chat_id
        verify_params(params_table, argv)
        return Chat(self.__post('getChat', argv))

    def getChatAdministrators(self, chat_id, **argv):
        params_table = {
            'chat_id': [int, str],
        }
        argv['chat_id'] = chat_id
        verify_params(params_table, argv)
        return [ChatMember(x) for x in self.__post('getChatAdministrators', argv)]

    def getChatMemberCount(self, chat_id, **argv):
        params_table = {
            'chat_id': [int, str],
        }
        argv['chat_id'] = chat_id
        verify_params(params_table, argv)
        return self.__post('getChatMemberCount', argv)

    def getChatMember(self, chat_id, user_id, **argv):
        params_table = {
            'chat_id': [int, str],
            'user_id': int,
        }
        argv['chat_id'] = chat_id
        argv['user_id'] = user_id
        verify_params(params_table, argv)
        return [ChatMember(x) for x in self.__post('getChatMember', argv)]

    def setChatStickerSet(self, chat_id, sticker_set_name, **argv):
        params_table = {
            'chat_id': [int, str],
            'sticker_set_name': str,
        }
        argv['chat_id'] = chat_id
        argv['sticker_set_name'] = sticker_set_name
        verify_params(params_table, argv)
        return self.__post('setChatStickerSet', argv)

    def deleteChatStickerSet(self, chat_id, **argv):
        params_table = {
            'chat_id': [int, str],
        }
        argv['chat_id'] = chat_id
        verify_params(params_table, argv)
        return self.__post('deleteChatStickerSet', argv)

    def answerCallbackQuery(self, callback_query_id, **argv):
        params_table = {
            'callback_query_id': str,
            'text': str,
            'show_alert': bool,
            'url': str,
            'cache_time': int,
        }
        argv['callback_query_id'] = callback_query_id
        verify_params(params_table, argv)
        return self.__post('answerCallbackQuery', argv)

    def setMyCommands(self, commands, **argv):
        params_table = {
            'commands': list,
            'scope': BotCommandScope,
            'language_code': str,
        }
        argv['commands'] = commands
        verify_params(params_table, argv)
        return self.__post('setMyCommands', argv)

    def deleteMyCommands(self, **argv):
        params_table = {
            'scope': BotCommandScope,
            'language_code': str,
        }
        verify_params(params_table, argv)
        return self.__post('deleteMyCommands', argv)

    def getMyCommands(self, **argv):
        params_table = {
            'scope': BotCommandScope,
            'language_code': str,
        }
        verify_params(params_table, argv)
        return [BotCommand(x) for x in self.__post('getMyCommands', argv)]

    def editMessageText(self, text, **argv):
        params_table = {
            'chat_id': [int, str],
            'message_id': int,
            'inline_message_id': str,
            'text': str,
            'parse_mode': str,
            'entities': list,
            'disable_web_page_preview': bool,
            'reply_markup': InlineKeyboardMarkup,
        }
        argv['text'] = text
        verify_params(params_table, argv)
        return Message(self.__post('editMessageText', argv))

    def editMessageCaption(self, **argv):
        params_table = {
            'chat_id': [int, str],
            'message_id': int,
            'inline_message_id': str,
            'caption': str,
            'parse_mode': str,
            'caption_entities': list,
            'reply_markup': InlineKeyboardMarkup,
        }
        verify_params(params_table, argv)
        return Message(self.__post('editMessageCaption', argv))

    def editMessageMedia(self, media, **argv):
        params_table = {
            'chat_id': [int, str],
            'message_id': int,
            'inline_message_id': str,
            'media': InputMedia,
            'reply_markup': InlineKeyboardMarkup,
        }
        argv['media'] = media
        verify_params(params_table, argv)
        return Message(self.__post('editMessageMedia', argv))

    def editMessageReplyMarkup(self, **argv):
        params_table = {
            'chat_id': [int, str],
            'message_id': int,
            'inline_message_id': str,
            'reply_markup': InlineKeyboardMarkup,
        }
        verify_params(params_table, argv)
        return Message(self.__post('editMessageReplyMarkup', argv))

    def stopPoll(self, chat_id, message_id, **argv):
        params_table = {
            'chat_id': [int, str],
            'message_id': int,
            'reply_markup': InlineKeyboardMarkup,
        }
        argv['chat_id'] = chat_id
        argv['message_id'] = message_id
        verify_params(params_table, argv)
        return Poll(self.__post('stopPoll', argv))

    def deleteMessage(self, chat_id, message_id, **argv):
        params_table = {
            'chat_id': [int, str],
            'message_id': int,
        }
        argv['chat_id'] = chat_id
        argv['message_id'] = message_id
        verify_params(params_table, argv)
        return self.__post('deleteMessage', argv)

    def sendSticker(self, chat_id, sticker, **argv):
        params_table = {
            'chat_id': [int, str],
            'sticker': [InputFile, str],
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
            'reply_markup': [InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply],
        }
        argv['chat_id'] = chat_id
        argv['sticker'] = sticker
        verify_params(params_table, argv)
        return Message(self.__post('sendSticker', argv))

    def getStickerSet(self, name, **argv):
        params_table = {
            'name': str,
        }
        argv['name'] = name
        verify_params(params_table, argv)
        return StickerSet(self.__post('getStickerSet', argv))

    def uploadStickerFile(self, user_id, png_sticker, **argv):
        params_table = {
            'user_id': int,
            'png_sticker': InputFile,
        }
        argv['user_id'] = user_id
        argv['png_sticker'] = png_sticker
        verify_params(params_table, argv)
        return File(self.__post('uploadStickerFile', argv))

    def createNewStickerSet(self, user_id, name, title, emojis, **argv):
        params_table = {
            'user_id': int,
            'name': str,
            'title': str,
            'png_sticker': [InputFile, str],
            'tgs_sticker': InputFile,
            'webm_sticker': InputFile,
            'emojis': str,
            'contains_masks': bool,
            'mask_position': MaskPosition,
        }
        argv['user_id'] = user_id
        argv['name'] = name
        argv['title'] = title
        argv['emojis'] = emojis
        verify_params(params_table, argv)
        return self.__post('createNewStickerSet', argv)

    def addStickerToSet(self, user_id, name, emojis, **argv):
        params_table = {
            'user_id': int,
            'name': str,
            'png_sticker': [InputFile, str],
            'tgs_sticker': InputFile,
            'webm_sticker': InputFile,
            'emojis': str,
            'mask_position': MaskPosition,
        }
        argv['user_id'] = user_id
        argv['name'] = name
        argv['emojis'] = emojis
        verify_params(params_table, argv)
        return self.__post('addStickerToSet', argv)

    def setStickerPositionInSet(self, sticker, position, **argv):
        params_table = {
            'sticker': str,
            'position': int,
        }
        argv['sticker'] = sticker
        argv['position'] = position
        verify_params(params_table, argv)
        return self.__post('setStickerPositionInSet', argv)

    def deleteStickerFromSet(self, sticker, **argv):
        params_table = {
            'sticker': str,
        }
        argv['sticker'] = sticker
        verify_params(params_table, argv)
        return self.__post('deleteStickerFromSet', argv)

    def setStickerSetThumb(self, name, user_id, **argv):
        params_table = {
            'name': str,
            'user_id': int,
            'thumb': [InputFile, str],
        }
        argv['name'] = name
        argv['user_id'] = user_id
        verify_params(params_table, argv)
        return self.__post('setStickerSetThumb', argv)

    def answerInlineQuery(self, inline_query_id, results, **argv):
        params_table = {
            'inline_query_id': str,
            'results': list,
            'cache_time': int,
            'is_personal': bool,
            'next_offset': str,
            'switch_pm_text': str,
            'switch_pm_parameter': str,
        }
        argv['inline_query_id'] = inline_query_id
        argv['results'] = results
        verify_params(params_table, argv)
        return self.__post('answerInlineQuery', argv)

    def sendInvoice(self, chat_id, title, description, payload, provider_token, currency, prices, **argv):
        params_table = {
            'chat_id': [int, str],
            'title': str,
            'description': str,
            'payload': str,
            'provider_token': str,
            'currency': str,
            'prices': list,
            'max_tip_amount': int,
            'suggested_tip_amounts': list,
            'start_parameter': str,
            'provider_data': str,
            'photo_url': str,
            'photo_size': int,
            'photo_width': int,
            'photo_height': int,
            'need_name': bool,
            'need_phone_number': bool,
            'need_email': bool,
            'need_shipping_address': bool,
            'send_phone_number_to_provider': bool,
            'send_email_to_provider': bool,
            'is_flexible': bool,
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
            'reply_markup': InlineKeyboardMarkup,
        }
        argv['chat_id'] = chat_id
        argv['title'] = title
        argv['description'] = description
        argv['payload'] = payload
        argv['provider_token'] = provider_token
        argv['currency'] = currency
        argv['prices'] = prices
        verify_params(params_table, argv)
        return Message(self.__post('sendInvoice', argv))

    def answerShippingQuery(self, shipping_query_id, ok, **argv):
        params_table = {
            'shipping_query_id': str,
            'ok': bool,
            'shipping_options': list,
            'error_message': str,
        }
        argv['shipping_query_id'] = shipping_query_id
        argv['ok'] = ok
        verify_params(params_table, argv)
        return self.__post('answerShippingQuery', argv)

    def answerPreCheckoutQuery(self, pre_checkout_query_id, ok, **argv):
        params_table = {
            'pre_checkout_query_id': str,
            'ok': bool,
            'error_message': str,
        }
        argv['pre_checkout_query_id'] = pre_checkout_query_id
        argv['ok'] = ok
        verify_params(params_table, argv)
        return self.__post('answerPreCheckoutQuery', argv)

    def setPassportDataErrors(self, user_id, errors, **argv):
        params_table = {
            'user_id': int,
            'errors': list,
        }
        argv['user_id'] = user_id
        argv['errors'] = errors
        verify_params(params_table, argv)
        return self.__post('setPassportDataErrors', argv)

    def sendGame(self, chat_id, game_short_name, **argv):
        params_table = {
            'chat_id': int,
            'game_short_name': str,
            'disable_notification': bool,
            'protect_content': bool,
            'reply_to_message_id': int,
            'allow_sending_without_reply': bool,
            'reply_markup': InlineKeyboardMarkup,
        }
        argv['chat_id'] = chat_id
        argv['game_short_name'] = game_short_name
        verify_params(params_table, argv)
        return Message(self.__post('sendGame', argv))

    def setGameScore(self, user_id, score, **argv):
        params_table = {
            'user_id': int,
            'score': int,
            'force': bool,
            'disable_edit_message': bool,
            'chat_id': int,
            'message_id': int,
            'inline_message_id': str,
        }
        argv['user_id'] = user_id
        argv['score'] = score
        verify_params(params_table, argv)
        return Message(self.__post('setGameScore', argv))

    def getGameHighScores(self, user_id, **argv):
        params_table = {
            'user_id': int,
            'chat_id': int,
            'message_id': int,
            'inline_message_id': str,
        }
        argv['user_id'] = user_id
        verify_params(params_table, argv)
        return [GameHighScore(x) for x in self.__post('getGameHighScores', argv)]
