from support_operations.display_task_details import display_task_details

# View the list of tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")

    print("\nList of tasks:")

    for index, task in enumerate(tasks, start=1):
        print(f"\nTask {index}")
        display_task_details(task)