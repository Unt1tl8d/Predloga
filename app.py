import asyncio
from aiogram import Bot, Dispatcher
from data import config
from callback import callbackquery
from handlers import botmsg, us_command


async def main():
    bot = Bot(config.token)
    dp = Dispatcher()

    dp.include_routers(
        us_command.rout,
        callbackquery.rout,
        botmsg.rout
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())