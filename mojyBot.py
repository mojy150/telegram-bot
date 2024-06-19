import telebot
# import PIL
import os
f = open("my bot token.txt","r+")
TOKEN = f.readline()
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def botmain(user):
    usertext = user.text
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name
    
    
    
    
    # --------------------------------------
    bot.send_message(userchatid,"salam chetori?")
    # --------------------------------------
    print("new message from:",userchatid)
    print("username:",userusername)
    print("firstname:",userfirstname)
    print("text:",usertext)
    print("-----------\n")
bot.polling()                                               #not end bot