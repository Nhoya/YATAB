#generate link

def genlink(bot,update):
    uid = update.message
    gid = update.message.chat_id
    if isAdmin(bot,uid,gid):
        bot.sendMessage(gid,link)


class link:
    cb = genlink
    name = "link"
    args = False
