# Update status of a task

def complete_task(tasks):
    # Ask for task title to mark as complete
    title = input("Enter the title of the task to mark as complete: ").strip()
    for task in tasks:
        if task["title"] == title:
            task["status"] = "complete"
            print(f"Task '{title}' marked as complete.")
            return tasks
    print(f"Task '{title}' not found.")
    return tasks


# Update task details

def update_task(tasks):
    # Ask for task title to update
    return tasks