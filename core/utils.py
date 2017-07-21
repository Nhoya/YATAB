import telegram
from telegram import *
from telegram.bot import *

def isAdmin(bot,uid,gid):
    role = bot.getChatMember(gid, uid)
    if role.status == "administrator" or role.status == "creator":
        return True
    else:
        return False

