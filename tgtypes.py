from strings import str_type
from strings import str_val

class tgtype:
    
    __type__table__ = {}
    
    def __init__(self, json_info={}):
        for x, y in json_info.items():
            _type = self.__type__table__[x]
            if _type == None:
                raise Exception( "No such param" )
            if type(y) == type(list):
                _type(y)
            if type(_type) == type(type):
                self.__dict__[x] = _type(y)
                continue
            for t in _type:
                if isinstance(y, t):
                    self.__dict__[x] = t(y)
                    break
    
    def __tree__(self, offset):
        s = "\033[37m"
        for x, y in self.__dict__.items():
            tail = "├─ " if x != list(self.__dict__.keys())[-1] else "└─ "
            addi = "│  " if x != list(self.__dict__.keys())[-1] else "   "
            if isinstance( y, list ):
                s += offset + tail + ( "%s %s:\n" % (str_type(y), x) )
                for p in range(len(y)):
                    tail = "├─ " if p < len(y) - 1 else "└─ "
                    addj = "│  " if p < len(y) - 1 else "   "
                    if isinstance( y[p], tgtype ):
                        s += addi + offset + tail + ( "%s[%d] -> %s :\n%s" % ( x, p, str_type(y[p]), y[p].__tree__( offset + addi + addj ) ) )
                    else:
                        s += addi + offset + tail + ( "%s[%d] -> %s : %s\n" % ( x, p, str_type(y[p]), str_val(y[p]) ) )
            elif isinstance( y, tgtype ):
                s += offset + tail + ( "%s %s :\n%s" % ( str_type(y), x, y.__tree__( offset + addi ) ) )
            else:
                s += offset + tail + ( "%s %s : %s\n" % ( str_type(y), x, str_val(y) ) )
        return s
    
    def __str__(self):
        return str_type(self) + "\n" + self.__tree__("") + "\033[0m"

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
class BotCommandScopeDefault(tgtype): pass
class BotCommandScopeAllPrivateChats(tgtype): pass
class BotCommandScopeAllGroupChats(tgtype): pass
class BotCommandScopeAllChatAdministrators(tgtype): pass
class BotCommandScopeChat(tgtype): pass
class BotCommandScopeChatAdministrators(tgtype): pass
class BotCommandScopeChatMember(tgtype): pass
class ResponseParameters(tgtype): pass
class InputMediaPhoto(tgtype): pass
class InputMediaVideo(tgtype): pass
class InputMediaAnimation(tgtype): pass
class InputMediaAudio(tgtype): pass
class InputMediaDocument(tgtype): pass
class Sticker(tgtype): pass
class StickerSet(tgtype): pass
class MaskPosition(tgtype): pass
class InlineQuery(tgtype): pass
class InlineQueryResultArticle(tgtype): pass
class InlineQueryResultPhoto(tgtype): pass
class InlineQueryResultGif(tgtype): pass
class InlineQueryResultMpeg4Gif(tgtype): pass
class InlineQueryResultVideo(tgtype): pass
class InlineQueryResultAudio(tgtype): pass
class InlineQueryResultVoice(tgtype): pass
class InlineQueryResultDocument(tgtype): pass
class InlineQueryResultLocation(tgtype): pass
class InlineQueryResultVenue(tgtype): pass
class InlineQueryResultContact(tgtype): pass
class InlineQueryResultGame(tgtype): pass
class InlineQueryResultCachedPhoto(tgtype): pass
class InlineQueryResultCachedGif(tgtype): pass
class InlineQueryResultCachedMpeg4Gif(tgtype): pass
class InlineQueryResultCachedSticker(tgtype): pass
class InlineQueryResultCachedDocument(tgtype): pass
class InlineQueryResultCachedVideo(tgtype): pass
class InlineQueryResultCachedVoice(tgtype): pass
class InlineQueryResultCachedAudio(tgtype): pass
class InputTextMessageContent(tgtype): pass
class InputLocationMessageContent(tgtype): pass
class InputVenueMessageContent(tgtype): pass
class InputContactMessageContent(tgtype): pass
class InputInvoiceMessageContent(tgtype): pass
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
class PassportElementErrorDataField(tgtype): pass
class PassportElementErrorFrontSide(tgtype): pass
class PassportElementErrorReverseSide(tgtype): pass
class PassportElementErrorSelfie(tgtype): pass
class PassportElementErrorFile(tgtype): pass
class PassportElementErrorFiles(tgtype): pass
class PassportElementErrorTranslationFile(tgtype): pass
class PassportElementErrorTranslationFiles(tgtype): pass
class PassportElementErrorUnspecified(tgtype): pass
class Game(tgtype): pass
class GameHighScore(tgtype): pass
class VoiceChatStarted(tgtype): pass
class VoiceChatEnded(tgtype): pass
class LoginUrl(tgtype): pass
class CallbackGame(tgtype): pass
class InputFile(tgtype): pass
class InputMessageContent(tgtype): pass

Update.__type__table__ = {
                       'update_id' : int,
                         'message' : Message,
                  'edited_message' : Message,
                    'channel_post' : Message,
             'edited_channel_post' : Message,
                    'inline_query' : InlineQuery,
            'chosen_inline_result' : ChosenInlineResult,
                  'callback_query' : CallbackQuery,
                  'shipping_query' : ShippingQuery,
              'pre_checkout_query' : PreCheckoutQuery,
                            'poll' : Poll,
                     'poll_answer' : PollAnswer,
                  'my_chat_member' : ChatMemberUpdated,
                     'chat_member' : ChatMemberUpdated,
               'chat_join_request' : ChatJoinRequest,
}

WebhookInfo.__type__table__ = {
                             'url' : str,
          'has_custom_certificate' : bool,
            'pending_update_count' : int,
                      'ip_address' : str,
                 'last_error_date' : int,
              'last_error_message' : str,
                 'max_connections' : int,
                 'allowed_updates' : list,
}

User.__type__table__ = {
                              'id' : int,
                          'is_bot' : bool,
                      'first_name' : str,
                       'last_name' : str,
                        'username' : str,
                   'language_code' : str,
                 'can_join_groups' : bool,
     'can_read_all_group_messages' : bool,
         'supports_inline_queries' : bool,
}

Chat.__type__table__ = {
                              'id' : int,
                            'type' : str,
                           'title' : str,
                        'username' : str,
                      'first_name' : str,
                       'last_name' : str,
                           'photo' : ChatPhoto,
                             'bio' : str,
            'has_private_forwards' : bool,
                     'description' : str,
                     'invite_link' : str,
                  'pinned_message' : Message,
                     'permissions' : ChatPermissions,
                 'slow_mode_delay' : int,
        'message_auto_delete_time' : int,
           'has_protected_content' : bool,
                'sticker_set_name' : str,
             'can_set_sticker_set' : bool,
                  'linked_chat_id' : int,
                        'location' : ChatLocation,
}

Message.__type__table__ = {
                      'message_id' : int,
                            'from' : User,
                     'sender_chat' : Chat,
                            'date' : int,
                            'chat' : Chat,
                    'forward_from' : User,
               'forward_from_chat' : Chat,
         'forward_from_message_id' : int,
               'forward_signature' : str,
             'forward_sender_name' : str,
                    'forward_date' : int,
            'is_automatic_forward' : bool,
                'reply_to_message' : Message,
                         'via_bot' : User,
                       'edit_date' : int,
           'has_protected_content' : bool,
                  'media_group_id' : str,
                'author_signature' : str,
                            'text' : str,
                        'entities' : list,
                       'animation' : Animation,
                           'audio' : Audio,
                        'document' : Document,
                           'photo' : list,
                         'sticker' : Sticker,
                           'video' : Video,
                      'video_note' : VideoNote,
                           'voice' : Voice,
                         'caption' : str,
                'caption_entities' : list,
                         'contact' : Contact,
                            'dice' : Dice,
                            'game' : Game,
                            'poll' : Poll,
                           'venue' : Venue,
                        'location' : Location,
                'new_chat_members' : list,
                'left_chat_member' : User,
                  'new_chat_title' : str,
                  'new_chat_photo' : list,
               'delete_chat_photo' : bool,
              'group_chat_created' : bool,
         'supergroup_chat_created' : bool,
            'channel_chat_created' : bool,
'message_auto_delete_timer_changed' : MessageAutoDeleteTimerChanged,
              'migrate_to_chat_id' : int,
            'migrate_from_chat_id' : int,
                  'pinned_message' : Message,
                         'invoice' : Invoice,
              'successful_payment' : SuccessfulPayment,
               'connected_website' : str,
                   'passport_data' : PassportData,
       'proximity_alert_triggered' : ProximityAlertTriggered,
            'voice_chat_scheduled' : VoiceChatScheduled,
              'voice_chat_started' : VoiceChatStarted,
                'voice_chat_ended' : VoiceChatEnded,
 'voice_chat_participants_invited' : VoiceChatParticipantsInvited,
                    'reply_markup' : InlineKeyboardMarkup,
}

MessageId.__type__table__ = {
                      'message_id' : int,
}

MessageEntity.__type__table__ = {
                            'type' : str,
                          'offset' : int,
                          'length' : int,
                             'url' : str,
                            'user' : User,
                        'language' : str,
}

PhotoSize.__type__table__ = {
                         'file_id' : str,
                  'file_unique_id' : str,
                           'width' : int,
                          'height' : int,
                       'file_size' : int,
}

Animation.__type__table__ = {
                         'file_id' : str,
                  'file_unique_id' : str,
                           'width' : int,
                          'height' : int,
                        'duration' : int,
                           'thumb' : PhotoSize,
                       'file_name' : str,
                       'mime_type' : str,
                       'file_size' : int,
}

Audio.__type__table__ = {
                         'file_id' : str,
                  'file_unique_id' : str,
                        'duration' : int,
                       'performer' : str,
                           'title' : str,
                       'file_name' : str,
                       'mime_type' : str,
                       'file_size' : int,
                           'thumb' : PhotoSize,
}

Document.__type__table__ = {
                         'file_id' : str,
                  'file_unique_id' : str,
                           'thumb' : PhotoSize,
                       'file_name' : str,
                       'mime_type' : str,
                       'file_size' : int,
}

Video.__type__table__ = {
                         'file_id' : str,
                  'file_unique_id' : str,
                           'width' : int,
                          'height' : int,
                        'duration' : int,
                           'thumb' : PhotoSize,
                       'file_name' : str,
                       'mime_type' : str,
                       'file_size' : int,
}

VideoNote.__type__table__ = {
                         'file_id' : str,
                  'file_unique_id' : str,
                          'length' : int,
                        'duration' : int,
                           'thumb' : PhotoSize,
                       'file_size' : int,
}

Voice.__type__table__ = {
                         'file_id' : str,
                  'file_unique_id' : str,
                        'duration' : int,
                       'mime_type' : str,
                       'file_size' : int,
}

Contact.__type__table__ = {
                    'phone_number' : str,
                      'first_name' : str,
                       'last_name' : str,
                         'user_id' : int,
                           'vcard' : str,
}

Dice.__type__table__ = {
                           'emoji' : str,
                           'value' : int,
}

PollOption.__type__table__ = {
                            'text' : str,
                     'voter_count' : int,
}

PollAnswer.__type__table__ = {
                         'poll_id' : str,
                            'user' : User,
                      'option_ids' : list,
}

Poll.__type__table__ = {
                              'id' : str,
                        'question' : str,
                         'options' : list,
               'total_voter_count' : int,
                       'is_closed' : bool,
                    'is_anonymous' : bool,
                            'type' : str,
         'allows_multiple_answers' : bool,
               'correct_option_id' : int,
                     'explanation' : str,
            'explanation_entities' : list,
                     'open_period' : int,
                      'close_date' : int,
}

Location.__type__table__ = {
                       'longitude' : float,
                        'latitude' : float,
             'horizontal_accuracy' : float,
                     'live_period' : int,
                         'heading' : int,
          'proximity_alert_radius' : int,
}

Venue.__type__table__ = {
                        'location' : Location,
                           'title' : str,
                         'address' : str,
                   'foursquare_id' : str,
                 'foursquare_type' : str,
                 'google_place_id' : str,
               'google_place_type' : str,
}

ProximityAlertTriggered.__type__table__ = {
                        'traveler' : User,
                         'watcher' : User,
                        'distance' : int,
}

MessageAutoDeleteTimerChanged.__type__table__ = {
        'message_auto_delete_time' : int,
}

VoiceChatScheduled.__type__table__ = {
                      'start_date' : int,
}

VoiceChatEnded.__type__table__ = {
                        'duration' : int,
}

VoiceChatParticipantsInvited.__type__table__ = {
                           'users' : list,
}

UserProfilePhotos.__type__table__ = {
                     'total_count' : int,
                          'photos' : list,
}

File.__type__table__ = {
                         'file_id' : str,
                  'file_unique_id' : str,
                       'file_size' : int,
                       'file_path' : str,
}

ReplyKeyboardMarkup.__type__table__ = {
                        'keyboard' : list,
                 'resize_keyboard' : bool,
               'one_time_keyboard' : bool,
         'input_field_placeholder' : str,
                       'selective' : bool,
}

KeyboardButton.__type__table__ = {
                            'text' : str,
                 'request_contact' : bool,
                'request_location' : bool,
                    'request_poll' : KeyboardButtonPollType,
}

KeyboardButtonPollType.__type__table__ = {
                            'type' : str,
}

ReplyKeyboardRemove.__type__table__ = {
                 'remove_keyboard' : bool,
                       'selective' : bool,
}

InlineKeyboardMarkup.__type__table__ = {
                 'inline_keyboard' : list,
}

InlineKeyboardButton.__type__table__ = {
                            'text' : str,
                             'url' : str,
                       'login_url' : LoginUrl,
                   'callback_data' : str,
             'switch_inline_query' : str,
'switch_inline_query_current_chat' : str,
                   'callback_game' : CallbackGame,
                             'pay' : bool,
}

TITLE.__type__table__ = {
                             'url' : str,
                    'forward_text' : str,
                    'bot_username' : str,
            'request_write_access' : bool,
}

CallbackQuery.__type__table__ = {
                              'id' : str,
                            'from' : User,
                         'message' : Message,
               'inline_message_id' : str,
                   'chat_instance' : str,
                            'data' : str,
                 'game_short_name' : str,
}

ForceReply.__type__table__ = {
                     'force_reply' : bool,
         'input_field_placeholder' : str,
                       'selective' : bool,
}

ChatPhoto.__type__table__ = {
                   'small_file_id' : str,
            'small_file_unique_id' : str,
                     'big_file_id' : str,
              'big_file_unique_id' : str,
}

ChatInviteLink.__type__table__ = {
                     'invite_link' : str,
                         'creator' : User,
            'creates_join_request' : bool,
                      'is_primary' : bool,
                      'is_revoked' : bool,
                            'name' : str,
                     'expire_date' : int,
                    'member_limit' : int,
      'pending_join_request_count' : int,
}

ChatMemberOwner.__type__table__ = {
                          'status' : str,
                            'user' : User,
                    'is_anonymous' : bool,
                    'custom_title' : str,
}

ChatMemberAdministrator.__type__table__ = {
                          'status' : str,
                            'user' : User,
                   'can_be_edited' : bool,
                    'is_anonymous' : bool,
                 'can_manage_chat' : bool,
             'can_delete_messages' : bool,
          'can_manage_voice_chats' : bool,
            'can_restrict_members' : bool,
             'can_promote_members' : bool,
                 'can_change_info' : bool,
                'can_invite_users' : bool,
               'can_post_messages' : bool,
               'can_edit_messages' : bool,
                'can_pin_messages' : bool,
                    'custom_title' : str,
}

ChatMemberMember.__type__table__ = {
                          'status' : str,
                            'user' : User,
}

ChatMemberRestricted.__type__table__ = {
                          'status' : str,
                            'user' : User,
                       'is_member' : bool,
                 'can_change_info' : bool,
                'can_invite_users' : bool,
                'can_pin_messages' : bool,
               'can_send_messages' : bool,
         'can_send_media_messages' : bool,
                  'can_send_polls' : bool,
         'can_send_other_messages' : bool,
       'can_add_web_page_previews' : bool,
                      'until_date' : int,
}

ChatMemberLeft.__type__table__ = {
                          'status' : str,
                            'user' : User,
}

ChatMemberBanned.__type__table__ = {
                          'status' : str,
                            'user' : User,
                      'until_date' : int,
}

ChatMemberUpdated.__type__table__ = {
                            'chat' : Chat,
                            'from' : User,
                            'date' : int,
                 'old_chat_member' : ChatMember,
                 'new_chat_member' : ChatMember,
                     'invite_link' : ChatInviteLink,
}

ChatJoinRequest.__type__table__ = {
                            'chat' : Chat,
                            'from' : User,
                            'date' : int,
                             'bio' : str,
                     'invite_link' : ChatInviteLink,
}

ChatPermissions.__type__table__ = {
               'can_send_messages' : bool,
         'can_send_media_messages' : bool,
                  'can_send_polls' : bool,
         'can_send_other_messages' : bool,
       'can_add_web_page_previews' : bool,
                 'can_change_info' : bool,
                'can_invite_users' : bool,
                'can_pin_messages' : bool,
}

ChatLocation.__type__table__ = {
                        'location' : Location,
                         'address' : str,
}

BotCommand.__type__table__ = {
                         'command' : str,
                     'description' : str,
}

BotCommandScopeDefault.__type__table__ = {
                            'type' : str,
}

BotCommandScopeAllPrivateChats.__type__table__ = {
                            'type' : str,
}

BotCommandScopeAllGroupChats.__type__table__ = {
                            'type' : str,
}

BotCommandScopeAllChatAdministrators.__type__table__ = {
                            'type' : str,
}

BotCommandScopeChat.__type__table__ = {
                            'type' : str,
                         'chat_id' : [int, str],
}

BotCommandScopeChatAdministrators.__type__table__ = {
                            'type' : str,
                         'chat_id' : [int, str],
}

BotCommandScopeChatMember.__type__table__ = {
                            'type' : str,
                         'chat_id' : [int, str],
                         'user_id' : int,
}

ResponseParameters.__type__table__ = {
              'migrate_to_chat_id' : int,
                     'retry_after' : int,
}

InputMediaPhoto.__type__table__ = {
                            'type' : str,
                           'media' : str,
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
}

InputMediaVideo.__type__table__ = {
                            'type' : str,
                           'media' : str,
                           'thumb' : [InputFile, str],
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
                           'width' : int,
                          'height' : int,
                        'duration' : int,
              'supports_streaming' : bool,
}

InputMediaAnimation.__type__table__ = {
                            'type' : str,
                           'media' : str,
                           'thumb' : [InputFile, str],
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
                           'width' : int,
                          'height' : int,
                        'duration' : int,
}

InputMediaAudio.__type__table__ = {
                            'type' : str,
                           'media' : str,
                           'thumb' : [InputFile, str],
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
                        'duration' : int,
                       'performer' : str,
                           'title' : str,
}

InputMediaDocument.__type__table__ = {
                            'type' : str,
                           'media' : str,
                           'thumb' : [InputFile, str],
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
  'disable_content_type_detection' : bool,
}

Sticker.__type__table__ = {
                         'file_id' : str,
                  'file_unique_id' : str,
                           'width' : int,
                          'height' : int,
                     'is_animated' : bool,
                        'is_video' : bool,
                           'thumb' : PhotoSize,
                           'emoji' : str,
                        'set_name' : str,
                   'mask_position' : MaskPosition,
                       'file_size' : int,
}

StickerSet.__type__table__ = {
                            'name' : str,
                           'title' : str,
                     'is_animated' : bool,
                        'is_video' : bool,
                  'contains_masks' : bool,
                        'stickers' : list,
                           'thumb' : PhotoSize,
}

MaskPosition.__type__table__ = {
                           'point' : str,
                         'x_shift' : float,
                         'y_shift' : float,
                           'scale' : float,
}

InlineQuery.__type__table__ = {
                              'id' : str,
                            'from' : User,
                           'query' : str,
                          'offset' : str,
                       'chat_type' : str,
                        'location' : Location,
}

InlineQueryResultArticle.__type__table__ = {
                            'type' : str,
                              'id' : str,
                           'title' : str,
           'input_message_content' : InputMessageContent,
                    'reply_markup' : InlineKeyboardMarkup,
                             'url' : str,
                        'hide_url' : bool,
                     'description' : str,
                       'thumb_url' : str,
                     'thumb_width' : int,
                    'thumb_height' : int,
}

InlineQueryResultPhoto.__type__table__ = {
                            'type' : str,
                              'id' : str,
                       'photo_url' : str,
                       'thumb_url' : str,
                     'photo_width' : int,
                    'photo_height' : int,
                           'title' : str,
                     'description' : str,
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
}

InlineQueryResultGif.__type__table__ = {
                            'type' : str,
                              'id' : str,
                         'gif_url' : str,
                       'gif_width' : int,
                      'gif_height' : int,
                    'gif_duration' : int,
                       'thumb_url' : str,
                 'thumb_mime_type' : str,
                           'title' : str,
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
}

InlineQueryResultMpeg4Gif.__type__table__ = {
                            'type' : str,
                              'id' : str,
                       'mpeg4_url' : str,
                     'mpeg4_width' : int,
                    'mpeg4_height' : int,
                  'mpeg4_duration' : int,
                       'thumb_url' : str,
                 'thumb_mime_type' : str,
                           'title' : str,
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
}

InlineQueryResultVideo.__type__table__ = {
                            'type' : str,
                              'id' : str,
                       'video_url' : str,
                       'mime_type' : str,
                       'thumb_url' : str,
                           'title' : str,
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
                     'video_width' : int,
                    'video_height' : int,
                  'video_duration' : int,
                     'description' : str,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
}

InlineQueryResultAudio.__type__table__ = {
                            'type' : str,
                              'id' : str,
                       'audio_url' : str,
                           'title' : str,
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
                       'performer' : str,
                  'audio_duration' : int,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
}

InlineQueryResultVoice.__type__table__ = {
                            'type' : str,
                              'id' : str,
                       'voice_url' : str,
                           'title' : str,
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
                  'voice_duration' : int,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
}

InlineQueryResultDocument.__type__table__ = {
                            'type' : str,
                              'id' : str,
                           'title' : str,
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
                    'document_url' : str,
                       'mime_type' : str,
                     'description' : str,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
                       'thumb_url' : str,
                     'thumb_width' : int,
                    'thumb_height' : int,
}

InlineQueryResultLocation.__type__table__ = {
                            'type' : str,
                              'id' : str,
                        'latitude' : float,
                       'longitude' : float,
                           'title' : str,
             'horizontal_accuracy' : float,
                     'live_period' : int,
                         'heading' : int,
          'proximity_alert_radius' : int,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
                       'thumb_url' : str,
                     'thumb_width' : int,
                    'thumb_height' : int,
}

InlineQueryResultVenue.__type__table__ = {
                            'type' : str,
                              'id' : str,
                        'latitude' : float,
                       'longitude' : float,
                           'title' : str,
                         'address' : str,
                   'foursquare_id' : str,
                 'foursquare_type' : str,
                 'google_place_id' : str,
               'google_place_type' : str,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
                       'thumb_url' : str,
                     'thumb_width' : int,
                    'thumb_height' : int,
}

InlineQueryResultContact.__type__table__ = {
                            'type' : str,
                              'id' : str,
                    'phone_number' : str,
                      'first_name' : str,
                       'last_name' : str,
                           'vcard' : str,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
                       'thumb_url' : str,
                     'thumb_width' : int,
                    'thumb_height' : int,
}

InlineQueryResultGame.__type__table__ = {
                            'type' : str,
                              'id' : str,
                 'game_short_name' : str,
                    'reply_markup' : InlineKeyboardMarkup,
}

InlineQueryResultCachedPhoto.__type__table__ = {
                            'type' : str,
                              'id' : str,
                   'photo_file_id' : str,
                           'title' : str,
                     'description' : str,
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
}

InlineQueryResultCachedGif.__type__table__ = {
                            'type' : str,
                              'id' : str,
                     'gif_file_id' : str,
                           'title' : str,
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
}

InlineQueryResultCachedMpeg4Gif.__type__table__ = {
                            'type' : str,
                              'id' : str,
                   'mpeg4_file_id' : str,
                           'title' : str,
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
}

InlineQueryResultCachedSticker.__type__table__ = {
                            'type' : str,
                              'id' : str,
                 'sticker_file_id' : str,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
}

InlineQueryResultCachedDocument.__type__table__ = {
                            'type' : str,
                              'id' : str,
                           'title' : str,
                'document_file_id' : str,
                     'description' : str,
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
}

InlineQueryResultCachedVideo.__type__table__ = {
                            'type' : str,
                              'id' : str,
                   'video_file_id' : str,
                           'title' : str,
                     'description' : str,
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
}

InlineQueryResultCachedVoice.__type__table__ = {
                            'type' : str,
                              'id' : str,
                   'voice_file_id' : str,
                           'title' : str,
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
}

InlineQueryResultCachedAudio.__type__table__ = {
                            'type' : str,
                              'id' : str,
                   'audio_file_id' : str,
                         'caption' : str,
                      'parse_mode' : str,
                'caption_entities' : list,
                    'reply_markup' : InlineKeyboardMarkup,
           'input_message_content' : InputMessageContent,
}

InputTextMessageContent.__type__table__ = {
                    'message_text' : str,
                      'parse_mode' : str,
                        'entities' : list,
        'disable_web_page_preview' : bool,
}

InputLocationMessageContent.__type__table__ = {
                        'latitude' : float,
                       'longitude' : float,
             'horizontal_accuracy' : float,
                     'live_period' : int,
                         'heading' : int,
          'proximity_alert_radius' : int,
}

InputVenueMessageContent.__type__table__ = {
                        'latitude' : float,
                       'longitude' : float,
                           'title' : str,
                         'address' : str,
                   'foursquare_id' : str,
                 'foursquare_type' : str,
                 'google_place_id' : str,
               'google_place_type' : str,
}

InputContactMessageContent.__type__table__ = {
                    'phone_number' : str,
                      'first_name' : str,
                       'last_name' : str,
                           'vcard' : str,
}

InputInvoiceMessageContent.__type__table__ = {
                           'title' : str,
                     'description' : str,
                         'payload' : str,
                  'provider_token' : str,
                        'currency' : str,
                          'prices' : list,
                  'max_tip_amount' : int,
           'suggested_tip_amounts' : list,
                   'provider_data' : str,
                       'photo_url' : str,
                      'photo_size' : int,
                     'photo_width' : int,
                    'photo_height' : int,
                       'need_name' : bool,
               'need_phone_number' : bool,
                      'need_email' : bool,
           'need_shipping_address' : bool,
   'send_phone_number_to_provider' : bool,
          'send_email_to_provider' : bool,
                     'is_flexible' : bool,
}

ChosenInlineResult.__type__table__ = {
                       'result_id' : str,
                            'from' : User,
                        'location' : Location,
               'inline_message_id' : str,
                           'query' : str,
}

LabeledPrice.__type__table__ = {
                           'label' : str,
                          'amount' : int,
}

Invoice.__type__table__ = {
                           'title' : str,
                     'description' : str,
                 'start_parameter' : str,
                        'currency' : str,
                    'total_amount' : int,
}

ShippingAddress.__type__table__ = {
                    'country_code' : str,
                           'state' : str,
                            'city' : str,
                    'street_line1' : str,
                    'street_line2' : str,
                       'post_code' : str,
}

OrderInfo.__type__table__ = {
                            'name' : str,
                    'phone_number' : str,
                           'email' : str,
                'shipping_address' : ShippingAddress,
}

ShippingOption.__type__table__ = {
                              'id' : str,
                           'title' : str,
                          'prices' : list,
}

SuccessfulPayment.__type__table__ = {
                        'currency' : str,
                    'total_amount' : int,
                 'invoice_payload' : str,
              'shipping_option_id' : str,
                      'order_info' : OrderInfo,
      'telegram_payment_charge_id' : str,
      'provider_payment_charge_id' : str,
}

ShippingQuery.__type__table__ = {
                              'id' : str,
                            'from' : User,
                 'invoice_payload' : str,
                'shipping_address' : ShippingAddress,
}

PreCheckoutQuery.__type__table__ = {
                              'id' : str,
                            'from' : User,
                        'currency' : str,
                    'total_amount' : int,
                 'invoice_payload' : str,
              'shipping_option_id' : str,
                      'order_info' : OrderInfo,
}

PassportData.__type__table__ = {
                            'data' : list,
                     'credentials' : EncryptedCredentials,
}

PassportFile.__type__table__ = {
                         'file_id' : str,
                  'file_unique_id' : str,
                       'file_size' : int,
                       'file_date' : int,
}

EncryptedPassportElement.__type__table__ = {
                            'type' : str,
                            'data' : str,
                    'phone_number' : str,
                           'email' : str,
                           'files' : list,
                      'front_side' : PassportFile,
                    'reverse_side' : PassportFile,
                          'selfie' : PassportFile,
                     'translation' : list,
                            'hash' : str,
}

EncryptedCredentials.__type__table__ = {
                            'data' : str,
                            'hash' : str,
                          'secret' : str,
}

PassportElementErrorDataField.__type__table__ = {
                          'source' : str,
                            'type' : str,
                      'field_name' : str,
                       'data_hash' : str,
                         'message' : str,
}

PassportElementErrorFrontSide.__type__table__ = {
                          'source' : str,
                            'type' : str,
                       'file_hash' : str,
                         'message' : str,
}

PassportElementErrorReverseSide.__type__table__ = {
                          'source' : str,
                            'type' : str,
                       'file_hash' : str,
                         'message' : str,
}

PassportElementErrorSelfie.__type__table__ = {
                          'source' : str,
                            'type' : str,
                       'file_hash' : str,
                         'message' : str,
}

PassportElementErrorFile.__type__table__ = {
                          'source' : str,
                            'type' : str,
                       'file_hash' : str,
                         'message' : str,
}

PassportElementErrorFiles.__type__table__ = {
                          'source' : str,
                            'type' : str,
                     'file_hashes' : list,
                         'message' : str,
}

PassportElementErrorTranslationFile.__type__table__ = {
                          'source' : str,
                            'type' : str,
                       'file_hash' : str,
                         'message' : str,
}

PassportElementErrorTranslationFiles.__type__table__ = {
                          'source' : str,
                            'type' : str,
                     'file_hashes' : list,
                         'message' : str,
}

PassportElementErrorUnspecified.__type__table__ = {
                          'source' : str,
                            'type' : str,
                    'element_hash' : str,
                         'message' : str,
}

Game.__type__table__ = {
                           'title' : str,
                     'description' : str,
                           'photo' : list,
                            'text' : str,
                   'text_entities' : list,
                       'animation' : Animation,
}

GameHighScore.__type__table__ = {
                        'position' : int,
                            'user' : User,
                           'score' : int,
}
