import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove
from assistant import Assistant

TOKEN = '7718113189:AAG9UNMbbmpkME7VBbjX81XovWh8qsP4BAs'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()
assistant = Assistant()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привіт! Я асистент-бот. Використовуйте /add, /list, /search.")

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("/add — додати нотатку\n/list — список\n/search — пошук")

@dp.message(Command("add"))
async def cmd_add(message: Message):
    await message.answer("Введіть текст нотатки:", reply_markup=ReplyKeyboardRemove())
    dp.message.register(process_note)

async def process_note(message: Message):
    assistant.add_note(message.text)
    await message.answer("Нотатку збережено.")
    dp.message.unregister(process_note)

@dp.message(Command("list"))
async def cmd_list(message: Message):
    notes = assistant.list_notes()
    if notes:
        text = "\n".join([f"{i+1}. {n}" for i, n in enumerate(notes)])
        await message.answer(text)
    else:
        await message.answer("Список нотаток порожній.")

@dp.message(Command("search"))
async def cmd_search(message: Message):
    await message.answer("Введіть ключове слово для пошуку:")
    dp.message.register(process_search)

async def process_search(message: Message):
    keyword = message.text
    results = assistant.search_notes(keyword)
    if results:
        await message.answer("\n".join(results))
    else:
        await message.answer("Нічого не знайдено.")
    dp.message.unregister(process_search)

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
