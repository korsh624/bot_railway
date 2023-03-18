import logging
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN='5077133016:AAFeAjz4GDOe_39siIkaenFULthrEQ07YLY'
logging.basicConfig(level=logging.INFO)
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def echo(message:types.Message):
    await message.reply('Start')
@dp.message_handler(commands=['help'])
async def echo(message:types.Message):
    await message.reply('Справка бота')
if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)