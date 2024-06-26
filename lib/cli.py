# lib/cli.py
#!/usr/bin/env python3
from models.__init__ import CURSOR, CONN
from models.show import Show
from models.network import Network


from helpers import (
    exit_program,
    list_shows,
    create_show,
    find_show_by_name, 
    delete_show,
    create_network,
    list_networks,
    delete_network,
    network_details
)


def main():
    while True:
        main_menu()
        
"""
        elif choice == "2":
            find_show_by_name()
        elif choice == "3":
            create_show()
        elif choice == "4":
            delete_show()
        elif choice == "6":
            list_networks()
        elif choice == "7":
            create_network()
        elif choice == "10":
            delete_network()
        else:
            print("Invalid choice")
"""
def main_menu():
    print("\n------------- ")
    print("TELEVISION SHOW APP")
    print("-------------\n ")
    print("Type E to exit the program")
    print("Select the number of the network to see its shows:")
    print(" Enter network name to delete network")
    
    list_networks()
    choice = input("> ")
    if choice in ("E", "e"):
        exit_program()
    else:
        try:
            # Get network index (assuming numeric input)
            network_index = int(choice)
            network_details(network_index)
        except ValueError:
            print("Invalid choice. Please enter a number or 0 to exit.")

""" this code is needed to grab the 

while True:
        try:
          owner_index = int(input("Enter owner number: ")) - 1
          display_owner_details(owner_index)
"""    

"""
def network_menu():
    print("Type 7 to add a new network")
    print("Type 8 to find a network by name")
    print("Type 9 to view networks by location")
    print("Type 10 to delete a network")
"""
"""
def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all shows")
    print("2. Find show by name")
    print("3. Add new show")
    print("4. Delete show")
    print("5. View shows by network")
    print("6. List all networks")
    print("7. Add new network")
    print("8. Find network by name")
    print("9. View networks by location")
    print("10. Delete network")

"""
    
if __name__ == "__main__":
    main()
