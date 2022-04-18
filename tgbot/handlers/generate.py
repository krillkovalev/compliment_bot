from aiogram import types
from tgbot.parser.pars import compliment


async def cmd_gnr(m: types.Message):
    await m.answer(compliment())