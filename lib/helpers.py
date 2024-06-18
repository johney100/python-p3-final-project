# lib/helpers.py
from models.__init__ import CURSOR, CONN
from models.show import Show
from models.network import Network

#helpersd should return = pass objects to each other

def seed_database():
    Show.drop_table()
    Network.drop_table()
    Show.create_table()
    Network.create_table()

    abc = Network.create("ABC", "Los Angeles")
    nbc = Network.create("NBC", "New York")
    hbo = Network.create("HBO", "Los Angeles")

    Show.create("Modern Family", "Comedy", 2)
    Show.create("Simpsons", "Comedy", 1)
    Show.create("Sopranos", "Drama", 3)
    Show.create("Yellowstone", "Drama", 2)

seed_database()
print("Seeded database")

def exit_program():
    print("Goodbye!")
    exit()

#def list_shows():
#    shows = Show.get_all()
#    for show in shows:
#        print(show)
    
def list_shows():
    shows = Show.get_all()
    if shows:
        print("List of Shows:\n")
        print("***************\n ")
    for show in shows:
        print(f" -{show.name}") 
        print("\n ")
    print("***************\n ")


def create_show(sub_choice):
    name = input("Enter the show name: ")
    genre = input("Enter the show genre: ")
    network_id = sub_choice
    try:
        show = Show.create(name, genre, network_id)
        print(f'Success: {show.name} was added to the network')
    except Exception as exc:
        print("Error creating show: ", exc)

def find_show_by_name():
    name = input("Enter the show's name: ")
    show = Show.find_by_name(name)
    print(show) if show else print(
        f'Show {name} not found')

    
def delete_show(network, show_index):
    shows = network.shows()  # Assuming network has a shows() method
    if 0 <= show_index < len(shows):
        show = shows[show_index]
        show.delete()  # Assuming show object has a delete method
        print(f'Show {show.name} deleted')  # Show details for reference
    else:
        print("Invalid show number. Please try again.")


def create_network():
    name = input("Enter the network name: ")
    location = input("Enter the network location: ")
    
    
    try:
        network = Network.create(name, location)
        print(f'Success: {network}')
    except Exception as exc:
        print("Error creating network: ", exc)

def list_networks():
    networks = Network.get_all()
    print("\n   Networks \n ") 
    print("***************\n ")
    for i, network in enumerate(networks):
        print(f"{i+1}.{network.name} ") 
    print("\n***************\n ")

def find_network_by_id():
    name = input("Enter the show's name: ")
    network = Network.find_by_id(id)
    print(network.name) if network else print(
        f'Network id not found')
    
def network_details(network_index):
  """Displays details of a specific network and their shows (if any)"""
  network = Network.find_by_id(network_index)
  if network:
    print(f"\nDetails for network: {network.name}")
    shows = network.shows()  
    if shows:
      print("\n  Shows: \n ")
      for i, show in enumerate(shows):
            print(f"{i+1}.{show.name} ({show.genre})\n ")         
    else:
      print(f"  No shows found on {network.name}.")
    while True:
      print("\n  Options:")
      print(" Enter 'A' to Add Show")
      print(" Enter 'B' to go back to Main Menu")
      print(" Enter show number to delete show")
      sub_choice = input("Enter your choice: ")

      if sub_choice in ("A", "a"):
        create_show(network.id)
        # Code to add a show (call a separate function or implement logic here)
        break  # Exit sub-menu after adding a show
      elif sub_choice in ("B", "b"):
        break  # Exit sub-menu loop (back to main menu)
      elif sub_choice not in ("A", "a", "B", "b"):
        try:
            show_index = int(sub_choice) - 1  # Adjust for 0-based indexing
            if 0 <= show_index < len(shows):
                delete_show(network, show_index)  # Pass network and show index
            else:
                print("Invalid show number. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number or a valid option.")
      else:
        print("Invalid choice. Please enter 1 or 2.")

  else:
    print(f"Network with ID {network_index} not found.")
  

def delete_network():
    
    id_ = input("Enter the network id: ")
    if network := Network.find_by_id(id_):
        network.delete()
        print(f'Show {id_} deleted')
    else:
        print(f'Show {id_} not found')