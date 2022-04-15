from teleneko.bits.strings import *
from teleneko.globe import log_warn


class tgtype:
    __type_table__ = {}

    def __init__(self, json_info=None):
        if json_info is None:
            json_info = {}
        for name, val in json_info.items():

            try:
                expectType = self.__type_table__[name]
            except KeyError:
                log_warn(f"received unexpected param '{name}'", self)
                continue

            if type(expectType) != list:
                self.__dict__[name] = expectType(val)
                continue

            if len(expectType) == 1:
                self.__dict__[name] = [expectType[0](v) for v in val]
                continue

            for e in expectType:
                if isinstance(val, e):
                    self.__dict__[name] = e(val)
                    break

    def __tree__(self, offset=""):
        s = ""
        for x, y in self.__dict__.items():
            tail = "├─ " if x != list(self.__dict__.keys())[-1] else "└─ "
            addi = "│  " if x != list(self.__dict__.keys())[-1] else "   "
            if isinstance(y, list):
                s += offset + tail + f"{str_type(y)} {x}:\n"
                offset = offset + addi
                for p in range(len(y)):
                    tail = "├─ " if p != len(y) - 1 else "└─ "
                    addi = "│  " if p != len(y) - 1 else "   "
                    if isinstance(y[p], tgtype):
                        s += offset + tail + f"{x}[{p}] -> {str_type(y[p])} :\n" + y[p].__tree__(offset + addi)
                    else:
                        s += offset + tail + f"{x}[{p}] -> {str_type(y[p])} : {str_val(y[p])}\n"
            elif isinstance(y, tgtype):
                s += offset + tail + f"{str_type(y)} {x} :\n" + y.__tree__(offset + addi)
            else:
                s += offset + tail + f"{str_type(y)} {x} : {str_val(y)}\n"
        return s

    def __str__(self):
        return decorating(str_type(self) + "\n" + self.__tree__(), 37, 0)

    def __repr__(self):
        return f"type<{str_type(self, True)} at {hex(id(self))}>"


class Update(tgtype): pass


class WebhookInfo(tgtype): pass


class User(tgtype): pass


class Chat(tgtype): pass


class Message(tgtype): pass


class MessageId(tgtype): pass


class MessageEntity(tgtype): pass


class PhotoSize(tgtype): pass


class Animation(tgtype): pass


class Audio(tgtype): pass


class Document(tgtype): pass


class Video(tgtype): pass


class VideoNote(tgtype): pass


class Voice(tgtype): pass


class Contact(tgtype): pass


class Dice(tgtype): pass


class PollOption(tgtype): pass


class PollAnswer(tgtype): pass


class Poll(tgtype): pass


class Location(tgtype): pass


class Venue(tgtype): pass


class ProximityAlertTriggered(tgtype): pass


class MessageAutoDeleteTimerChanged(tgtype): pass


class VoiceChatScheduled(tgtype): pass


class VoiceChatEnded(tgtype): pass


class VoiceChatParticipantsInvited(tgtype): pass


class UserProfilePhotos(tgtype): pass


class File(tgtype): pass


class ReplyKeyboardMarkup(tgtype): pass


class KeyboardButton(tgtype): pass


class KeyboardButtonPollType(tgtype): pass


class ReplyKeyboardRemove(tgtype): pass


class InlineKeyboardMarkup(tgtype): pass


class InlineKeyboardButton(tgtype): pass


class TITLE(tgtype): pass


class CallbackQuery(tgtype): pass


class ForceReply(tgtype): pass


class ChatPhoto(tgtype): pass


class ChatInviteLink(tgtype): pass


class ChatMember(tgtype): pass


class ChatMemberOwner(ChatMember): pass


class ChatMemberAdministrator(ChatMember): pass


class ChatMemberMember(ChatMember): pass


class ChatMemberRestricted(ChatMember): pass


class ChatMemberLeft(ChatMember): pass


class ChatMemberBanned(ChatMember): pass


class ChatMemberUpdated(tgtype): pass


class ChatJoinRequest(tgtype): pass


class ChatPermissions(tgtype): pass


class ChatLocation(tgtype): pass


class BotCommand(tgtype): pass


class BotCommandScope(tgtype): pass


class BotCommandScopeDefault(BotCommandScope): pass


class BotCommandScopeAllPrivateChats(BotCommandScope): pass


class BotCommandScopeAllGroupChats(BotCommandScope): pass


class BotCommandScopeAllChatAdministrators(BotCommandScope): pass


class BotCommandScopeChat(BotCommandScope): pass


class BotCommandScopeChatAdministrators(BotCommandScope): pass


class BotCommandScopeChatMember(BotCommandScope): pass


class ResponseParameters(tgtype): pass


class InputMedia(tgtype): pass


class InputMediaPhoto(tgtype): pass


class InputMediaVideo(InputMedia): pass


class InputMediaAnimation(InputMedia): pass


class InputMediaAudio(InputMedia): pass


class InputMediaDocument(InputMedia): pass


class Sticker(tgtype): pass


class StickerSet(tgtype): pass


class MaskPosition(tgtype): pass


class InlineQuery(tgtype): pass


class InlineQueryResult(tgtype): pass


class InlineQueryResultArticle(InlineQueryResult): pass


class InlineQueryResultPhoto(InlineQueryResult): pass


class InlineQueryResultGif(InlineQueryResult): pass


class InlineQueryResultMpeg4Gif(InlineQueryResult): pass


class InlineQueryResultVideo(InlineQueryResult): pass


class InlineQueryResultAudio(InlineQueryResult): pass


class InlineQueryResultVoice(InlineQueryResult): pass


class InlineQueryResultDocument(InlineQueryResult): pass


class InlineQueryResultLocation(InlineQueryResult): pass


class InlineQueryResultVenue(InlineQueryResult): pass


class InlineQueryResultContact(InlineQueryResult): pass


class InlineQueryResultGame(InlineQueryResult): pass


class InlineQueryResultCachedPhoto(InlineQueryResult): pass


class InlineQueryResultCachedGif(InlineQueryResult): pass


class InlineQueryResultCachedMpeg4Gif(InlineQueryResult): pass


class InlineQueryResultCachedSticker(InlineQueryResult): pass


class InlineQueryResultCachedDocument(InlineQueryResult): pass


class InlineQueryResultCachedVideo(InlineQueryResult): pass


class InlineQueryResultCachedVoice(InlineQueryResult): pass


class InlineQueryResultCachedAudio(InlineQueryResult): pass


class InputMessageContent(tgtype): pass


class InputTextMessageContent(InputMessageContent): pass


class InputLocationMessageContent(InputMessageContent): pass


class InputVenueMessageContent(InputMessageContent): pass


class InputContactMessageContent(InputMessageContent): pass


class InputInvoiceMessageContent(InputMessageContent): pass


class ChosenInlineResult(tgtype): pass


class LabeledPrice(tgtype): pass


class Invoice(tgtype): pass


class ShippingAddress(tgtype): pass


class OrderInfo(tgtype): pass


class ShippingOption(tgtype): pass


class SuccessfulPayment(tgtype): pass


class ShippingQuery(tgtype): pass


class PreCheckoutQuery(tgtype): pass


class PassportData(tgtype): pass


class PassportFile(tgtype): pass


class EncryptedPassportElement(tgtype): pass


class EncryptedCredentials(tgtype): pass


class PassportElementError(tgtype): pass


class PassportElementErrorDataField(PassportElementError): pass


class PassportElementErrorFrontSide(PassportElementError): pass


class PassportElementErrorReverseSide(PassportElementError): pass


class PassportElementErrorSelfie(PassportElementError): pass


class PassportElementErrorFile(PassportElementError): pass


class PassportElementErrorFiles(PassportElementError): pass


class PassportElementErrorTranslationFile(PassportElementError): pass


class PassportElementErrorTranslationFiles(PassportElementError): pass


class PassportElementErrorUnspecified(PassportElementError): pass


class Game(tgtype): pass


class GameHighScore(tgtype): pass


class VoiceChatStarted(tgtype): pass


class LoginUrl(tgtype): pass


class CallbackGame(tgtype): pass


class InputFile(tgtype): pass


Update.__type_table__ = {
    'update_id': int,
    'message': Message,
    'edited_message': Message,
    'channel_post': Message,
    'edited_channel_post': Message,
    'inline_query': InlineQuery,
    'chosen_inline_result': ChosenInlineResult,
    'callback_query': CallbackQuery,
    'shipping_query': ShippingQuery,
    'pre_checkout_query': PreCheckoutQuery,
    'poll': Poll,
    'poll_answer': PollAnswer,
    'my_chat_member': ChatMemberUpdated,
    'chat_member': ChatMemberUpdated,
    'chat_join_request': ChatJoinRequest,
}

WebhookInfo.__type_table__ = {
    'url': str,
    'has_custom_certificate': bool,
    'pending_update_count': int,
    'ip_address': str,
    'last_error_date': int,
    'last_error_message': str,
    'max_connections': int,
    'allowed_updates': [str],
}

User.__type_table__ = {
    'id': int,
    'is_bot': bool,
    'first_name': str,
    'last_name': str,
    'username': str,
    'language_code': str,
    'can_join_groups': bool,
    'can_read_all_group_messages': bool,
    'supports_inline_queries': bool,
}

Chat.__type_table__ = {
    'id': int,
    'type': str,
    'title': str,
    'username': str,
    'first_name': str,
    'last_name': str,
    'photo': ChatPhoto,
    'bio': str,
    'has_private_forwards': bool,
    'description': str,
    'invite_link': str,
    'pinned_message': Message,
    'permissions': ChatPermissions,
    'slow_mode_delay': int,
    'message_auto_delete_time': int,
    'has_protected_content': bool,
    'sticker_set_name': str,
    'can_set_sticker_set': bool,
    'linked_chat_id': int,
    'location': ChatLocation,
}

Message.__type_table__ = {
    'message_id': int,
    'from': User,
    'sender_chat': Chat,
    'date': int,
    'chat': Chat,
    'forward_from': User,
    'forward_from_chat': Chat,
    'forward_from_message_id': int,
    'forward_signature': str,
    'forward_sender_name': str,
    'forward_date': int,
    'is_automatic_forward': bool,
    'reply_to_message': Message,
    'via_bot': User,
    'edit_date': int,
    'has_protected_content': bool,
    'media_group_id': str,
    'author_signature': str,
    'text': str,
    'entities': [MessageEntity],
    'animation': Animation,
    'audio': Audio,
    'document': Document,
    'photo': [PhotoSize],
    'sticker': Sticker,
    'video': Video,
    'video_note': VideoNote,
    'voice': Voice,
    'caption': str,
    'caption_entities': [MessageEntity],
    'contact': Contact,
    'dice': Dice,
    'game': Game,
    'poll': Poll,
    'venue': Venue,
    'location': Location,
    'new_chat_members': [User],
    'left_chat_member': User,
    'new_chat_title': str,
    'new_chat_photo': [PhotoSize],
    'delete_chat_photo': bool,
    'group_chat_created': bool,
    'supergroup_chat_created': bool,
    'channel_chat_created': bool,
    'message_auto_delete_timer_changed': MessageAutoDeleteTimerChanged,
    'migrate_to_chat_id': int,
    'migrate_from_chat_id': int,
    'pinned_message': Message,
    'invoice': Invoice,
    'successful_payment': SuccessfulPayment,
    'connected_website': str,
    'passport_data': PassportData,
    'proximity_alert_triggered': ProximityAlertTriggered,
    'voice_chat_scheduled': VoiceChatScheduled,
    'voice_chat_started': VoiceChatStarted,
    'voice_chat_ended': VoiceChatEnded,
    'voice_chat_participants_invited': VoiceChatParticipantsInvited,
    'reply_markup': InlineKeyboardMarkup,
}

MessageId.__type_table__ = {
    'message_id': int,
}

MessageEntity.__type_table__ = {
    'type': str,
    'offset': int,
    'length': int,
    'url': str,
    'user': User,
    'language': str,
}

PhotoSize.__type_table__ = {
    'file_id': str,
    'file_unique_id': str,
    'width': int,
    'height': int,
    'file_size': int,
}

Animation.__type_table__ = {
    'file_id': str,
    'file_unique_id': str,
    'width': int,
    'height': int,
    'duration': int,
    'thumb': PhotoSize,
    'file_name': str,
    'mime_type': str,
    'file_size': int,
}

Audio.__type_table__ = {
    'file_id': str,
    'file_unique_id': str,
    'duration': int,
    'performer': str,
    'title': str,
    'file_name': str,
    'mime_type': str,
    'file_size': int,
    'thumb': PhotoSize,
}

Document.__type_table__ = {
    'file_id': str,
    'file_unique_id': str,
    'thumb': PhotoSize,
    'file_name': str,
    'mime_type': str,
    'file_size': int,
}

Video.__type_table__ = {
    'file_id': str,
    'file_unique_id': str,
    'width': int,
    'height': int,
    'duration': int,
    'thumb': PhotoSize,
    'file_name': str,
    'mime_type': str,
    'file_size': int,
}

VideoNote.__type_table__ = {
    'file_id': str,
    'file_unique_id': str,
    'length': int,
    'duration': int,
    'thumb': PhotoSize,
    'file_size': int,
}

Voice.__type_table__ = {
    'file_id': str,
    'file_unique_id': str,
    'duration': int,
    'mime_type': str,
    'file_size': int,
}

Contact.__type_table__ = {
    'phone_number': str,
    'first_name': str,
    'last_name': str,
    'user_id': int,
    'vcard': str,
}

Dice.__type_table__ = {
    'emoji': str,
    'value': int,
}

PollOption.__type_table__ = {
    'text': str,
    'voter_count': int,
}

PollAnswer.__type_table__ = {
    'poll_id': str,
    'user': User,
    'option_ids': [int],
}

Poll.__type_table__ = {
    'id': str,
    'question': str,
    'options': [PollOption],
    'total_voter_count': int,
    'is_closed': bool,
    'is_anonymous': bool,
    'type': str,
    'allows_multiple_answers': bool,
    'correct_option_id': int,
    'explanation': str,
    'explanation_entities': [MessageEntity],
    'open_period': int,
    'close_date': int,
}

Location.__type_table__ = {
    'longitude': float,
    'latitude': float,
    'horizontal_accuracy': float,
    'live_period': int,
    'heading': int,
    'proximity_alert_radius': int,
}

Venue.__type_table__ = {
    'location': Location,
    'title': str,
    'address': str,
    'foursquare_id': str,
    'foursquare_type': str,
    'google_place_id': str,
    'google_place_type': str,
}

ProximityAlertTriggered.__type_table__ = {
    'traveler': User,
    'watcher': User,
    'distance': int,
}

MessageAutoDeleteTimerChanged.__type_table__ = {
    'message_auto_delete_time': int,
}

VoiceChatScheduled.__type_table__ = {
    'start_date': int,
}

VoiceChatEnded.__type_table__ = {
    'duration': int,
}

VoiceChatParticipantsInvited.__type_table__ = {
    'users': [User],
}

UserProfilePhotos.__type_table__ = {
    'total_count': int,
    'photos': [PhotoSize],
}

File.__type_table__ = {
    'file_id': str,
    'file_unique_id': str,
    'file_size': int,
    'file_path': str,
}

ReplyKeyboardMarkup.__type_table__ = {
    'keyboard': [KeyboardButton],
    'resize_keyboard': bool,
    'one_time_keyboard': bool,
    'input_field_placeholder': str,
    'selective': bool,
}

KeyboardButton.__type_table__ = {
    'text': str,
    'request_contact': bool,
    'request_location': bool,
    'request_poll': KeyboardButtonPollType,
}

KeyboardButtonPollType.__type_table__ = {
    'type': str,
}

ReplyKeyboardRemove.__type_table__ = {
    'remove_keyboard': bool,
    'selective': bool,
}

InlineKeyboardMarkup.__type_table__ = {
    'inline_keyboard': [InlineKeyboardButton],
}

InlineKeyboardButton.__type_table__ = {
    'text': str,
    'url': str,
    'login_url': LoginUrl,
    'callback_data': str,
    'switch_inline_query': str,
    'switch_inline_query_current_chat': str,
    'callback_game': CallbackGame,
    'pay': bool,
}

TITLE.__type_table__ = {
    'url': str,
    'forward_text': str,
    'bot_username': str,
    'request_write_access': bool,
}

CallbackQuery.__type_table__ = {
    'id': str,
    'from': User,
    'message': Message,
    'inline_message_id': str,
    'chat_instance': str,
    'data': str,
    'game_short_name': str,
}

ForceReply.__type_table__ = {
    'force_reply': bool,
    'input_field_placeholder': str,
    'selective': bool,
}

ChatPhoto.__type_table__ = {
    'small_file_id': str,
    'small_file_unique_id': str,
    'big_file_id': str,
    'big_file_unique_id': str,
}

ChatInviteLink.__type_table__ = {
    'invite_link': str,
    'creator': User,
    'creates_join_request': bool,
    'is_primary': bool,
    'is_revoked': bool,
    'name': str,
    'expire_date': int,
    'member_limit': int,
    'pending_join_request_count': int,
}

ChatMemberOwner.__type_table__ = {
    'status': str,
    'user': User,
    'is_anonymous': bool,
    'custom_title': str,
}

ChatMemberAdministrator.__type_table__ = {
    'status': str,
    'user': User,
    'can_be_edited': bool,
    'is_anonymous': bool,
    'can_manage_chat': bool,
    'can_delete_messages': bool,
    'can_manage_voice_chats': bool,
    'can_restrict_members': bool,
    'can_promote_members': bool,
    'can_change_info': bool,
    'can_invite_users': bool,
    'can_post_messages': bool,
    'can_edit_messages': bool,
    'can_pin_messages': bool,
    'custom_title': str,
}

ChatMemberMember.__type_table__ = {
    'status': str,
    'user': User,
}

ChatMemberRestricted.__type_table__ = {
    'status': str,
    'user': User,
    'is_member': bool,
    'can_change_info': bool,
    'can_invite_users': bool,
    'can_pin_messages': bool,
    'can_send_messages': bool,
    'can_send_media_messages': bool,
    'can_send_polls': bool,
    'can_send_other_messages': bool,
    'can_add_web_page_previews': bool,
    'until_date': int,
}

ChatMemberLeft.__type_table__ = {
    'status': str,
    'user': User,
}

ChatMemberBanned.__type_table__ = {
    'status': str,
    'user': User,
    'until_date': int,
}

ChatMemberUpdated.__type_table__ = {
    'chat': Chat,
    'from': User,
    'date': int,
    'old_chat_member': ChatMember,
    'new_chat_member': ChatMember,
    'invite_link': ChatInviteLink,
}

ChatJoinRequest.__type_table__ = {
    'chat': Chat,
    'from': User,
    'date': int,
    'bio': str,
    'invite_link': ChatInviteLink,
}

ChatPermissions.__type_table__ = {
    'can_send_messages': bool,
    'can_send_media_messages': bool,
    'can_send_polls': bool,
    'can_send_other_messages': bool,
    'can_add_web_page_previews': bool,
    'can_change_info': bool,
    'can_invite_users': bool,
    'can_pin_messages': bool,
}

ChatLocation.__type_table__ = {
    'location': Location,
    'address': str,
}

BotCommand.__type_table__ = {
    'command': str,
    'description': str,
}

BotCommandScopeDefault.__type_table__ = {
    'type': str,
}

BotCommandScopeAllPrivateChats.__type_table__ = {
    'type': str,
}

BotCommandScopeAllGroupChats.__type_table__ = {
    'type': str,
}

BotCommandScopeAllChatAdministrators.__type_table__ = {
    'type': str,
}

BotCommandScopeChat.__type_table__ = {
    'type': str,
    'chat_id': [int, str],
}

BotCommandScopeChatAdministrators.__type_table__ = {
    'type': str,
    'chat_id': [int, str],
}

BotCommandScopeChatMember.__type_table__ = {
    'type': str,
    'chat_id': [int, str],
    'user_id': int,
}

ResponseParameters.__type_table__ = {
    'migrate_to_chat_id': int,
    'retry_after': int,
}

InputMediaPhoto.__type_table__ = {
    'type': str,
    'media': str,
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
}

InputMediaVideo.__type_table__ = {
    'type': str,
    'media': str,
    'thumb': [InputFile, str],
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'width': int,
    'height': int,
    'duration': int,
    'supports_streaming': bool,
}

InputMediaAnimation.__type_table__ = {
    'type': str,
    'media': str,
    'thumb': [InputFile, str],
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'width': int,
    'height': int,
    'duration': int,
}

InputMediaAudio.__type_table__ = {
    'type': str,
    'media': str,
    'thumb': [InputFile, str],
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'duration': int,
    'performer': str,
    'title': str,
}

InputMediaDocument.__type_table__ = {
    'type': str,
    'media': str,
    'thumb': [InputFile, str],
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'disable_content_type_detection': bool,
}

Sticker.__type_table__ = {
    'file_id': str,
    'file_unique_id': str,
    'width': int,
    'height': int,
    'is_animated': bool,
    'is_video': bool,
    'thumb': PhotoSize,
    'emoji': str,
    'set_name': str,
    'mask_position': MaskPosition,
    'file_size': int,
}

StickerSet.__type_table__ = {
    'name': str,
    'title': str,
    'is_animated': bool,
    'is_video': bool,
    'contains_masks': bool,
    'stickers': [Sticker],
    'thumb': PhotoSize,
}

MaskPosition.__type_table__ = {
    'point': str,
    'x_shift': float,
    'y_shift': float,
    'scale': float,
}

InlineQuery.__type_table__ = {
    'id': str,
    'from': User,
    'query': str,
    'offset': str,
    'chat_type': str,
    'location': Location,
}

InlineQueryResultArticle.__type_table__ = {
    'type': str,
    'id': str,
    'title': str,
    'input_message_content': InputMessageContent,
    'reply_markup': InlineKeyboardMarkup,
    'url': str,
    'hide_url': bool,
    'description': str,
    'thumb_url': str,
    'thumb_width': int,
    'thumb_height': int,
}

InlineQueryResultPhoto.__type_table__ = {
    'type': str,
    'id': str,
    'photo_url': str,
    'thumb_url': str,
    'photo_width': int,
    'photo_height': int,
    'title': str,
    'description': str,
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
}

InlineQueryResultGif.__type_table__ = {
    'type': str,
    'id': str,
    'gif_url': str,
    'gif_width': int,
    'gif_height': int,
    'gif_duration': int,
    'thumb_url': str,
    'thumb_mime_type': str,
    'title': str,
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
}

InlineQueryResultMpeg4Gif.__type_table__ = {
    'type': str,
    'id': str,
    'mpeg4_url': str,
    'mpeg4_width': int,
    'mpeg4_height': int,
    'mpeg4_duration': int,
    'thumb_url': str,
    'thumb_mime_type': str,
    'title': str,
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
}

InlineQueryResultVideo.__type_table__ = {
    'type': str,
    'id': str,
    'video_url': str,
    'mime_type': str,
    'thumb_url': str,
    'title': str,
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'video_width': int,
    'video_height': int,
    'video_duration': int,
    'description': str,
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
}

InlineQueryResultAudio.__type_table__ = {
    'type': str,
    'id': str,
    'audio_url': str,
    'title': str,
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'performer': str,
    'audio_duration': int,
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
}

InlineQueryResultVoice.__type_table__ = {
    'type': str,
    'id': str,
    'voice_url': str,
    'title': str,
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'voice_duration': int,
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
}

InlineQueryResultDocument.__type_table__ = {
    'type': str,
    'id': str,
    'title': str,
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'document_url': str,
    'mime_type': str,
    'description': str,
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
    'thumb_url': str,
    'thumb_width': int,
    'thumb_height': int,
}

InlineQueryResultLocation.__type_table__ = {
    'type': str,
    'id': str,
    'latitude': float,
    'longitude': float,
    'title': str,
    'horizontal_accuracy': float,
    'live_period': int,
    'heading': int,
    'proximity_alert_radius': int,
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
    'thumb_url': str,
    'thumb_width': int,
    'thumb_height': int,
}

InlineQueryResultVenue.__type_table__ = {
    'type': str,
    'id': str,
    'latitude': float,
    'longitude': float,
    'title': str,
    'address': str,
    'foursquare_id': str,
    'foursquare_type': str,
    'google_place_id': str,
    'google_place_type': str,
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
    'thumb_url': str,
    'thumb_width': int,
    'thumb_height': int,
}

InlineQueryResultContact.__type_table__ = {
    'type': str,
    'id': str,
    'phone_number': str,
    'first_name': str,
    'last_name': str,
    'vcard': str,
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
    'thumb_url': str,
    'thumb_width': int,
    'thumb_height': int,
}

InlineQueryResultGame.__type_table__ = {
    'type': str,
    'id': str,
    'game_short_name': str,
    'reply_markup': InlineKeyboardMarkup,
}

InlineQueryResultCachedPhoto.__type_table__ = {
    'type': str,
    'id': str,
    'photo_file_id': str,
    'title': str,
    'description': str,
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
}

InlineQueryResultCachedGif.__type_table__ = {
    'type': str,
    'id': str,
    'gif_file_id': str,
    'title': str,
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
}

InlineQueryResultCachedMpeg4Gif.__type_table__ = {
    'type': str,
    'id': str,
    'mpeg4_file_id': str,
    'title': str,
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
}

InlineQueryResultCachedSticker.__type_table__ = {
    'type': str,
    'id': str,
    'sticker_file_id': str,
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
}

InlineQueryResultCachedDocument.__type_table__ = {
    'type': str,
    'id': str,
    'title': str,
    'document_file_id': str,
    'description': str,
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
}

InlineQueryResultCachedVideo.__type_table__ = {
    'type': str,
    'id': str,
    'video_file_id': str,
    'title': str,
    'description': str,
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
}

InlineQueryResultCachedVoice.__type_table__ = {
    'type': str,
    'id': str,
    'voice_file_id': str,
    'title': str,
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
}

InlineQueryResultCachedAudio.__type_table__ = {
    'type': str,
    'id': str,
    'audio_file_id': str,
    'caption': str,
    'parse_mode': str,
    'caption_entities': [MessageEntity],
    'reply_markup': InlineKeyboardMarkup,
    'input_message_content': InputMessageContent,
}

InputTextMessageContent.__type_table__ = {
    'message_text': str,
    'parse_mode': str,
    'entities': [MessageEntity],
    'disable_web_page_preview': bool,
}

InputLocationMessageContent.__type_table__ = {
    'latitude': float,
    'longitude': float,
    'horizontal_accuracy': float,
    'live_period': int,
    'heading': int,
    'proximity_alert_radius': int,
}

InputVenueMessageContent.__type_table__ = {
    'latitude': float,
    'longitude': float,
    'title': str,
    'address': str,
    'foursquare_id': str,
    'foursquare_type': str,
    'google_place_id': str,
    'google_place_type': str,
}

InputContactMessageContent.__type_table__ = {
    'phone_number': str,
    'first_name': str,
    'last_name': str,
    'vcard': str,
}

InputInvoiceMessageContent.__type_table__ = {
    'title': str,
    'description': str,
    'payload': str,
    'provider_token': str,
    'currency': str,
    'prices': [LabeledPrice],
    'max_tip_amount': int,
    'suggested_tip_amounts': [int],
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
}

ChosenInlineResult.__type_table__ = {
    'result_id': str,
    'from': User,
    'location': Location,
    'inline_message_id': str,
    'query': str,
}

LabeledPrice.__type_table__ = {
    'label': str,
    'amount': int,
}

Invoice.__type_table__ = {
    'title': str,
    'description': str,
    'start_parameter': str,
    'currency': str,
    'total_amount': int,
}

ShippingAddress.__type_table__ = {
    'country_code': str,
    'state': str,
    'city': str,
    'street_line1': str,
    'street_line2': str,
    'post_code': str,
}

OrderInfo.__type_table__ = {
    'name': str,
    'phone_number': str,
    'email': str,
    'shipping_address': ShippingAddress,
}

ShippingOption.__type_table__ = {
    'id': str,
    'title': str,
    'prices': [LabeledPrice],
}

SuccessfulPayment.__type_table__ = {
    'currency': str,
    'total_amount': int,
    'invoice_payload': str,
    'shipping_option_id': str,
    'order_info': OrderInfo,
    'telegram_payment_charge_id': str,
    'provider_payment_charge_id': str,
}

ShippingQuery.__type_table__ = {
    'id': str,
    'from': User,
    'invoice_payload': str,
    'shipping_address': ShippingAddress,
}

PreCheckoutQuery.__type_table__ = {
    'id': str,
    'from': User,
    'currency': str,
    'total_amount': int,
    'invoice_payload': str,
    'shipping_option_id': str,
    'order_info': OrderInfo,
}

PassportData.__type_table__ = {
    'data': [EncryptedPassportElement],
    'credentials': EncryptedCredentials,
}

PassportFile.__type_table__ = {
    'file_id': str,
    'file_unique_id': str,
    'file_size': int,
    'file_date': int,
}

EncryptedPassportElement.__type_table__ = {
    'type': str,
    'data': str,
    'phone_number': str,
    'email': str,
    'files': [PassportFile],
    'front_side': PassportFile,
    'reverse_side': PassportFile,
    'selfie': PassportFile,
    'translation': [PassportFile],
    'hash': str,
}

EncryptedCredentials.__type_table__ = {
    'data': str,
    'hash': str,
    'secret': str,
}

PassportElementErrorDataField.__type_table__ = {
    'source': str,
    'type': str,
    'field_name': str,
    'data_hash': str,
    'message': str,
}

PassportElementErrorFrontSide.__type_table__ = {
    'source': str,
    'type': str,
    'file_hash': str,
    'message': str,
}

PassportElementErrorReverseSide.__type_table__ = {
    'source': str,
    'type': str,
    'file_hash': str,
    'message': str,
}

PassportElementErrorSelfie.__type_table__ = {
    'source': str,
    'type': str,
    'file_hash': str,
    'message': str,
}

PassportElementErrorFile.__type_table__ = {
    'source': str,
    'type': str,
    'file_hash': str,
    'message': str,
}

PassportElementErrorFiles.__type_table__ = {
    'source': str,
    'type': str,
    'file_hashes': [str],
    'message': str,
}

PassportElementErrorTranslationFile.__type_table__ = {
    'source': str,
    'type': str,
    'file_hash': str,
    'message': str,
}

PassportElementErrorTranslationFiles.__type_table__ = {
    'source': str,
    'type': str,
    'file_hashes': [str],
    'message': str,
}

PassportElementErrorUnspecified.__type_table__ = {
    'source': str,
    'type': str,
    'element_hash': str,
    'message': str,
}

Game.__type_table__ = {
    'title': str,
    'description': str,
    'photo': [PhotoSize],
    'text': str,
    'text_entities': [MessageEntity],
    'animation': Animation,
}

GameHighScore.__type_table__ = {
    'position': int,
    'user': User,
    'score': int,
}
