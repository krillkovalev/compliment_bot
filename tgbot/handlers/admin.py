# from aiogram import Dispatcher
# # from aiogram.dispatcher import FSMContext
# from aiogram.types import Message
#
# from tgbot.handlers.error import cmd_error
# from tgbot.handlers.generate import cmd_gnr
# from tgbot.handlers.start import cmd_start
# from tgbot.handlers.help import cmd_help
#
#
# async def admin_start(m: Message):
#     await m.answer("Бот запущен!")
#
#
# def register_admin(dp: Dispatcher):
#     dp.register_message_handler(cmd_start, commands=['start'])
#     dp.register_message_handler(cmd_help, commands=['help'])
#     dp.register_message_handler(cmd_gnr, commands=['generate'])
#     dp.register_message_handler(cmd_error)
