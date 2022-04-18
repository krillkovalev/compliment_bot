from aiogram import Dispatcher
# from aiogram.dispatcher import FSMContext
# from aiogram.types import Message

from tgbot.handlers.generate import cmd_gnr
from tgbot.handlers.start import cmd_start
from tgbot.handlers.help import cmd_help
# from tgbot.models.role import UserRole
# from tgbot.services.repository import Repo


# async def admin_start(m: Message):
#     await m.answer("Hello, admin!")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
    # dp.register_message_handler(admin_start, commands=["start"], state="*", role=UserRole.ADMIN)
    dp.register_message_handler(cmd_help, commands=['help'])
    dp.register_message_handler(cmd_gnr, commands=['generate'])

    # # or you can pass multiple roles:
    # dp.register_message_handler(admin_start, commands=["start"], state="*", role=[UserRole.ADMIN])
    # # or use another filter:
    # dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
