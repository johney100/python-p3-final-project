#!/usr/bin/env python3
# lib/debug.py
from models.show import Show
from models.network import Network

from models.__init__ import CONN, CURSOR
def reset_database():
    Show.drop_table()
    Network.drop_table()
    Show.create_table()
    Network.create_table()



breakpoint()
