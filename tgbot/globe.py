import logging

import tgbot.bits.decorators as decorators
import tgbot.bits.controller as controller
from tgbot.bits.strings import decorating

bot_debug = True
bot_logger = None
bot_namelist = dict()


def set_logger(new_logger: logging.Logger):
    global bot_logger
    bot_logger = new_logger


def log_debug(message, *args, **kwargs):
    if len(args) > 0:
        obj = args[0]
    else:
        obj = None
    if not bot_debug:
        return
    if obj is not None:
        message = f"{repr(obj)} {message}"
    if isinstance(bot_logger, logging.Logger):
        bot_logger.debug(message)
    else:
        print(f"[Debug] {message}")


def log_info(message, *args, **kwargs):
    if len(args) > 0:
        obj = args[0]
    else:
        obj = None
    if obj is not None:
        message = f"{repr(obj)} {message}"
    if isinstance(bot_logger, logging.Logger):
        bot_logger.info(message)
    else:
        print(f"[Info] {message}")


def log_warn(message, *args, **kwargs):
    if len(args) > 0:
        obj = args[0]
    else:
        obj = None
    if obj is not None:
        message = f"{repr(obj)} {message}"
    if isinstance(bot_logger, logging.Logger):
        bot_logger.warning(message)
    else:
        print(f"{decorating('[Warn]', 33)} {message}")


# redefine decorator.py
log_full = decorators.log_full(bot_logger, bot_debug)
log_stack = decorators.log_stack(bot_logger, bot_debug)
log_timer = decorators.log_timer(bot_logger, bot_debug)
log_exceptions = decorators.log_exceptions(bot_logger)
with_info = decorators.with_info


# redefine controller.py
class event(controller.event):
    @with_info(log_info, begin="raised", end="handled", report_params=True)
    def happen(self, message=None):
        super(event, self).happen(message)


class timer(controller.timer):
    @with_info(log_info, begin="start", report_params=True)
    def run(self):
        super(timer, self).run()

    @with_info(log_info, end="interrupt", report_params=True)
    def stop(self):
        super(timer, self).stop()


# redefine poster.py
import tgbot.bits.poster as poster
post = log_exceptions(poster.post)
verify_params = log_exceptions(poster.verify_params)

bot_mainloop = timer(interval=0.5, name='mainloop')
