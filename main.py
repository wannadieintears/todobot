import asyncio
from aiogram import Bot, Dispatcher
import data
from handlers import handlers


async def main():
    bot = Bot(data.token)
    dp = Dispatcher()

    dp.include_routers(
        handlers.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())