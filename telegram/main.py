from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram import ReplyKeyboardMarkup
from config import BOT_TOKEN
import random


async def start(update, context):
    reply_keyboard = [['/dice', '/timer']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text(
        "Привет!",
        reply_markup=markup
    )


async def dice(update, context):
    reply_keyboard = [['/one', '/two'],
                      ["/twenty", "/back"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text(
        "Dices: ",
        reply_markup=markup
    )


async def one(update, context):
    reply_keyboard = [['/one', '/two'],
                      ["/twenty", "/back"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text(
        random.randint(0, 7),
        reply_markup=markup
    )


async def two(update, context):
    reply_keyboard = [['/one', '/two'],
                      ["/twenty", "/back"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text(
        f"{random.randint(0, 7)} {random.randint(0, 7)}",
        reply_markup=markup
    )


async def twenty(update, context):
    reply_keyboard = [['/one', '/two'],
                      ["/twenty", "/back"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text(
        f"{random.randint(0, 20)}",
        reply_markup=markup
    )

async def timer(update, context):
    reply_keyboard = [['/timer30', '/timer1'],
                      ["/timer5", "/back"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text(
        f"Timers: ",
        reply_markup=markup
    )


async def timer30(update, context):
    pass

async def timer1(update, context):
    pass

async def timer5(update, context):
    pass


back = start


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("dice", dice))
    application.add_handler(CommandHandler("timer", timer))
    application.add_handler(CommandHandler("one", one))
    application.add_handler(CommandHandler("two", two))
    application.add_handler(CommandHandler("twenty", twenty))
    application.add_handler(CommandHandler("30sec", timer30))
    application.add_handler(CommandHandler("one_minute", timer1))
    application.add_handler(CommandHandler("five_minute", timer5))
    application.add_handler(CommandHandler("back", back))
    
    
    application.run_polling()


main()