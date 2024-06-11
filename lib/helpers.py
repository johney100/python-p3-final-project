# lib/helpers.py
from models.__init__ import CURSOR, CONN
from models.show import Show
from models.network import Network

def seed_database():
    Show.drop_table()
    Network.drop_table()
    Show.create_table()
    Network.create_table()

seed_database()
print("Seeded database")

def exit_program():
    print("Goodbye!")
    exit()

def list_shows():
    shows = Show.get_all()
    for show in shows:
        print(show)

def create_show():
    name = input("Enter the show name: ")
    genre = input("Enter the show genre: ")
    network_id = input("Enter the network id: ")
    try:
        show = Show.create(name, genre, network_id)
        print(f'Success: {show}')
    except Exception as exc:
        print("Error creating show: ", exc)

def find_show_by_name():
    name = input("Enter the show's name: ")
    show = Show.find_by_name(name)
    print(show) if show else print(
        f'Show {name} not found')

    
def delete_show():
    #def delete_show():
    id_ = input("Enter the show's id: ")
    if show := Show.find_by_id(id_):
        show.delete()
        print(f'Show {id_} deleted')
    else:
        print(f'Show {id_} not found')

def create_network():
    name = input("Enter the network name: ")
    location = input("Enter the network location: ")
    
    
    try:
        network = Network.create(name, location)
        print(f'Success: {network}')
    except Exception as exc:
        print("Error creating network: ", exc)

def list_networks():
    network = Network.get_all()
    for network in network:
        print(network)

def delete_network():
    
    id_ = input("Enter the network id: ")
    if network := Network.find_by_id(id_):
        network.delete()
        print(f'Show {id_} deleted')
    else:
        print(f'Show {id_} not found')