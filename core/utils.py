import telegram
from telegram import *
from telegram.bot import *

def isAdmin(bot,uid,gid):
    role = bot.getChatMember(gid, uid)
    return (True if role.status in ["administrator", "creator"] else False)

