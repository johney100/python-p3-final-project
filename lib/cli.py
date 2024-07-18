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
    network_loop,
    list_shows,
    shows_loop

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
    print(" Enter any show name to check it's details")
    
    networks = list_networks()
    shows = list_shows()
   
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
    elif any(show.name == choice for show in shows):
        find_show_by_name(choice)
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
            print(f"'{network_to_delete}' not found. Please try again.")



def find_show_by_name(choice):
    show = Show.find_by_name(choice)
    network = Network.find_by_id(show.network_id)

       
    print(f"Show Name: {show.name} | Genre: {show.genre} | Network: {network.name} ")

if __name__ == "__main__":
    main()
