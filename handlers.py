from kryptoparse.gecko import parse
from kryptoparse.apl import parse1
from kryptoparse.PAT import parse2

from main import bot, dp


from aiogram.types import Message
from config import admin_id
from aiogram.dispatcher.filters import Command, Text

from keyboards.default import menu



async def sent_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='bot запущен')


@dp.message_handler(Command(["menu","start"]))
async def show_menu(message: Message):
    await message.answer("Можешь выбрать", reply_markup=menu)


@dp.message_handler(Text(equals=['BTC','ETH','APL','PAT']))
async def get_res(message: Message):
    await message.answer(f'Ты выбрал {message.text}. Подожди.') #reply_markup=ReplyKeyboardRemove())
#async def echo(message: Message):
    text = message.text
    res = parse()
    if text == 'BTC':
        await message.answer(text=res['btc'] + ' //info from coingecko')
    elif text == 'ETH':
        await message.answer(text=res['eth'] + ' //info from coingecko')
    elif text == 'APL':
        res = parse1()
        await message.answer(text=res['apl'] + ' //info from coingecko')
    elif text == 'PAT':
        res = parse2()
        await message.answer(text=res['pat'] + ' //info from coingecko')






    #await message.answer(text=text)
    # await bot.send_message(chat_id=admin_id,
    # text=text)



