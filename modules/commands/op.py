from core.dbmanage import SetupSession, RegisterUser, RegisterAdmin, AdminInDb, RemoveAdmin
import telegram
import sqlite3 as lite
from core.utils import isAdmin

def modecb(bot,update,args):
    suid = update.message.from_user.id
    gid = update.message.chat_id
    #only an administrator can do that
    if not isAdmin(bot,suid,gid):
        return

    db,cur = SetupSession()
    try:
        username = update.message.reply_to_message.from_user.username
        userid = update.message.reply_to_message.from_user.id
    except AttributeError:
        update.message.reply_text(text="Usage:\nquoting the user you want to change mode\n/mode +o|-o")
        return

    RegisterUser(db,cur,userid,username)
    if args[0] == "+o":
        #promote_to_admin
        if not AdminInDb(db,cur,userid,gid):
            update.message.reply_text(text = username+" promoted to op")
            RegisterAdmin(db,cur,userid,gid)
        else:
            update.message.reply_text(text=username+" already Op")
    elif args[0] == "-o":
        if AdminInDb(db,cur,userid,gid):
            update.message.reply_text(text=username+" removed from op")
            RemoveAdmin(db,cur,userid,gid)

def opcb(bot, update):
    db,cur = SetupSession()
    username = update.message.from_user.username
    userid = update.message.from_user.id
    gid = update.message.chat_id
    RegisterUser(db,cur,userid,username)
    
    if AdminInDb(db,cur,userid,gid):
        print("promote to admin"+username)
        #promote_to_admin

def deop(bot,update):
    username = update.message.reply_to_message.from_user.username
    userid = update.message.reply_to_message.from_user.id
    gid = update.message.chat_id
    RegisterUser(db,cur,userid,username)
    RemoveAdmin(db,cur,userid,gid)
    #remove administrator

class op:
    name = "op"
    cb = opcb
    args = False
    desc = "Give OP rights"

class mode:
    name = "mode"
    cb = modecb
    args = True
    desc = "Change User mode +o | -o"
