from User import User

def main():
    print("\n\n===============================================================================")
    print("\tPlease register your account")
    first_name = input("\tEnter your first name: ")
    last_name = input("\tEnter your last name: ")

    to_do_list = []
    user = User(first_name, last_name)
    print("\n\tWelcome!", user)

    option = int(print_menu())
    analyzeOption(option)
    while option != 6:
        option = int(print_menu())
        analyzeOption(option)

    print("\n BYE!!! ")


def analyzeOption(option):
    if option == 1:
        pass
        # Add to-do to to-do list
    elif option == 2:
        pass
        # Update to-do on to-do list
    elif option == 3:
        pass
        # View all to-dos
    elif option == 4:
        # Update the status of a to-do
        pass
    elif option == 5:
        pass
        # Delete to-do from to-do list
    elif option == 6:
        return
    else:
        print("Invalid option. Try again")


def print_menu():
    print("\n----------------------------------------------------------------")
    print("\n Please select an item from the menu")
    print("1. Add a task")
    print("2. Update a task")
    print("3. View all tasks")
    print("4. Update the status of a task ")
    print("5. Delete a task")
    print("6. Quit")
    return input(": ")


if __name__ == "__main__":
    main()
