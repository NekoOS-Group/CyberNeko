import logging

from tgbot.bits.controller import timer

__all__ = ['bot_debug', 'bot_logger', 'bot_namelist', 'bot_mainloop', 'set_logger', 'log_info', 'log_warn']

bot_debug = True
bot_logger = None
bot_namelist = dict()
bot_mainloop = timer(interval=0.5)


def set_logger(new_logger: logging.Logger):
    global bot_logger
    bot_logger = new_logger


def log_debug(message):
    if isinstance(bot_logger, logging.Logger):
        bot_logger.debug(message)
    else:
        print(f"[Debug]{message}")


def log_info(message):
    if isinstance(bot_logger, logging.Logger):
        bot_logger.info(message)
    else:
        print(f"[Info]{message}")


def log_warn(message):
    if isinstance(bot_logger, logging.Logger):
        bot_logger.warning(message)
    else:
        print(f"[Warn]{message}")
