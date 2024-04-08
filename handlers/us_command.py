import sqlite3
from aiogram import Router, Bot
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, BotCommand
from data import config
from handlers import botmsg
from keybord import Inlinekbord, kbord
from aiogram.types import ReplyKeyboardRemove


Bot = Bot(config.token)
rout = Router()
db = sqlite3.connect('data\content.db')
cur = db.cursor()

@rout.startup()
async def setup_my_commands():
    bot_commands = [
        BotCommand(command="/start", description="Начало работы с ботом"),
        BotCommand(command="/help", description="Помощь с командами"),
        BotCommand(command="/rules", description="Правила для постинга фото"),
        BotCommand(command="/content", description="Предложение контента"),
        BotCommand(command="/partner", description="Реклама, партнерство и т.п предложения"),
        BotCommand(command="/reit", description="Оценка паблика и бота")
    ]
    await Bot.set_my_commands(bot_commands)


@rout.message(Command('start'))
async def start(message: Message):
    await message.answer('Приветствую тебя в боте канала @Telopodpischicy, я могу как отправить твой как контент который ты хочешь предложить так и предложение по рекламе и т.п\n\nКоманда которая поможет тебе разобраться /help', reply_markup=ReplyKeyboardRemove())


@rout.message(Command('reit'))
async def reit(message: Message):
    await message.answer(f'@{message.from_user.username} тебе нравится наш канал и бот?(в будущем будет 10 бальная шкала)', reply_markup=Inlinekbord.reit())


@rout.message(Command('rules'))
async def rules(message: Message):
    await message.answer(F'Привет! постарайтесь соблюдать эти правила,\
 что-бы тебя опубликовали:\n1. Присылайте несколько фоток, если одна фотка есть\
 шанс что вас не опубликуют\n2. Тебе должно быть от 18 лет\n3. Желательно краткое\
 описание на 1-2 предложения\n4. За спам и оск баним в чате\n5. Кидайте только\
 сжатые фото и видео,\nСтараемся публиковать все быстро, и по очереди, поэтому\
 извините если задержка с вашей анкетой\n@TeloPodpischicy\n\nДля того чтоб отправить сообщение в предложку испорльзуй команду /content', reply_markup=ReplyKeyboardRemove())
    return message


@rout.message(Command('help'))
async def help(message: Message):
    await message.answer(F'Привет! Я готов помочь тебе понять как я работаю.\n\n\
/rules - это правила для того чтоб твое предложение контента одобрили.\n\n\
/content - c помощью нее ты сможешь предложить свой контент в наш канал.(Если хочешь свою подпись к фото в паблике, то подписывай фото)\n\n\
/partner - это команда для предложений по рекламе, сотруднечеству и т.п, после того как ты ее пропишешь надо будет ждать когда с тобой\
свяжется человек который за это отвечает через меня т.е бота.', reply_markup=ReplyKeyboardRemove())
    return message

@rout.message(Command('content'))
async def content(message: Message):
    await message.answer(text='Ну давай, порадуй нас красивым контентом',
        parse_mode=ParseMode.HTML,
        reply_markup=kbord.button())
    cur.execute(f"DELETE FROM `content` WHERE users = '{message.from_user.id}'")
    db.commit()


@rout.message(Command('partner'))
async def partner(message: Message):
    print(message.chat.id, message.from_user.id)
    cur.execute("INSERT INTO partner (id, caption) VALUES (?,?)", (message.from_user.id, message.text))
    #await message.answer(text='На данный момент команда в разработке, можешь написать @Iydihdihc8t или @Wernexxx')
    await message.answer(text='Теперь можешь писать свое предложение, не корректные предложения сразу будут удаляться!', reply_markup=Inlinekbord.cancel())
    db.commit()

@rout.message(Command('ls'))
async def ls(message: Message):
    await Bot.send_message(chat_id='6415335814', text='Чтоб написать предложение админу напиши /partner')