import os
import logging
from service import add_time
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters

from telegram.ext import ApplicationBuilder

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)

#  создаем объект бота
bot = ApplicationBuilder().token(os.environ.get("TOKEN")).build()

#  сообщения - константы для вывода пользователю
START_MESSAGE = "Напишите боту время в которое вы пришли на работу в формате HH:MM, например: 08:00.\
    Бот напишет вам время, когда вы можете идти домой. Диапозон допустимых часов 6:00 - 11:59"
TIME_MESSAGE = "Вы ввели неправильное время, повторите попытку в формате HH:MM, \
    например: 08:00. Диапозон допустимых часов 6:00 - 11:59"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Хендлер для команды start"""
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=START_MESSAGE,
    )


async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Хенндлер для вычисления времени ухода с работы"""
    time = update.message.text
    result = await add_time(time)
    if result:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=result)
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=TIME_MESSAGE,
        )


#  регистрация хендлеров и запуск бота
def main():
    start_handler = CommandHandler("start", start)
    bot.add_handler(start_handler)
    time_handler = MessageHandler(filters.Text(), time)
    bot.add_handler(time_handler)
    bot.run_polling()


if __name__ == "__main__":
    main()
