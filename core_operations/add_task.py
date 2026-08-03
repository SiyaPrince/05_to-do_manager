from support_operations.display_task_details import display_task_details

# Add tasks
def add_task(tasks):

    # Ask for task details
    # Title
    title = input("Enter task title: ").strip()
    # Description
    description = input("Enter task description: ").strip()
    # Due date
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    # Priority
    priority = input("Enter priority (low/medium/high): ").strip()

    # Create task dictionary
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "status": "pending"
    }

    # Append task to tasks list
    tasks.append(task)

    # Print confirmation message

    # Print successful addition message
    print("\nTask added successfully!")

    # Display the added task details
    display_task_details(tasks[-1])

    return tasks