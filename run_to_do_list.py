from core_operations.add_task import add_task
from core_operations.delete_task import delete_task
from core_operations.search_task import search_task
from core_operations.view_tasks import view_tasks
from core_operations.update_task import update_task
from core_operations.complete_task import complete_task
from support_operations.display_menu import display_menu
from support_operations.display_welcome import display_welcome_message


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