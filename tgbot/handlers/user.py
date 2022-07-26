from aiogram import Dispatcher
# from aiogram.types import Message
from tgbot.handlers.error import cmd_error
from tgbot.handlers.generate import cmd_gnr
from tgbot.handlers.help import cmd_help
from tgbot.handlers.start import cmd_start


def register_user(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(cmd_help, commands=['help'])
    dp.register_message_handler(cmd_gnr, commands=['generate'])
    dp.register_message_handler(cmd_error)
