import logging

is_debug = True
logger = None


def set_logger(new_logger):
    global logger
    logger = new_logger


from tgbot.bot import bot
from tgbot.tgapi import basic_bot
from tgbot.tgtypes import *
from tgbot.bits.decorators import handle
from tgbot.bits.controller import timer
