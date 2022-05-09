from .globe import bot_mainloop
from .globe import event, timer, handle, event_filter
from .globe import set_logger, set_debug, terminal, find_bot_by_name

from .bot import bot
from .tgapi import basic_bot

from .tgtypes import *
from .extypes import *

set_debug(False)
bot_mainloop.on = True
