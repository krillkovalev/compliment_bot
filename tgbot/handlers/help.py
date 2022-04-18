from aiogram import types


async def cmd_help(m: types.Message):
    await m.answer(f'Привет, {m.from_user.full_name}! \n'
                   f'Тебе нужна помощь?')
