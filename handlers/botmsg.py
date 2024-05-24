import sqlite3
from aiogram import Router, F, Bot
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.media_group import MediaGroupBuilder
from handlers.us_command import partner
from keybord import Inlinekbord 
from data import config


Bot = Bot(config.token)
rout = Router()
db = sqlite3.connect('data\content.db')
cur = db.cursor()


@rout.message(F.text == 'Удалить')
async def close(message: Message):
    db = sqlite3.connect('data\content.db')
    cur = db.cursor()
    await message.answer(f'Очень жаль что ты передумал(ла), но мы будем ждать когда ты передумаешь и скинешь нам контент', reply_markup=ReplyKeyboardRemove())
    user = message.from_user.id
    cur.execute(f"DELETE FROM content WHERE users = '{user}'")
    db.commit()
    db.close()


@rout.message(F.text == 'Отправить контент')
async def send(message: Message):
    try:
        db = sqlite3.connect('data\content.db')
        cur = db.cursor()
        cur.execute(f"SELECT photo, video FROM content WHERE users = '{message.from_user.id}' ORDER BY caption DESC")
        caption = cur.fetchone()
        db.commit()
        db.close()
        await message.answer(f'Хорошо, а как будем постить?\n\nВнимание!!!\nЧтоб постить не анонимно у вас должен быть юзернейм!!!', reply_markup=Inlinekbord.typepost())
    except:
        db.close()
        await message.answer(text='Бот говорит ты ничего не отправил(ла), если ты что-то отправил(ла), но бот этого не видит пиши @Iydihdihc8t', reply_markup=ReplyKeyboardRemove())


@rout.message()
async def wait(message: Message):
    print(f"{message.text},\n {message.from_user.username},\n {message.from_user.id}")
    db = sqlite3.connect('data\content.db')
    cur = db.cursor()
    user = message.from_user.id
    msg = message.caption
    if message.photo:
        photo = message.photo[-1].file_id
        cur.execute(f"INSERT INTO content (`users`, `photo`, `caption`) VALUES (?, ?, ?)", (user, photo, msg))
        db.commit()
    if message.video:
        video = message.video.file_id
        cur.execute(f"INSERT INTO content (`users`, `video`, `caption`) VALUES (?, ?, ?)", (user, video, msg))
        db.commit()
    try:
        cur.execute(f"SELECT acceptid, userid FROM messages")
        items = cur.fetchone()
        print(items)
        if message.from_user.id == items[0]:
                        print(message.from_user.username, message.text)
                        await message.send_copy(chat_id=items[1])
        if message.from_user.id == items[1]:
                        print(message.from_user.username, message.text)
                        await message.send_copy(chat_id=items[0])
        if message.text == 'Прекратить диалог':
                        await Bot.send_message(text='Ваш диалог завершен', chat_id=items[1], reply_markup=ReplyKeyboardRemove())
                        await Bot.send_message(text='Ваш диалог завершен', chat_id=items[0], reply_markup=ReplyKeyboardRemove())
                        if message.from_user.id == items[1]:
                            cur.execute(f"DELETE FROM messages WHERE userid = '{message.from_user.id}'")
                            db.commit()
                        if message.from_user.id == items[0]:
                            cur.execute(f"DELETE FROM messages WHERE acceptid = '{message.from_user.id}'")
                        db.commit()
    except:
        cur.execute(f"SELECT id FROM partner")
        chat_id = cur.fetchall()
        print(chat_id)
        for i in chat_id:
            msg = message.text
            i = i[0]
            if message.from_user.id == i:
                print(user, message.text, message.message_id)
                cur.execute(f"INSERT INTO partner (`id`, `caption`) VALUES (?, ?)", (user, msg))
                await message.answer('Хорошо, я записал то что ты хочешь, отправляем это админу?', reply_markup=Inlinekbord.partner())
                db.commit()


