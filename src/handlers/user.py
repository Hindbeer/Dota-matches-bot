from aiogram.types import Message
from src.main import bot, dp
from src.keyboards import UserKeyboard
import src.misc.parser

parser = src.misc.parser


@dp.message_handler(commands='start')
async def start(message: Message):
    await bot.send_message(message.chat.id,
                           '''
🥴 Привет, я могу тебе показать текущие матчи в DotA2!
🤓 Нажми на кнопки ниже для большей информации (/help) 

                            ''', reply_markup=UserKeyboard.main_keyboard)


@dp.message_handler(text='информация')
async def start(message: Message):
    await bot.send_message(message.chat.id,
                           f'''
Этот бот вам покажет ближайшие матчи в DotA2 и на каком турнире они проходят.
Бот еще будет дополняться функционалом.

Вся информация берется с liquipedia.net
tg канал: @fancy_kuve
tg профиль: @G0golMogol
                            ''', )


@dp.message_handler(text='посмотреть игры')
async def show_matches(message: Message):
    await bot.send_message(message.chat.id, parser.show_matches())
