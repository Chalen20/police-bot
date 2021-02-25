import config
import telebot
import random
import threading

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(chat_id=message.chat.id, text="Bot just started")

    # level 0
    levelZeroBoard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    Start = telebot.types.KeyboardButton(text="Так")
    levelZeroBoard.add(Start)
    bot.send_message(message.chat.id, "Ви стали учасником ДТП?", reply_markup=levelZeroBoard)
    bot.register_next_step_handler(message, get_answer_level_1)


def get_answer_level_1(message):
    if message.text == "Так":
        levelOneBoard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        Yes = telebot.types.KeyboardButton(text="Так")
        No = telebot.types.KeyboardButton(text='Ні')
        levelOneBoard.add(Yes)
        levelOneBoard.add(No)
        bot.send_message(text="Чи є потерпілі?", chat_id=message.chat.id, reply_markup=levelOneBoard)
        bot.register_next_step_handler(message, get_answer_level_2)
    else:
        bot.send_message(text="Так, а що ти від мене хотів?", chat_id=message.chat.id)


def get_answer_level_2(message):
    if message.text == "Так":
        bot.send_message(text="Ойой", chat_id=message.chat.id)
    else:
        bot.send_message(text="Хух", chat_id=message.chat.id)


if __name__ == "__main__":
    bot.polling()
