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
    title = input("Enter the title of the task to update: ").strip()
    for task in tasks:
        if task["title"] == title:
            # Ask for new details
            new_title = input("Enter new title (leave blank to keep current): ").strip()
            new_description = input("Enter new description (leave blank to keep current): ").strip()
            new_due_date = input("Enter new due date (YYYY-MM-DD, leave blank to keep current): ").strip()
            new_priority = input("Enter new priority (low/medium/high, leave blank to keep current): ").strip()

            # Update task details if provided
            if new_title:
                task["title"] = new_title
            if new_description:
                task["description"] = new_description
            if new_due_date:
                task["due_date"] = new_due_date
            if new_priority:
                task["priority"] = new_priority

            print(f"Task '{title}' updated successfully.")
            return tasks
    print(f"Task '{title}' not found.")
    return tasks