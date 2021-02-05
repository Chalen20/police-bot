import config
import telebot
import random
import threading

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(chat_id=message.chat.id, text="Bot just started")


if __name__ == "__main__":
    bot.polling()
