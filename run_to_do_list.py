from core_operations.add_task import add_task
from core_operations.delete_task import delete_task
from core_operations.search_task import search_task
from core_operations.view_tasks import view_tasks
from core_operations.update_task import update_task
from core_operations.complete_task import complete_task


def display_welcome_message():
    print("=" * 45)
    print("\nWelcome to the To-Do List Manager!")
    print("=" * 45)

def display_menu():
    print("\nPlease choose an option:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Search tasks")
    print("4. Update a task")
    print("5. Complete a task")
    print("6. Delete a task")
    print("7. Exit")

def run_to_do_list():
    # Create empty tasks list
    tasks = []

    # Display welcome message

    display_welcome_message()

    while True:
        # Display menu

        display_menu()

        # Ask for choice
        operation_choice = input("Please choose operation: ").strip().lower()
        print()

        if operation_choice == "1":
            #     Add
            tasks = add_task(tasks)
        elif operation_choice == "2":    
            # View
            view_tasks(tasks)
        elif operation_choice == "3":
            # Search
            search_task(tasks)
        elif operation_choice == "4":
            # Update
            update_task(tasks)
        elif operation_choice == "5":
            # Complete
            complete_task(tasks)
        elif operation_choice == "6":
            # Delete
            delete_task(tasks)

        elif operation_choice == "7":
            # Exit
            print("Exiting the To-Do List Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")