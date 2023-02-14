import logging
from service import add_time
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters

from telegram.ext import ApplicationBuilder

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)

bot = (
    ApplicationBuilder().token("6280292684:AAHRlODNjfk32TsEb0jZFWKVWVQt_2BIfGk").build()
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Хендлер для команды start"""
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Напишите боту время в которое вы пришли на работу в формате HH:MM, например: 08:00. Бот напишет вам время, когда вы можете идти домой. Диапозон допустимых часов 6:00 - 11:59",
    )


async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    time = update.message.text
    result = await add_time(time)
    if result:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=result)
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Вы ввели неправильное время, повторите попытку в формате HH:MM, например: 08:00. Диапозон допустимых часов 6:00 - 11:59",
        )


def main():
    start_handler = CommandHandler("start", start)
    bot.add_handler(start_handler)
    time_handler = MessageHandler(filters.Text(), time)
    bot.add_handler(time_handler)
    bot.run_polling()


if __name__ == "__main__":
    main()
