from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

import asyncio
import logging

from config import *
from keyboards import *
# from admin import *
# from db import *
from crud_functions import *
import texts

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Добро пожаловать, {message.from_user.username}! {texts.start}', reply_markup = start_kb)

#--- States Machine ---
@dp.message_handler(text='Регистрация')
async def sign_up(message):
    await message.answer(f'Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text) == False:
        await state.update_data(username = message.text)
        await message.answer(f'Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer(f'Пользователь существует, введите другое имя')
        await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email = message.text)
    await message.answer(f'Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age = message.text)
    data = await state.get_data()
    add_user(data['username'],data['email'],data['age'])
    await message.answer(f'Регистрация прошла успешно')
    await state.finish()

#-----------------------

@dp.message_handler(text='О нас')
async def price(message):
    await message.answer(texts.about, reply_markup = start_kb)

@dp.message_handler(text='Стоимость')
async def info(message):
    await message.answer('Что вас интересует?', reply_markup = catalog_kb)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    all_products = get_all_products()
    with open("images/Pizza.png", 'rb') as img:
        await message.answer_photo(img, f'Название: {all_products[0][0]} | Описание: {all_products[0][1]} | Цена: {all_products[0][2]}')
    with open("images/Sushi.png", 'rb') as img:
        await message.answer_photo(img, f'Название: {all_products[1][0]} | Описание: {all_products[1][1]} | Цена: {all_products[1][2]}')
    with open("images/Burger.png", 'rb') as img:
        await message.answer_photo(img, f'Название: {all_products[2][0]} | Описание: {all_products[2][1]} | Цена: {all_products[2][2]}')
    with open("images/Shaurma.png", 'rb') as img:
        await message.answer_photo(img, f'Название: {all_products[3][0]} | Описание: {all_products[3][1]} | Цена: {all_products[3][2]}')
    await message.answer('Выберите товар для покупки:', reply_markup = catalog_food_kb)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.callback_query_handler(text="small")
async def buy_s(call):
    await call.message.answer(texts.Sgame, reply_markup = buy_kb)
    await call.answer()

@dp.callback_query_handler(text="medium")
async def buy_m(call):
    await call.message.answer(texts.Mgame, reply_markup = buy_kb)
    await call.answer()

@dp.callback_query_handler(text="big")
async def buy_l(call):
    await call.message.answer(texts.Lgame, reply_markup = buy_kb)
    await call.answer()

@dp.callback_query_handler(text="other")
async def buy_other(call):
    await call.message.answer(texts.other, reply_markup = buy_kb)
    await call.answer()


@dp.callback_query_handler(text='back_to_catalog')
async def back(call):
    await call.message.answer('Что вас интересует?', reply_markup = catalog_kb)
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)