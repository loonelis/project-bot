from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_categories, get_items_by_category

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Отзывы', callback_data='otz'), InlineKeyboardButton(text='Владелец', callback_data='vladelec')],
],)


to_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вернуться на главную',
                          callback_data='to_main')]
])




async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name,
                                          callback_data=f'category_{category.id}'))
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()



async def items(category_id: int):
    items = await get_items_by_category(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in items:
        keyboard.add(InlineKeyboardButton(text=item.name,
                                          callback_data=f'item_{item.id}'))
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()



admin_panel = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Разослать сообщение всем пользователям')],
    [KeyboardButton(text='Добавить новый товар')]
],resize_keyboard=True,
input_field_placeholder='Админ панель')


main_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='', callback_data='admr'), InlineKeyboardButton(text='Добавить товар', callback_data='admn')]
])