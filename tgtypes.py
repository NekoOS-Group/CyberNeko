from strings import str_type

class tgtype:
    
    def __tree__(self, offset):
        s = ""
        for x, y in self.__dict__.items():
            tail = "├─ " if x != list(self.__dict__.keys())[-1] else "└─ "
            addi = "│  " if x != list(self.__dict__.keys())[-1] else "   "
            if isinstance( y, list ):
                s += offset + tail + ( "%s %s:\n" % (str_type(y), x) )
                for p in range(len(y)):
                    tail = "├─ " if p < len(y) - 1 else "└─ "
                    addj = "│  " if p < len(y) - 1 else "   "
                    if isinstance( y[p], tgtype ):
                        s += "│  " + offset + tail + ( "%s[%d] -> %s :\n%s" % ( x, p, str_type(y[p]), y[p].__tree__( offset + addi + addj ) ) )
                    else:
                        s += "│  " + offset + tail + ( "%s[%d] -> %s : %s\n" % ( x, p, str_type(y[p]), y[p] ) )
            elif isinstance( y, tgtype ):
                s += offset + tail + ( "%s %s :\n%s" % ( str_type(y), x, y.__tree__( offset + addi ) ) )
            else:
                s += offset + tail + ( "%s %s : %s\n" % ( str_type(y), x, str(y) ) )
        return s
    
    def __str__(self):
        return str_type(self) + " self\n" + self.__tree__("") + "\033[0m"

#class User:

#class Chat:

#class Update:

#class Message:

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

#class ChatPhoto:

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

