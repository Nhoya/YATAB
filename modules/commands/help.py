import telegram
import config
from telegram import ParseMode
import html

def helpcb(bot,update):
    msg = "===== <b>COMMANDS</b> =====\n"
    for command in config.commands:
        msg += "/{} - {}\n".format(html.escape(command.name), html.escape(command.desc))
    msg = msg+" ===== <b>CONTROLS</b> =====\n"
    for cont in config.onjoin:
        msg += "<code>{}</code> - <code>{}</code>\n".format(html.escape(cont.name), html.escape(cont.desc))
    update.message.reply_text(text=msg, parse_mode=ParseMode.HTML)
    

class help:
    name = "help"
    cb = helpcb
    args = False
    desc = "show help"
