import telegram
import re
from core.dbmanage import SetupSession, BotInWhitelist



def NoBots(bot,update):
    gid = update.message.chat_id
    new_members = update.message.new_chat_members
    for user in new_members:
        username = user.username
        uid = user.id
        if uid == bot.id:
            continue
        if re.search("\w*bot$",username,re.IGNORECASE) is None:
            continue
        db,cur = SetupSession()
        if not BotInWhitelist(db,cur,gid,uid):
            update.message.reply_text(text="Bot not in whitelist")
            bot.kickChatMember(gid, uid)
            db.close()
        else:
            update.message.reply_text(text="Bot in whitelist")
            db.close()
        

class nobots:
    name = "nobots"
    cb = NoBots
    desc = "kick bots not in whitelist"

