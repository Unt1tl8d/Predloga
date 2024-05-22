from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def solution_cont():
    row_first = (InlineKeyboardButton(text= 'Основной тгк', callback_data='osnova'),
            InlineKeyboardButton(text= 'Приватка', callback_data='privat'))
    row_second = (InlineKeyboardButton(text="Слова о привате", callback_data="customcapt"),
                  InlineKeyboardButton(text= 'Не постить эту хуйню', callback_data='deny'))
    rows = [row_first, row_second]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
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


def solution_pay():
    markup = InlineKeyboardMarkup(row_wight=2, 
    inline_keyboard=[
            [
            InlineKeyboardButton(text= '✅', callback_data='payaccept'),
            InlineKeyboardButton(text= '❌', callback_data='paydeny')
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

def product():
    markup = InlineKeyboardMarkup( 
    inline_keyboard=[
            [
            InlineKeyboardButton(text= 'Подписка навсегда 300p', callback_data='subinfiniti'),
            InlineKeyboardButton(text= 'Подписка на месяц 100p', callback_data='submonth')
        ]
        ]
        )
    return markup


def complete():
    markup = InlineKeyboardMarkup( 
    inline_keyboard=[
            [
            InlineKeyboardButton(text= 'проверить оплату', callback_data='complete'),
        ]
        ]
        )
    return markup


def payment():
    #url = f'https://auth.robokassa.ru/Merchant/Index.aspx?MerchantLogin=@TeloPodpischicybot&OutSum={score}&Description=TeloPrivat&SignatureValue=TMeqdwc12OKIw9VvjE59'
    markup = InlineKeyboardMarkup(row_wight=1,
    inline_keyboard=[
            [
            InlineKeyboardButton(text= 'Оплатить', callback_data='pay'),
            InlineKeyboardButton(text= 'Отмена', callback_data='back')
        ]
        ]
        )
    return markup