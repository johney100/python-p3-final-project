#!/usr/bin/env python3

from models.__init__ import CURSOR, CONN
from models.network import Network
from models.show import Show

def seed_database():
    Show.drop_table()
    Network.drop_table()
    Show.create_table()
    Network.create_table()

    abc = Network.create("ABC", "Los Angeles")
    nbc = Network.create("NBC", "New York")
    hbo = Network.create("HBO", "Los Angeles")
    Show.create("Modern Family", "Comedy", 2)
    Show.create("Friends", "Comedy", 2)
    Show.create("The Sopranos", "Drama", 1)

seed_database()
print("Seeded database")
