
import logging
from getwords import correctWord
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "5859542305:AAEj-BRMPO79UQEDAFmRjrAaPA4uA7PNq60"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Salom!\nMen Uz-Imlo-Botman!\nMening yordamimda siz so'zlarni to'g'ri yozishni o'rganasiz.")

@dp.message_handler(commands=["help"])
async def send_help(message:types.Message):

    await message.reply("Siz yordam buyrug'ini chaqirdizgiz!")

@dp.message_handler()
async def uzimlo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    word=message.text.lower()
    List=correctWord(word)
    if List[0]==1:
        answer=f"✅{List[1].capitalize()}"
    elif List[0]==0:
        answer=f"❌{word}\n"
        for i in List[1]:
            answer=answer+f"✅{i.capitalize()}\n"
    await message.answer(answer)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)