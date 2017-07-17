from modules.commands.s0ng5 import s0ng
from modules.commands.pong import pong
from modules.commands.op import op,mode
from modules.commands.ban import ban,unban
from modules.commands.help import help

from modules.onjoin.notasciiname import no_ascii_name
from modules.onjoin.nobots import nobots

TOKEN=''
WHITELIST = []

#commands
commands = [s0ng,pong,op,mode,ban,unban,help]

#actions on user join
onjoin = [nobots,no_ascii_name]
