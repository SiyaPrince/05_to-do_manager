# Update status of a task

from core_operations.view_tasks import view_tasks


def complete_task(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks(tasks)

    try:
        task_selection = int(input("\nSelect the task number to mark as complete: "))
    except ValueError:
        print("\nInvalid selection. Please enter a number.")
        return

    if task_selection < 1 or task_selection > len(tasks):
        print("\nInvalid task selection.")
        return

    selection_index = task_selection - 1
    task_to_complete = tasks[selection_index]

    if task_to_complete["status"] == "complete":
        print(f"Task '{task_to_complete['title']}' is already complete.")
        return

    task_to_complete["status"] = "Completed"
    print(f"\nTask '{task_to_complete['title']}' marked as complete.")
        

