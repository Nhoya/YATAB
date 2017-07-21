import telegram
import config

def helpcb(bot,update):
    msg = "===== *COMMANDS* =====\n"
    for command in config.commands:
        msg = msg+"/"+command.name+" - "+command.desc+"\n"
    msg = msg+" ===== *CONTROLS* =====\n"
    for cont in config.onjoin:
        msg = msg+"`"+cont.name+"` - "+cont.desc+"\n"
    bot.sendMessage(update.message.chat_id,text=msg,parse_mode='MARKDOWN')
    

class help:
    name = "help"
    cb = helpcb
    args = False
    desc = "show help"
