from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Стоимость'),
            KeyboardButton(text='О нас'),
            KeyboardButton(text='Купить'),
            KeyboardButton(text='Регистрация')
        ]
    ], resize_keyboard=True
)

catalog_food_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Пицца', callback_data='product_buying'),
        InlineKeyboardButton(text='Суши', callback_data='product_buying')],
        [InlineKeyboardButton(text='Бургер', callback_data='product_buying'),
        InlineKeyboardButton(text='Шаурма', callback_data='product_buying')]
    ]
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Маленькая игра', callback_data='small')],
        [InlineKeyboardButton(text='Средняя игра', callback_data='medium')],
        [InlineKeyboardButton(text='Большая игра', callback_data='big')],
        [InlineKeyboardButton(text='Другие предложения', callback_data='other')]
    ]
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Купить!', url='http://ya.ru')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_catalog')]
    ]
)

admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Пользователи', callback_data='users')],
        [InlineKeyboardButton(text='Статистика', callback_data='stat')],
        [
            InlineKeyboardButton(text='Блокировка', callback_data='block'),
            InlineKeyboardButton(text='Разблокировка', callback_data='unblock'),
        ]
    ]
)