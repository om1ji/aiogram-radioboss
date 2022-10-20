from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.methods import *

import logging
import radioboss_parser
from consts import *

bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


@dp.message(Command(commands=["start"]))

    # Отвечает на команду /start 

async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.full_name}!")

@dp.message(Command(commands=['next']))
async def next_song(message: Message) -> None:

    # Переключает на следующий трек
    if message.from_user.id in ADMINS:
        r = radioboss_parser.next()
        current = radioboss_parser.current_song()
        await bot.send_message(message.chat.id, f'{r}! The next song is "{current}"')
    else:
        await bot.send_message(message.chat.id, "You are not either Om1ji or DreamSystem!")

@dp.message(Command(commands=['info']))
async def next_song(message: Message) -> None:

    # Выводит информацию о текущем состоянии сервера

    current = radioboss_parser.current_song()
    await bot.send_message(message.chat.id, f"""Current song is "{radioboss_parser.current_song()}"
Amount of listeners: {radioboss_parser.current_listeners()} 
    """)

@dp.message()
async def to_om1ji(message: types.Message) -> None:

    # Принимает все сообщения типа Audio и пересылает их Омиджи.
    # В личке у Омиджи появляется пересланное сообщение типа Audio и автоматически бот делает на это сообщение reply с указанием отправителя.
    # Отправителю не обязательно иметь юзернейм для ссылки на него. Ссылка работает по его айди.

    if message.audio:
        answer = await bot.forward_message(OM1JI, message.from_user.id, message.message_id)
        await bot.send_message(OM1JI, f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>', reply_to_message_id=answer.message_id)


if __name__ == "__main__":
    dp.run_polling(bot)
