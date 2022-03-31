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

class User(tgtype):
    pass
    
class Chat(tgtype):
    pass
    
class Message(tgtype):
    pass
    
class Update(tgtype):
     pass

#class MessageId:

#class MessageEntity:

#class PhotoSize:

#class Animation:

#class Audio:

#class Document:

#class Video:

#class VideoNote:

#class Voice:

#class Contact:

#class Dice:

#class PollOption:

#class PollAnswer:

#class Poll:

#class Location:

#class Venue:

#class ProximityAlertTrigered:

#class MessageAutoDeleteTimerChanged:

#class VoiceChatScheduled:

#class VoiceChatStarted:

#class VoiceChatEnded:

#class VoiceChatParticipantsInvited:

#class UserProfilePhotos:

#class File:

#class ReplyKeyboardMarkup:

#class KeyboardButton:

#class KeyboardButtonPollType:

#class ReplyKeyboardRemove:

#class InlineKeyboardMarkup:

#class InlineKeyboardButton:

#class LoginUrl:

#class CallbackQuery:

#class ForceReply:

class ChatPhoto(tgtype):
    pass
    
#class ChatInviteLink:

#class ChatMember:

#class ChatMemberOwner:

#class ChatMemberAdministrator:

#class ChatMemberMember:

#class ChatMemberRestricted:

#class ChatMemberLeft:

#class ChatMemberBanned:

#class ChatMemberUpdated:

#class ChatJoinRequest:

#class ChatPermissions:

#class ChatLocation:

#class BotCommand:

#class BotCommandScope:

#class BotCommandScopeAllPrivateChats:

#class BotCommandScopeAllGroupChats:

#class BotCommandScopeAllChatAdministrators:

#class BotCommandScopeChat:

#class BotCommandScopeChatAdministrators:

#class BotCommandScopeChatMember:

#class ResponseParameters:

#class InputMedia:

#class InputMediaPhoto:

#class InputMediaVideo:

#class InputMediaAnimation:

#class InputMediaAudio:

#class InputMediaDocument:

#class InputFile:

User.__type__table__ = {
    'id'                          : int,
    'is_bot'                      : bool,
    'first_name'                  : str,
    'last_name'                   : str,
    'username'                    : str,
    'language_code'               : str,
    'can_join_groups'             : bool,
    'can_read_all_group_messages' : bool,
    'supports_inline_queries'     : bool
}

Chat.__type__table__ = {
    'id'                          : int,
    'type'                        : str,
    'title'                       : str,
    'username'                    : str,
    'first_name'                  : str,
    'last_name'                   : str,
#   'photo'                       : ChatPhoto,
    'bio'                         : str,
    'has_private_forwards'        : bool,
    'description'                 : str,
    'invite_link'                 : str,
    'pinned_message'              : Message,
#   'permissions'                 : ChatPermissions,
    'slow_mode_delay'             : int,
    'message_auto_delete_time'    : int,
    'has_protected_content'       : bool,
    'sticker_set_name'            : str,
    'can_set_sticker_set'         : bool,
    'linked_chat_id'              : int,
#   'location'                    : ChatLocation
}

Message.__type__table__ = {
    'message_id'                  : int,
    'from'                        : User,
    'sender_chat'                 : Chat,
    'date'                        : int,
    'text'                        : str,
    'chat'                        : Chat
    # ...
}

Update.__type__table__ = {
    'update_id'                    : int,
    'message'                      : Message
    # ...
 }
 
ChatPhoto.__type__table__ = {
    'small_file_id'                : str,
    'small_file_unique_id'         : str,
    'big_file_id'                  : str,
    'big_file_unique_id'           : str
}
