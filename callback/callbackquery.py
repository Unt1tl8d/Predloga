import datetime
import random
import sqlite3
import time
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram import types, Router, Bot
from data import config
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardRemove, Message
from keybord import Inlinekbord, kbord 
from handlers import us_command


Bot = Bot(config.token)
rout = Router()
db = sqlite3.connect('data\content.db')
cur = db.cursor()


async def last_msg(callback):
    g = await us_command.reit()
    print(g)
    await Bot.edit_message_text(text=f'Загружаю', chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    time.sleep(2)
    await Bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await Bot.send_message(text=f'Теперь надо немножко подождать и мы все запостим😘😘😘', chat_id=callback.message.chat.id, reply_markup=ReplyKeyboardRemove())
    await Bot.send_message(text=f'Оценка канала и бота на данный момент - {round(g, 1)}\n\n@{callback.from_user.username}, а во ты сколько оценишь наш канал и бота?\n', chat_id=callback.message.chat.id, reply_markup=Inlinekbord.reit())


async def find_cont(callback):
    msgid = callback.message.message_id
    cur.execute(f"SELECT * FROM save_content ORDER BY caption DESC")
    items = cur.fetchall()
    for i in items:
        if i[0] == msgid - 1:
            items = i
        if i[0] == msgid - 2:
            items = i
        if i[0] == msgid - 3:
            items = i
        if i[0] == msgid - 4:
            items = i
        if i[0] == msgid - 5:
            items = i
        if i[0] == msgid - 6:
            items = i
        if i[0] == msgid - 7:
            items = i
        if i[0] == msgid - 8:
            items = i
        if i[0] == msgid - 9:
            items = i
        if i[0] == msgid - 10:
            items = i
        if i[0] == msgid - 11:
            items = i
        if i[0] == msgid - 12:
            items = i
        if i[0] == msgid - 13:
            items = i
    return items


async def find_messager(callback):
    msgid = callback.message.message_id
    cur.execute(f"SELECT * FROM save_partner ORDER BY caption DESC")
    items = cur.fetchall()
    for i in items:
        if i[0] == msgid - 1:
            items = i
        if i[0] == msgid - 2:
            items = i
        if i[0] == msgid - 3:
            items = i
        if i[0] == msgid - 4:
            items = i
        if i[0] == msgid - 5:
            items = i
        if i[0] == msgid - 6:
            items = i
        if i[0] == msgid - 7:
            items = i
        if i[0] == msgid - 8:
            items = i
        if i[0] == msgid - 9:
            items = i
        if i[0] == msgid - 10:
            items = i
        if i[0] == msgid - 11:
            items = i
        if i[0] == msgid - 12:
            items = i
        if i[0] == msgid - 13:
            items = i
    return items


@rout.callback_query()
async def vote_callback(callback: types.CallbackQuery):
    db.commit()
    if callback.data == "customcapt":
        try:
            items = await find_cont(callback)
            contid = items[0]
            items = items[0]
            media1 = MediaGroupBuilder(caption=f"Контент с предложки от {items[4]} {items[3]}\n\nP.s Больше её фотографий в привате -- @TeloPodpischicybot - /subscription")
            try:
                cur.execute(f"SELECT photo FROM save_content WHERE id = {contid[0]}")
                items = cur.fetchall()
                for i in items:
                    if i == None:
                        pass
                    else:
                        media1.add_photo(media=i[0])
            except:
                pass
            try:
                cur.execute(f"SELECT video FROM save_content WHERE id = {contid[0]} ORDER BY video DESC")
                items = cur.fetchall()
                for i in items:
                    if i[0] == None:
                        pass
                    else:
                        media1.add_video(media=i[0])
            except:
                pass
            cur.execute(f"DELETE FROM `save_content` WHERE id = '{contid[0]}'")
            db.commit()
            await Bot.send_media_group(media=media1.build(), chat_id=config.channel)
            await Bot.edit_message_text(text=f'@{callback.from_user.username} контент успешно запощен',
                                        chat_id=config.predloga, message_id=callback.message.message_id)
        except:
            print('Ошибка в отправке с словами о привате')
            await Bot.send_message(text=f'Напиши сене я по пизде пошел', chat_id=config.predloga)
    if callback.data == "osnova": 
        try:
            items = await find_cont(callback)
            contid = items[0]
            media1 = MediaGroupBuilder(caption=f"Контент с предложки от {items[4]} {items[3]}\n\nПредложка для ваших фоток - @TeloPodpischicybot")
            try:
                cur.execute(f"SELECT photo FROM save_content WHERE id = {contid[5]}")
                items = cur.fetchall()
                for i in items:
                    if i == None:
                        pass
                    else:
                        media1.add_photo(media=i[0])
            except:
                pass
            try:
                cur.execute(f"SELECT video FROM save_content WHERE id = {contid[5]} ORDER BY video DESC")
                items = cur.fetchall()
                for i in items:
                    if i[0] == None:
                        pass
                    else:
                        media1.add_video(media=i[0])
            except:
                pass
            cur.execute(f"DELETE FROM `save_content` WHERE id = '{contid}'")
            db.commit()
            await Bot.send_media_group(media=media1.build(), chat_id=config.channel)
            await Bot.edit_message_text(text=f'@{callback.from_user.username} контент успешно запощен',
                                        chat_id=config.predloga, message_id=callback.message.message_id)
        except:
            print('Ошибка в отправке в основу')
            await Bot.send_message(text=f'Напиши сене я по пизде пошел', chat_id=config.predloga)
    if callback.data == "privat":
        try:
            items = await find_cont(callback)
            contid = items[0]
            media1 = MediaGroupBuilder(caption=f"Девочка с предложечки")
            try:
                cur.execute(f"SELECT photo FROM save_content WHERE id = {contid[0]} ORDER BY photo DESC")
                items = cur.fetchall()
                for i in items:
                        if i == None:
                            pass
                        else:
                            media1.add_photo(media=i[0])
            except:
                pass
            try:
                cur.execute(f"SELECT video FROM save_content WHERE id = {contid[0]} ORDER BY video DESC")
                items = cur.fetchall()
                for i in items:
                        if i == None:
                            pass
                        else:
                            media1.add_video(media=i[0])
            except:
                pass
            cur.execute(f"SELECT userid FROM save_content WHERE id = {contid[0]}")
            items = cur.fetchone()
            await Bot.send_media_group(media=media1.build(), chat_id=config.privat)
            await Bot.send_message(text='Твои фото были на столько хороши что мы их постонули в приватку, если хочешь постить такое на постоянной основе пиши девелоперу бота, оформим бесплатный приват за это🥰', chat_id=items[0])
            await Bot.edit_message_text(text=f'@{callback.from_user.username} контент успешно запощен',
                                        chat_id=config.predloga, message_id=callback.message.message_id)
            cur.execute(f"DELETE FROM `save_content` WHERE id = '{contid[0]}'")
            db.commit()
        except:
            print('Ошибка в отправке в приват')
            await Bot.send_message(text=f'Напиши сене я по пизде пошел', chat_id=config.predloga)
    if callback.data == "deny":
        try:
            items = await find_cont(callback)
            contid = items[0]
            cur.execute(f"SELECT * FROM save_content WHERE id = {contid}")
            items = cur.fetchall()
            for i in items:
                cur.execute(f"DELETE FROM `save_content` WHERE id = '{contid}'")
            db.commit()
            await Bot.edit_message_text(text=f'@{callback.from_user.username} контент объективно пошел нахуй',
                                        chat_id=config.predloga, message_id=callback.message.message_id)
        except:
            await Bot.send_message(text=f'Напиши сене я по пизде пошел', chat_id=config.predloga)
    if callback.data == '1':
        await Bot.edit_message_text(text=f'@{callback.from_user.username} спасибо за оценку!\n\nЕсли не сложно напиши ему @Iydihdihc8t что тебе не нравится.',
                                    chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        cur.execute(f"""UPDATE rait SET devident = devident + {callback.data}, divider = divider + 1 WHERE id = 1""")
        cur.execute(f"INSERT INTO rait (`id`, chatid, username, devident, divider) VALUES (?, ?, ?, ?, ?)",
                    (callback.message.message_id, callback.from_user.id, callback.from_user.username, int(callback.data), 1))
        db.commit()
    if callback.data == '2':
        await Bot.edit_message_text(text=f'@{callback.from_user.username} спасибо за оценку!\n\nЕсли не сложно напиши ему @Iydihdihc8t что тебе не нравится.',
                                    chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        cur.execute(f"""UPDATE rait SET devident = devident + {callback.data}, divider = divider + 1 WHERE id = 1""")
        cur.execute(f"INSERT INTO rait (`id`, chatid, username, devident, divider) VALUES (?, ?, ?, ?, ?)",
                    (callback.message.message_id, callback.from_user.id, callback.from_user.username, int(callback.data), 1))
        db.commit()
    if callback.data == '3':
        await Bot.edit_message_text(text=f'@{callback.from_user.username} спасибо за оценку!\n\nЕсли не сложно напиши ему @Iydihdihc8t что тебе не нравится.',
                                    chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        cur.execute(f"""UPDATE rait SET devident = devident + {callback.data}, divider = divider + 1 WHERE id = 1""")
        cur.execute(f"INSERT INTO rait (`id`, chatid, username, devident, divider) VALUES (?, ?, ?, ?, ?)",
                    (callback.message.message_id, callback.from_user.id, callback.from_user.username, int(callback.data), 1))
        db.commit()
    if callback.data == '4':
        await Bot.edit_message_text(text=f'@{callback.from_user.username} спасибо за оценку!\n\nЕсли не сложно напиши ему @Iydihdihc8t что тебе не нравится.',
                                    chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        cur.execute(f"""UPDATE rait SET devident = devident + {callback.data}, divider = divider + 1 WHERE id = 1""")
        cur.execute(f"INSERT INTO rait (`id`, chatid, username, devident, divider) VALUES (?, ?, ?, ?, ?)",
                    (callback.message.message_id, callback.from_user.id, callback.from_user.username, int(callback.data), 1))
        db.commit()
    if callback.data == '5':
        await Bot.edit_message_text(text=f'@{callback.from_user.username} спасибо за оценку!\n\nЕсли не сложно напиши ему @Iydihdihc8t что тебе не нравится.',
                                    chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        cur.execute(f"""UPDATE rait SET devident = devident + {callback.data}, divider = divider + 1 WHERE id = 1""")
        cur.execute(f"INSERT INTO rait (`id`, chatid, username, devident, divider) VALUES (?, ?, ?, ?, ?)",
                    (callback.message.message_id, callback.from_user.id, callback.from_user.username, int(callback.data), 1))
        db.commit()
    if callback.data == '6':
        await Bot.edit_message_text(text=f'@{callback.from_user.username} спасибо за хорошую оценку!\n',
                                    chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        cur.execute(f"""UPDATE rait SET devident = devident + {callback.data}, divider = divider + 1 WHERE id = 1""")
        cur.execute(f"INSERT INTO rait (`id`, chatid, username, devident, divider) VALUES (?, ?, ?, ?, ?)",
                    (callback.message.message_id, callback.from_user.id, callback.from_user.username, int(callback.data), 1))
        db.commit()
    if callback.data == '7':
        await Bot.edit_message_text(text=f'@{callback.from_user.username} спасибо за хорошую оценку!\n',
                                    chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        cur.execute(f"""UPDATE rait SET devident = devident + {callback.data}, divider = divider + 1 WHERE id = 1""")
        cur.execute(f"INSERT INTO rait (`id`, chatid, username, devident, divider) VALUES (?, ?, ?, ?, ?)",
                    (callback.message.message_id, callback.from_user.id, callback.from_user.username, int(callback.data), 1))
        db.commit()
    if callback.data == '8':
        await Bot.edit_message_text(text=f'@{callback.from_user.username} спасибо за хорошую оценку!\n',
                                    chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        cur.execute(f"""UPDATE rait SET devident = devident + {callback.data}, divider = divider + 1 WHERE id = 1""")
        cur.execute(f"INSERT INTO rait (`id`, chatid, username, devident, divider) VALUES (?, ?, ?, ?, ?)",
                    (callback.message.message_id, callback.from_user.id, callback.from_user.username, int(callback.data), 1))
        db.commit()
    if callback.data == '9':
        await Bot.edit_message_text(text=f'@{callback.from_user.username} спасибо за хорошую оценку!\n',
                                    chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        cur.execute(f"""UPDATE rait SET devident = devident + {callback.data}, divider = divider + 1 WHERE id = 1""")
        cur.execute(f"INSERT INTO rait (`id`, chatid, username, devident, divider) VALUES (?, ?, ?, ?, ?)",
                    (callback.message.message_id, callback.from_user.id, callback.from_user.username, int(callback.data), 1))
        db.commit()
    if callback.data == '10':
        await Bot.edit_message_text(text=f'@{callback.from_user.username} спасибо за хорошую оценку!\n',
                                    chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        cur.execute(f"""UPDATE rait SET devident = devident + {callback.data}, divider = divider + 1 WHERE id = 1""")
        cur.execute(f"INSERT INTO rait (`id`, chatid, username, devident, divider) VALUES (?, ?, ?, ?, ?)",
                    (callback.message.message_id, callback.from_user.id, callback.from_user.username, int(callback.data), 1))
        db.commit()
        db.commit()
    if callback.data == "anon":
        try:
            anon = 'Anonymous'
            cur.execute(f"SELECT caption FROM content WHERE users = '{callback.from_user.id}' ORDER BY caption DESC")
            caption = cur.fetchone()[0]
            if caption == None:
                caption = ''
                #caption = capt["вопрос от девочки: какая фотка лучше\n\n❤️- 1\n💘- 2"
                                #"вопрос от девочки: что вам больше нравится попа или грудь\n\n❤️грудь\n💘попа\n😈мне больше ножки"
                                #"вопрос от девочки: оцените попу\n❤️классная\n💘ну норм\n😈не очень"
                                #"вопрос от девочки: что бы сделали со мной?)\n\n❤️тр*хнул бы\n💘отшлепал\n😈ничего"
                                #"вопрос от девочки: помогите, какая фотка лучше\n❤️- 1\n💘- 2"]
            if str(caption):
                caption = f'\n\nCообщение - {caption}'
            media = MediaGroupBuilder(caption=f"Контент от nick - @{callback.from_user.username}, id - {callback.from_user.id}{caption}")
            cur.execute(f"SELECT photo FROM content WHERE users = '{callback.from_user.id}' ORDER BY photo DESC")
            photo = cur.fetchall()
            try:
                for i in photo:
                            media.add_photo(media=i[0])
                            cur.execute(f"INSERT INTO save_content (id, photo, caption, typepost, userid) VALUES (?, ?, ?, ?, ?)",
                                        (callback.message.message_id, i[0], caption, anon, callback.from_user.id))
            except:
                pass             
            cur.execute(f"SELECT video FROM content WHERE users = '{callback.from_user.id}' ORDER BY video DESC")
            video = cur.fetchall()
            try:
                for i in video:
                            media.add_video(media=i[0])
                            cur.execute(f"INSERT INTO save_content (id, video, caption, typepost, userid) VALUES (?, ?, ?, ?, ?)",
                                        (callback.message.message_id, i[0], caption, anon, callback.from_user.id))
            except:
                pass
            cur.execute(f"DELETE FROM content WHERE users = '{callback.from_user.id}'") 
            db.commit()
            await last_msg(callback)
            await Bot.send_media_group(media=media.build(), chat_id=config.predloga)
            await Bot.send_message(text=f'Постим фото выше или нет?',
                                   chat_id=config.predloga, parse_mode=ParseMode.HTML, reply_markup=Inlinekbord.solution_cont())        
        except:
            print('Ошибка в отправке в аноне')
            await Bot.send_message(text=f'Бот говорит ты ничего не отправил, если ты что-то отправил, но бот этого не видит пиши @Iydihdihc8t',
                                   chat_id=callback.message.chat.id, reply_markup=ReplyKeyboardRemove())
    if callback.data == "noanon":
        try:
            cur.execute(f"SELECT caption FROM content WHERE users = '{callback.from_user.id}' ORDER BY caption DESC")
            caption = cur.fetchone()[0]
            print(caption)
            if caption == None:
                caption = ''
            if caption == str:
                caption = '\n\nCообщение - '+caption
            media = MediaGroupBuilder(caption=f"Контент от nick - @ {callback.from_user.username}, id - {callback.from_user.id}\n\nCообщение - {caption}")
            cur.execute(f"SELECT photo FROM content WHERE users = '{callback.from_user.id}' ORDER BY photo DESC")
            photo = cur.fetchall()
            try:
                for i in photo:
                        media.add_photo(media=i[0])
                        cur.execute(f"INSERT INTO save_content (id, video, caption, typepost, userid) VALUES (?, ?, ?, ?, ?)",
                                    (callback.message.message_id, i[0], caption, '@'+callback.from_user.username, callback.from_user.id))
            except:
                pass
            try:
                cur.execute(f"SELECT video FROM content WHERE users = '{callback.from_user.id}' ORDER BY video DESC")
                video = cur.fetchall()
                for i in video:
                        media.add_video(media=i[0])
                        cur.execute(f"INSERT INTO save_content (id, video, caption, typepost, userid) VALUES (?, ?, ?, ?, ?)",
                                    (callback.message.message_id, i[0], caption, '@'+callback.from_user.username, callback.from_user.id))
            except:
                pass
            cur.execute(f"DELETE FROM content WHERE users = '{callback.from_user.id}'") 
            db.commit()
            await last_msg(callback)
            await Bot.send_media_group(media=media.build(), chat_id=config.predloga)
            await Bot.send_message(text=f'Постим фото выше или нет?', chat_id=config.predloga, parse_mode=ParseMode.HTML, reply_markup=Inlinekbord.solution_cont())  
        except:
            print('Ошибка в отправке в неаноне')
            await Bot.send_message(text=f'Бот говорит ты ничего не отправил, если ты что-то отправил, но бот этого не видит пиши @Iydihdihc8t',
                                         chat_id=callback.message.chat.id, reply_markup=ReplyKeyboardRemove())
    
    #партнерка и все такое
    if callback.data == 'sendpart':
        cur.execute(f"SELECT * FROM partner WHERE id = '{callback.from_user.id}' ORDER BY caption DESC")
        items = cur.fetchone()
        cur.execute(f"INSERT INTO save_partner (`id`, chatid, caption, username) VALUES (?, ?, ?, ?)",
                    (callback.message.message_id, items[0], items[1], callback.from_user.username))
        cur.execute(f"DELETE FROM partner WHERE id = '{items[0]}'")
        await Bot.edit_message_text(text='Я отправил твое предложение админу, ожидай ответа, он придет сюда.',
                                    chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await Bot.send_message(text=f'Предложение от @{callback.from_user.username}\n\nСодержимое - {items[1]}',
                               chat_id=config.advert, parse_mode=ParseMode.HTML, reply_markup=Inlinekbord.solution_partner())
        db.commit()
    if callback.data == 'delete':
        await Bot.edit_message_text(text='Жаль конечно, но я удалил твое предложение.',
                                    chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        cur.execute(f"DELETE FROM partner WHERE id = '{callback.from_user.id}'")
        db.commit()
    if callback.data == 'cancel':
        await Bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await us_command.help(callback.message)
        cur.execute(f"DELETE FROM partner WHERE id = '{callback.from_user.id}'")
        db.commit()
    if callback.data == 'partaccept':
        items = await find_messager(callback)
        contid = items[0]
        cur.execute(f"SELECT * FROM save_partner WHERE id = '{contid}' ORDER BY caption DESC")
        items = cur.fetchone()
        cur.execute(f"DELETE FROM save_partner WHERE chatid = '{items[1]}'")
        cur.execute(f"INSERT INTO messages (acceptid, userid) VALUES (?, ?)", (callback.from_user.id, items[1]))
        db.commit()
        await Bot.edit_message_text(text=f'@{callback.from_user.username} принял предложение от @{items[3]}\n\nПредложение - {items[2]}\n\n@TeloPodpischicybot там переписываться c @{items[3]}.', message_id=callback.message.message_id, chat_id=config.advert)
        await Bot.send_message(text='Все что ты сюда напишешь будет отправлено собеседнику.', chat_id=callback.from_user.id, reply_markup=kbord.cancel())
        await Bot.send_message(text='Ваше предложение заинтересовало админа.', chat_id=items[1], reply_markup=kbord.cancel())
    if callback.data == 'partdeny':
        items = await find_messager(callback)
        contid = items[0]
        cur.execute(f"SELECT * FROM save_partner WHERE id = '{contid}' ORDER BY caption DESC")
        items = cur.fetchone()
        await Bot.edit_message_text(text=f'@{callback.from_user.username} отклонил предложение от - @{items[3]}\n\nПредложение - {items[2]}',
                                    chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await Bot.send_message(chat_id=items[1], text='Администратор отклонил ваше предложение')
        cur.execute(f"DELETE FROM save_partner WHERE chatid = '{items[1]}'")
        db.commit()

    #подписки
    if callback.data == "subinfiniti":
        try:
            cur.execute("INSERT INTO pay (callid, id, nick, srok) VALUES (?,?,?,?)", (callback.message.message_id, callback.from_user.id, callback.from_user.username, callback.data))
            db.commit()
            await Bot.edit_message_text(text='Подписка на приват навсегда 300р',
                                        chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=Inlinekbord.payment())
        except:
            print('Ошибка в саб инфинити')
            await Bot.send_message(text=f'Походу я ебланул, напиши мне в лс я решу проблемму @Iydihdihc8t',
                                        chat_id=callback.message.chat.id, reply_markup=ReplyKeyboardRemove())
    if callback.data == "submonth":
        try:
            cur.execute("INSERT INTO pay (callid, id, nick, srok) VALUES (?,?,?,?)", (callback.message.message_id, callback.from_user.id, callback.from_user.username, callback.data))
            db.commit()
            await Bot.edit_message_text(text='Подписка на приват на месяц 100р',
                                        chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=Inlinekbord.payment())
        except:
            print('Ошибка в саб монс')
            await Bot.send_message(text=f'Походу я ебланул, напиши мне в лс я решу проблемму @Iydihdihc8t',
                                        chat_id=callback.message.chat.id, reply_markup=ReplyKeyboardRemove())
    if callback.data == "back":
        cur.execute(f"DELETE FROM pay WHERE callid = '{callback.message.message_id}'")
        db.commit()
        await Bot.edit_message_text(text='Подписка навсегда 300p\nПодписка на месяц 100p', message_id=callback.message.message_id, chat_id=callback.from_user.id, reply_markup=Inlinekbord.product())
    if callback.data == "pay":
        try:
            await Bot.edit_message_text(text='Реквизиты для перевода\nСard - 2200 7008 8280 3439\nПолучатель - Вера М\nБанк Тинькофф\nВ КОМЕНТАРИИ К ОПЛАТЕ ПИШИ СВОЙ ЮЗЕРНЕЙМ ИЛИ МОЖЕШЬ ПОТЕРЯТЬ ДЕНЬГИ', chat_id=callback.from_user.id,message_id=callback.message.message_id, reply_markup=Inlinekbord.complete())
        except:
            await Bot.send_message(text=f'Походу я ебланул, напиши мне в лс я решу проблемму @Iydihdihc8t',
                                        chat_id=callback.message.chat.id, reply_markup=ReplyKeyboardRemove())
    if callback.data == "complete":
        try:
            await Bot.edit_message_text(text='Ожидайте проверки оплаты', chat_id=callback.from_user.id, message_id=callback.message.message_id)
            cur.execute(f"SELECT * FROM pay WHERE callid = '{callback.message.message_id}'")
            items = cur.fetchall()
            print(callback.message.message_id)
            print(items)
            items = items[0]
            await Bot.send_message(text=f"@Iydihdihc8t проверь оплату {items[3]} @{callback.from_user.username}",chat_id=config.buysub, reply_markup=Inlinekbord.solution_pay())
            db.commit()
        except:
            print('Ошибка в проверке оплаты')
            await Bot.send_message(text=f'Походу я ебланул, напиши мне в лс я решу проблемму @Iydihdihc8t',
                                        chat_id=callback.message.chat.id, reply_markup=ReplyKeyboardRemove())
    if callback.data == "payaccept":
        try:
            callid = callback.message.message_id - 1
            cur.execute(f"SELECT * FROM pay WHERE callid = '{callid}'")
            items = cur.fetchall()
            print(callback.message.message_id)
            print(callid)
            print(items)
            items = items[0]
            chat_id = config.privat
            link = await Bot.create_chat_invite_link(chat_id,name='Покупка привата', member_limit=1)
            await Bot.send_message(text=link.invite_link, chat_id=items[1])
            await Bot.edit_message_text(text=f'Ты одобрил подписку @{items[2]} на {items[3]}', chat_id=callback.message.chat.id, message_id=callback.message.message_id)
            cur.execute("INSERT INTO sub (callid, id, nick, srok) VALUES (?,?,?,?)", (items[0], items[1], items[2], items[3]))
            cur.execute(f"DELETE FROM pay WHERE callid = '{items[0]}'")
            db.commit()
        except:
            await Bot.send_message(text=f'Ты долбоеб, нахуя багованую хуйню написал? Иди теперь смотри че не так и помогай юзеру!!!',
                                        chat_id=callback.message.chat.id, reply_markup=ReplyKeyboardRemove())
    if callback.data == 'paydeny':
        try:
            callid = callback.message.message_id - 1
            cur.execute(f"SELECT * FROM pay WHERE callid = '{callid}'")
            items = cur.fetchall()
            items = items[0]
            print(callback.message.message_id)
            print(callid)
            print(items)
            cur.execute(f"DELETE FROM pay WHERE callid = '{items[0]}'")
            db.commit()
            await Bot.send_message(text="Ты кого наебать хочешь?))) Ты вот думаешь я бота написать смог, а наеб не увижу, да?XD", chat_id=items[1])
            await Bot.edit_message_text(text=f'Ты послал нахуй того кто хотел наебать тебя', chat_id=config.buysub, message_id=callback.message.message_id)
        except:
            await Bot.send_message(text=f'Ты долбоеб, нахуя багованую хуйню написал? Иди теперь смотри че не так и помогай юзеру!!!',
                                        chat_id=callback.message.chat.id, reply_markup=ReplyKeyboardRemove())