from core_operations.view_tasks import view_tasks
from support_operations.display_task_details import display_task_details


def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.")
        return

    view_tasks(tasks)

    try:
        task_selection = int(input("\nSelect the task number to delete: "))
    except ValueError:
        print("Invalid selection. Please enter a number.")
        return

    if task_selection < 1 or task_selection > len(tasks):
        print("Invalid task selection.")
        return

    selected_index = task_selection - 1
    selected_task = tasks[selected_index]

    print("\nSelected task:")
    display_task_details(selected_task)

    confirmation = input(
        "\nDelete this task? (yes/no): "
    ).strip().lower()

    if confirmation in ("yes", "y"):
        deleted_task = tasks.pop(selected_index)
        print(f"Task '{deleted_task['title']}' deleted successfully.")
    elif confirmation in ("no", "n"):
        print("Deletion cancelled.")
    else:
        print("Invalid confirmation. Deletion cancelled.")