import sqlite3
import re
from aiogram import Bot, Router, types
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
    BotCommand(command="/help", description="Помощь с командами"),
    BotCommand(command="/rules", description="Правила для постинга фото"),
    BotCommand(command="/subscription", description="Покупка привата канала"),
    BotCommand(command="/content", description="Предложение контента"),
    BotCommand(command="/partner", description="Реклама, партнерство и т.п предложения"),
    BotCommand(command="/reit", description="Оценка паблика и бота"),
    ]
    await Bot.set_my_commands(bot_commands)


@rout.message(Command('start'))
async def start(message: Message):
    await message.answer('Приветствую тебя в боте канала @Telopodpischicy, я могу как отправить твой как контент который ты хочешь предложить так и предложение по рекламе и т.п\n\nКоманда которая поможет тебе разобраться /help\n\nЧтобы отправить свой контент пиши /content', reply_markup=ReplyKeyboardRemove())


@rout.message(Command('reit'))
async def reit(message: Message):
    cur.execute(f"SELECT devident, divider FROM rait")
    items = cur.fetchall()
    items = items[0]
    print(items[0])
    devident = items[0]
    devider = items[1]
    g = devident / devider
    print(f'Rait = {g}')
    await message.answer(f'Оценка канала и бота на данный момент - {round(g, 1)}\n\n@{message.from_user.username}, а во ты сколько оценишь наш канал и бота?', reply_markup=Inlinekbord.reit())


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
/rules - правила для того чтоб твое предложение контента одобрили.\n\n\
/content - c помощью нее ты сможешь предложить свой контент в наш канал.(Если хочешь свою подпись к фото в паблике, то подписывай фото)\n\n\
/partner - команда для предложений по рекламе, сотруднечеству и т.п, после того как ты ее пропишешь и отправишь предложение надо будет ждать когда с тобой\
свяжется человек который за это отвечает через меня т.е бота.\n\n\
/subscription - команда для покупки привата нашего канала в котором много сочного контента', reply_markup=ReplyKeyboardRemove())
    return message


@rout.message(Command('content'))
async def content(message: Message):
    await message.answer(text='Ну давай, порадуй нас красивым контентом',
    parse_mode=ParseMode.HTML,
    reply_markup=kbord.button())
    cur.execute(f"DELETE FROM `content` WHERE users = '{message.from_user.id}'")
    db.commit()


@rout.message(Command('subscription'))
async def sub(message:Message):
    msg = message.answer(text='Подписка навсегда 300p\nПодписка на месяц 100p', reply_markup=Inlinekbord.product())
    return msg


@rout.message(Command('partner'))
async def partner(message: Message):
    print(message.chat.id, message.from_user.id)
    cur.execute("INSERT INTO partner (id, caption) VALUES (?,?)", (message.from_user.id, message.text))
    #await message.answer(text='На данный момент команда в разработке, можешь написать @Iydihdihc8t или @Wernexxx')
    await message.answer(text='Теперь можешь писать свое предложение, не корректные предложения сразу будут удаляться!', reply_markup=Inlinekbord.cancel())
    db.commit()


@rout.message(Command('allcont'))
async def allcont(message:Message):
    cur.execute(f"SELECT users, photo, video FROM content ORDER BY users DESC")
    items = cur.fetchall()
    print(items)
    if items[0] == (1,'1','1'):
            print('try')
            print(items[0])
            await Bot.send_message(chat_id=message.chat.id, text='База пустая, приходи позже')
    else:
        try:    
            for i in items:
                if i[1] == None:
                    print(i[0])
                    await Bot.send_video(chat_id=message.chat.id,caption=str(i[0]), video=i[2])
                else:
                    print(i[0])
                    await Bot.send_photo(chat_id=message.chat.id,caption=str(i[0]), photo=i[1])
        except:
            await Bot.send_message(chat_id=message.chat.id, text='Это все фото"')   

@rout.message(Command('ls'))
async def ls(message: Message):
    ids = [877909465,6069640212,6322299949,2142725920,6015594203]
    for i in ids:
        await Bot.send_message(chat_id=i, text='Напиши /partner еще раз, бот почемуто не воркал, но я все починил')