from aiogram.types  import KeyboardButton, ReplyKeyboardMarkup


def button():
    end = KeyboardButton(text="Отправить контент")
    cancel = KeyboardButton(text="Удалить")
    button_row = [end, cancel]
    markup = ReplyKeyboardMarkup(keyboard=[button_row],resize_keyboard=True)
    return markup

def cancel():
    cancel = KeyboardButton(text="Прекратить диалог")
    button_row = [cancel]
    markup = ReplyKeyboardMarkup(keyboard=[button_row],resize_keyboard=True)
    return markup