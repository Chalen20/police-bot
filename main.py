import config
import telebot
import random
import threading

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(chat_id=message.chat.id, text="Bot just started")
    catalogKBoard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    Steam = telebot.types.KeyboardButton(text="Steam")
    Origin = telebot.types.KeyboardButton(text="Origin")
    UPlay = telebot.types.KeyboardButton(text="UPlay")
    EpicGames = telebot.types.KeyboardButton(text="Epic Games")
    VPN = telebot.types.KeyboardButton(text="VPN")
    catalogKBoard.add(Steam, Origin, UPlay, EpicGames, VPN)
    bot.send_message(message.chat.id, "Выберите Раздел", reply_markup=catalogKBoard)


if __name__ == "__main__":
    bot.polling()
