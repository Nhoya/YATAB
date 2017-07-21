import random
#from telegram import *
import telegram


songs = ["HqGRCOup974", "XRfsdPJKhUo", "shulFP-035k", "53OAddB7xqI", "vwTuQNEVIwI", "jH68ZeUsM_s", "wDQs_06BSes", "i9lYCOb2oxM", "kYkCLvesmGI", "bp-vI3Ir5DY", "niHDWNHVGU4", "GKlFIxOhXoo", "0ZaKztEzLig", "6BpUlvP8Sfo", "adadmXP5doc", "3CmwqfXtzaY", "32KSpJ0eQoU", "evYVNzomoaU", "jIICr9wmW1M", "CpiQ9dE6bJQ", "_xzfjBnASOw", "ELP-F-qs_34", "93Bqipx787k", "hvLgmciarjs", "dJKijsG0nxY"]


def s0ngcb(bot,update):
    vid = random.choice(songs) #check config.py
    print(update.message.chat_id)
    bot.sendMessage(update.message.chat_id,text="https://www.youtube.com/watch?v="+vid)


class s0ng:
    name = "s0ng"
    cb = s0ngcb
    args = False
    desc = "pick random l33t s0ng"
