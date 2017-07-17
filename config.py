from modules.commands.s0ng5 import s0ng
from modules.commands.pong import pong
from modules.commands.op import op,mode
from modules.commands.ban import ban,unban
from modules.commands.help import help

from modules.onjoin.notasciiname import no_ascii_name
from modules.onjoin.nobots import nobots

TOKEN=''
WHITELIST = []
#modules that don't need arguments

commands = [s0ng,pong,op,mode,ban,unban,help]

onjoin = [nobots,no_ascii_name]
