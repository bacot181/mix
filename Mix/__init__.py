import asyncio

import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

from config import *
from Mix.core import *
from Mix.mix_client import *

git()
heroku()
bot = Bot()
nlx = Userbot()


from team import *
from thegokil import DEVS, NO_GCAST

from langs import *
