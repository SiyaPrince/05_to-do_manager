# Delete task from the list of tasks
from core_operations import search_task
from core_operations.view_tasks import view_tasks


def delete_task(tasks):
    # Ask for task title to delete
    title = input("Enter the title of the task to delete: ").strip()
    to_be_deleted_task = []

    for task in tasks:
        if task["title"] == title:
            to_be_deleted_task.append(task)
        else:
            print(f"Task '{title}' not found.")

    view_tasks(to_be_deleted_task)

    print("\n Which task would you like to delete?")

    if search_task(to_be_deleted_task):
        tasks.remove(search_task(to_be_deleted_task))

