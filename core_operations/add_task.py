from support_operations import validate_description, validate_description, validate_due_date, validate_priority, validate_title
from support_operations.display_task_details import display_task_details

def validate_task_details(title, description, due_date, priority):
    # Validate title
    if not validate_title(title):
        return False

    # Validate description
    if not validate_description(description):
        return False

    # Validate due date format (YYYY-MM-DD)
    if not validate_due_date(due_date):
        return False

    # Validate priority
    if not validate_priority(priority):
        return False

    return True

def ask_task_details():

    while True:
        # Ask for task details
        title = input("Enter task title: ").strip()
        description = input("Enter task description: ").strip()
        due_date = input("Enter due date (YYYY-MM-DD): ").strip()
        priority = input("Enter priority (low/medium/high): ").strip().capitalize()

        # Validate task details
        if validate_task_details(title, description, due_date, priority):
            return title, description, due_date, priority
        else:
            print("Please re-enter the task details.")

# Add tasks
def add_task(tasks):

    # Ask for task details
    # Title
    title, description, due_date, priority = ask_task_details()

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
    display_task_details(task)

    return tasks