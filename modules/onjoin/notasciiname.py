import telegram
from telegram.error import *

def NoAsciiCharName(bot,update):
    gid = update.message.chat_id
    new_members = update.message.new_chat_members
    for user in new_members:
        name = user.first_name
        uid = user.id
        try:
            name.encode('ascii')
        except UnicodeEncodeError:
            try:
                bot.kickChatMember(gid,uid)
                bot.sendMessage(gid,text="You are so lame")
            except TelegramError:
                return


class no_ascii_name:
    name = "not_ascii_name"
    cb = NoAsciiCharName
    desc = "kick users with non-ascii char in first name"
