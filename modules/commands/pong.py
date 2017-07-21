import telegram

def pongcb(bot,update):
    update.message.reply_text(text="pong")

class pong:
    name = "ping"
    cb = pongcb
    args = False
    desc = "just for fun"
