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
    delete_network
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_shows()
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


if __name__ == "__main__":
    main()
