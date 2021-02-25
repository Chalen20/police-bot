import config
import telebot
import random
import threading

bot = telebot.TeleBot(config.TOKEN)

global chat_id





@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(chat_id=message.chat.id, text="Bot just started")

    # level 0
    levelZeroBoard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    Start = telebot.types.KeyboardButton(text="Так")
    levelZeroBoard.add(Start)
    bot.send_message(message.chat.id, "Ви стали учасником ДТП?", reply_markup=levelZeroBoard)

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    """
    :param query: об'єкт запиту (при натисканні на кнопочку)
    :return:
    """
    data = query.data

    # Викликається при натисканні на кнопку Enter
    if data.startswith("Так"):
        level_1(query)

def level_1(query):
    # level 1
    bot.send_message(chat_id=query.chat.id, text="Level 1")


if __name__ == "__main__":
    bot.polling()
