# lib/cli.py
#!/usr/bin/env python3


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
        

def main_menu():
    print("Television Show Database")
    print("Type 0 to exit the program")
    print("Select the number of the network to see its shows:")
    list_networks()
    choice = input("> ")
    if choice == "0":
        exit_program()
    else:
        try:
            # Get network index (assuming numeric input)
            network_index = int(choice)
            network_details(network_index)
        except ValueError:
            print("Invalid choice. Please enter a number or 0 to exit.")

    
if __name__ == "__main__":
    main()
