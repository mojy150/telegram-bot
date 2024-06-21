import telebot
# import PIL
import os
from telebot import types

f = open("my bot token.txt","r+")
TOKEN = f.readline()
bot = telebot.TeleBot(TOKEN)

def startcmd(user):
    usertext = user.text
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name
    
    dokmeha = types.ReplyKeyboardMarkup(row_width=3)
    dokme1 = types.KeyboardButton("test1")
    dokme2 = types.KeyboardButton("test2")
    dokme3 = types.KeyboardButton("test3")
    dokmeha.add(dokme1,dokme2,dokme3)
    
    bot.send_message(userchatid,"Hello, wellcome to mojy bot!",reply_markup=dokmeha)
# --------------------------------------
@bot.message_handler(content_types=["text"])
def botmain(user):
    usertext = user.text
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name
    
    if usertext == "/start":
        startcmd(user)
    
    
    # --------------------------------------
    print("new message from:",userchatid)
    print("username:",userusername)
    print("firstname:",userfirstname)
    print("text:",usertext)
    print("-----------\n")
bot.polling()                                               #not end bot