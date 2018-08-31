from User import User
from Todo import Todo, Status

'''Main function'''


def main():
    # Demand for user's details
    print("\n\n===============================================================================")
    print("\tPlease register your account")
    first_name = input("\tEnter your first name: ")
    last_name = input("\tEnter your last name: ")

    # Initialize to-do list and welcome user
    to_do_list = []
    user = User(first_name, last_name)
    print("\n\tWelcome!", user)

    # Get user's option after displaying menu and analyze the user's option
    option = int(print_menu())
    analyzeOption(option, to_do_list)
    # While the user's option is not 6, continue getting the user's option
    while option != 6:
        option = int(print_menu())
        analyzeOption(option, to_do_list)

    print("\n BYE!!! ")


# Analyse user's option based on what he/she entered
def analyzeOption(option, to_dos):
    if option == 1:
        to_dos += [add_todo()]
    elif option == 2:
        pass
        update_todo(to_dos)
    elif option == 3:
        list_todos(to_dos)
    elif option == 4:
        update_status(to_dos)
        pass
    elif option == 5:
        delete_todo(to_dos)
    elif option == 6:
        return
    else:
        print("Invalid option. Try again")


def add_todo():
    task = input("\nEnter task: ")
    time = input("Enter time (HH:MM): ")
    new_todo = Todo(task, time)
    return new_todo


# List all to-dos
def list_todos(to_dos):
    print("\n____________________________________________________________________\n")
    for to_do in to_dos:
        print(to_do)


# Update task's status
def update_status(to_dos):
    identifier = input("\nEnter the identifier: ")
    for to_do in to_dos:
        if to_do.getId() == int(identifier):
            print("Select a status")
            print("\t1. TODO\n\t2. DONE\n\t3. DOING")
            status = int(input(": "))
            while 1 < status < 3:

                if status == 1:
                    to_do.setStatus(Status.TODO)
                    return
                elif status == 2:
                    to_do.setStatus(Status.DONE)
                    return
                elif status == 3:
                    to_do.setStatus(Status.DOING)
                    return
                else:
                    print("Invalid option. Try Again!")


# Update a task on to-do list
def update_todo(to_dos):
    identifier = input("\nEnter the identifier: ")
    for to_do in to_dos:
        if to_do.getId() == int(identifier):
            task = input("Enter task: ")
            time = input("Enter time (HH:MM): ")
            to_do.setTask(task)
            to_do.setTime(time)
            return


# Delete task
def delete_todo(to_dos):
    identifier = input("\nEnter the identifier: ")
    for to_do in to_dos:
        if to_do.getId() == int(identifier):
            to_dos.remove(to_do)
            return


# Display menu and get user's option
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
