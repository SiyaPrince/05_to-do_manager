from support_operations.display_task_details import display_task_details

# View the list of tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\n The list of tasks:")
        for task in tasks:
            display_task_details(task)