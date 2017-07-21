import telegram

def pongcb(bot,update):
    bot.sendMessage(update.message.chat_id,text="pong")

class pong:
    name = "ping"
    cb = pongcb
    args = False
    desc = "just for fun"
