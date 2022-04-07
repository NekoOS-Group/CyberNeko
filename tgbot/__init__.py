import logging

is_debug = True
logger = None


def set_logger(new_logger):
    global logger
    logger = new_logger


from tgbot.tgapi import bot
from tgbot.tgtypes import *
