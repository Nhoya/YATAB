#generate link

def genlink(bot,update):
    uid = update.message
    gid = update.message.chat_id
    if isAdmin(bot,uid,gid):
        update.message.reply_text(text=link)


class link:
    cb = genlink
    name = "link"
    args = False
