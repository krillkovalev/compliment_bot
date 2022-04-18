from aiogram import types


async def cmd_start(m: types.Message):
    await m.answer(f'Привет, {m.from_user.full_name}! Я бот, который умеет генерировать комплименты.')
