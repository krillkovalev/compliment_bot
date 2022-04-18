from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.handlers.generate import cmd_gnr
from tgbot.handlers.help import cmd_help
from tgbot.handlers.start import cmd_start
from tgbot.services.repository import Repo


# async def user_start(m: Message, repo: Repo):
#     # await repo.add_user(m.from_user.id)


def register_user(dp: Dispatcher):
    # dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(cmd_help, commands=['help'])
    dp.register_message_handler(cmd_gnr, commands=['generate'])