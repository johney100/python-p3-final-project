# lib/cli.py
#!/usr/bin/env python3
from models.__init__ import CURSOR, CONN
from models.show import Show
from models.network import Network


from helpers import (
    exit_program,
    create_network,
    list_networks,
    network_details,
    network_loop

)


def main():
    while True:
        main_menu()
        

def main_menu():
    print("\n------------- ")
    print("TELEVISION SHOW APP")
    print("-------------\n ")
    print("Type E to exit the program")
    print("Select the number of the network to see its shows:")
    print(" Enter network name to delete network")
    print(" Enter C to create network")
    
    networks = list_networks()
    choice = input("> ")
    if choice in ("E", "e"):
        exit_program()
    elif choice in ("C", "c"):
        create_network()
    elif choice.isdigit():
        try:
            # Get network index (assuming numeric input)
            
            network_index = int(choice)
            if 0 <= network_index - 1 < len(networks):
                network = networks[network_index - 1]
                network_details(network)
                shows_loop(network)
                network_loop(network)
            else:
                print(f"There is no network with the number [{choice}] on this list. Please try again.")

        except ValueError:
            print("Invalid choice. Please enter a network number or E to exit.")
    else: 
        
        network_to_delete = choice.upper()
        # Find network by name and delete if found
        network = Network.find_by_name(network_to_delete)
        if network:
            for show in network.shows():
                show.delete()
            network.delete_network()
            print(f"Network '{network_to_delete}' deleted successfully.")
        else:
            print(f"Network '{network_to_delete}' not found. Please try again.")


def shows_loop(network): 
    shows = network.shows() 
    if shows:
      print("\nShows")
      print("***************")
      for i, show in enumerate(shows, start=1):
            print(f"{i}.{show.name} ({show.genre})\n ")  
      print("\n***************\n ")
    else:
      print(f"  No shows found on {network.name}.")

if __name__ == "__main__":
    main()
