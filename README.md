Television Show App - Python CLI

Project Overview

This project provides a command-line interface (CLI) for managing a database of television shows and their associated networks. It leverages Python for development and connects to a database (implementation details likely reside in models/__init__.py).

Key Features

Network Management: Create, list, view details, and delete networks.
Show Management: Create, list, view details, and delete shows.
User Input: Interact with the application through the CLI.
Error Handling: Mechanisms to gracefully handle potential issues during database interactions or user input (specific implementation details might be found within the code itself).
Directory Structure

.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── show.py        
    │   └── network.py 
    ├── cli.py
    ├── helpers.py
Installation

Prerequisites: Ensure Python 3.x is installed (python3 --version or python --version).
Dependencies: Utilize pipenv to manage dependencies. Install pipenv following the instructions at https://pipenv.pypa.io/en/latest/installation.html and then run pipenv install within the project directory.
Usage

Run the application: 
Execute pipenv run python seed.py.
Execute pipenv run python cli.py.
Navigation: Use letters or numbers to make selections from the main menu.
Functionalities:

Create Network (C): Add a network with its name and location.
List Networks: Display a list of all networks in the database.
Select Network by Number: Choose a network from the list to view its details and associated shows (if any). You can also delete the network by entering its number.
Delete Network by Name: Enter the full name of the network to delete.
View Network Details: Provides information about the chosen network, including its name and any shows belonging to it.
List Shows (All): Displays a list of all shows currently in the database.
Find Show by Name: Enter the full name of a show to view its details, including genre and network.
Exit (E): Terminate the program.
Seeding the Database (Optional)

The project includes a script (seed_database.py, not provided here) to populate the database with some sample data (networks and shows) for initial testing. To run this script:

Navigate to the project directory.
Run pipenv run python seed_database.py (assuming the script exists). This creates the tables, seeds the database, and displays a confirmation message.
Functionality Details

While the specific implementation details might vary, the application likely comprises these core components:

Database Connectivity: Connects to a database (details in models/__init__.py).
Network Management: Functions for creating, listing, viewing details, and deleting networks.
Show Management: Functions for creating, listing, viewing details, and deleting shows.
User Input: Handles user input through the command line.
Error Handling: Mechanisms to address potential issues.
Customization and Further Development

This template provides a foundational structure. Feel free to customize it by:

Implementing additional functionalities for show and network management.
Refining the user interface for a more user-friendly experience.
Enhancing error handling for robustness.
Incorporating unit tests for code quality assurance.
I hope this enhanced README effectively outlines the project's functionalities and serves as a valuable guide for its use and potential expansion.