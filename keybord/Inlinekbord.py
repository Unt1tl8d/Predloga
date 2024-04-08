from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def solution():
    markup = InlineKeyboardMarkup(row_wight=2, 
    inline_keyboard=[
            [
            InlineKeyboardButton(text= '✅', callback_data='accept'),
            InlineKeyboardButton(text= '❌', callback_data='deny')
        ]
        ]
        )
    return markup


def typepost():
    markup = InlineKeyboardMarkup(row_wight=2, 
    inline_keyboard=[
            [
            InlineKeyboardButton(text= 'Анонимно', callback_data='anon'),
            InlineKeyboardButton(text= 'Не анонимно', callback_data='noanon')
        ]
        ]
        )
    return markup


def reit():
    markup = InlineKeyboardMarkup(row_wight=2, 
        inline_keyboard=[
            [
            InlineKeyboardButton(text= '👍', callback_data='cool'),
            InlineKeyboardButton(text= '👎', callback_data='bad')
        ]
        ]
        )
    return markup


def solution_partner():
    markup = InlineKeyboardMarkup(row_wight=2, 
    inline_keyboard=[
            [
            InlineKeyboardButton(text= '✅', callback_data='partaccept'),
            InlineKeyboardButton(text= '❌', callback_data='partdeny')
        ]
        ]
        )
    return markup



def partner():
    markup = InlineKeyboardMarkup(row_wight=2, 
        inline_keyboard=[
            [
            InlineKeyboardButton(text="Отправить предложение", callback_data='sendpart'),
            InlineKeyboardButton(text="Oтменить", callback_data='delete')
        ]
        ]
        )
    return markup


def cancel():
    markup = InlineKeyboardMarkup(row_wight=1, 
        inline_keyboard=[
            [
            InlineKeyboardButton(text="Oтменить", callback_data='cancel')
        ]
        ]
        )
    return markup