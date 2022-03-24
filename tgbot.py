import requests
import json

def __post__(url, command, proxy):
    try:
        r = requests.get( url+command, proxies=proxy )
        if r.status_code != 200:
            raise Exception("404 not found")
        return r.content
    except:
        raise Exception("Error")

def post(bot, command):
    return __post__( bot.__getUrl__(), command, bot.__getProxy__() )

class bot:
    def __init__(self, token, proxy=""):
        self.__setToken__(token)
        self.__setProxy__(proxy)
        self.url = "https://api.telegram.org/bot" + token + "/"
        try:
            self.getMe()
        except:
            raise Exception("Can't connect telegram service or wrong token.")

# private functions            
    def __setToken__(self, token):
        self.token = token
    
    def __setProxy__(self, proxy):
        self.proxy = {
            'https':proxy,
            'http':proxy
        }
    
    def __getUrl__(self):
        return self.url
    
    def __getProxy__(self):
        return self.proxy
    
# public functions

    def getMe(self):
        return json.loads( post(self, "getMe") )
    
    # todo
#    def logOut(self):
    
#    def close(self):
    
#    def Formatting_options(self):
    
#    def fowardMessage(self):
    
#    def copyMessage(self):
    
#    def getUserProfilePhotos(self):

   # Send Something
#    def sendMessage(self):
    
#    def sendPhoto(self):
    
#    def sendAudio(self):
    
#    def sendDocument(self):
    
#    def sendVideo(self):
    
#    def sendAnimation(self):
    
#    def sendVoice(self):
    
#    def sendVideoNote(self):
    
#    def sendMediaGroup(self):
    
#    def sendLocation(self):
    
#    def sendVenue(self):
    
#    def sendContact(self):
    
#    def sendPoll(self):
    
#    def sendDice(self):
    
#    def sendChatAction(self):
    
#    def getFile(self):
    
#    def editMessageLiveLocation(self):
    
#    def stopMessageLiveLocation(self):
    
   # Chat Manage
#    def banChatMember(self):
    
#    def unbanChatMember(self):
    
#    def restrictChatMember(self):
    
#    def promoteChatMember(self):
    
#    def setChatAdministratorCustomTitle(self):
    
#    def banChatSenderChat(self):
    
#    def unbanChatSenderChat(self):
    
#    def setChatPermissions(self):
    
#    def exportChatInviteLink(self):
    
#    def createChatInviteLink(self):
    
#    def editChatInviteLink(self):
    
#    def revokeChatInviteLink(self):
    
#    def approveChatJoinRequest(self):
    
#    def declineChatJoinRequest(self):
    
#    def setChatPhoto(self):
    
#    def deleteChatPhoto(self):
    
#    def setChatDescription(self):
    
#    def pinChatMessage(self):
    
#    def unpinChatMessage(self):

#    def unpinAllChatMessages(self):

#    def leaveChat(self):

#    def getChat(self):

#    def getChatAdministrators(self):

#    def getChatMemberCount(self):

#    def setChatStickerSet(self):

#    def deleteChatStickerSet(self):

#    def answerCallbackQuery(self):

#    def setMyCommands(self):

#    def deleteMyCommands(self):

#    def getMyCommands(self):


