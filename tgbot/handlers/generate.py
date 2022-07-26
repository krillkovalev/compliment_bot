import aiogram.types
from aiogram import types
import requests


async def cmd_gnr(m: types.Message):
    compliment = requests.get('https://complimentr.com/api')
    compliment = compliment.json()
    await m.answer(f"{m.from_user.username}, {compliment['compliment']}")
