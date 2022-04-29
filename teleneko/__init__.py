from teleneko.globe import bot_mainloop
from teleneko.globe import event, timer, handle, event_filter
from teleneko.globe import set_logger, set_debug, terminal, find_bot_by_name

from teleneko.bot import bot
from teleneko.tgapi import basic_bot

from teleneko.tgtypes import *

set_debug(False)
bot_mainloop.on = True
