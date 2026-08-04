# Update task details
from core_operations.view_tasks import view_tasks
from support_operations.display_task_details import display_task_details
from support_operations.validate_title import validate_title
from support_operations.validate_description import validate_description
from support_operations.validate_due_date import validate_due_date
from support_operations.validate_priority import validate_priority


def update_task(tasks):

    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks(tasks)

    try:
        task_selection = int(input("\nSelect the task number to update: "))
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

    # Ask for new details
    new_title = input(
    f"Enter new title (leave blank to keep '{selected_task['title']}'): "
    ).strip()

    new_description = input(
        "Enter new description (leave blank to keep current): "
    ).strip()

    new_due_date = input(
        f"Enter new due date (leave blank to keep '{selected_task['due_date']}'): "
    ).strip()

    new_priority = input(
        f"Enter new priority (leave blank to keep '{selected_task['priority']}'): "
    ).strip().capitalize()

    # Update task details if provided
    if new_title:
        if not validate_title(new_title):
            print("Invalid title. Update cancelled.")
            return
        selected_task["title"] = new_title

    if new_description:
        if not validate_description(new_description):
            print("Invalid description. Update cancelled.")
            return
        selected_task["description"] = new_description

    if new_due_date:
        if not validate_due_date(new_due_date):
            print("Invalid due date. Update cancelled.")
            return
        selected_task["due_date"] = new_due_date

    if new_priority:
        if not validate_priority(new_priority):
            print("Invalid priority. Update cancelled.")
            return
        selected_task["priority"] = new_priority

    print(f"Task '{selected_task['title']}' updated successfully.")
    display_task_details(selected_task)
    return tasks
