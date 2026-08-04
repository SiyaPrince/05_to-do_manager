from support_operations.display_task_details import display_task_details

def validate_task_details(title, description, due_date, priority):
    # Validate title
    if not title:
        print("Task title cannot be empty.")
        return False

    # Validate description
    if not description:
        print("Task description cannot be empty.")
        return False

    # Validate due date format (YYYY-MM-DD)
    try:
        year, month, day = map(int, due_date.split('-'))
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError
    except ValueError:
        print("Invalid due date format. Please use YYYY-MM-DD.")
        return False

    # Validate priority
    if priority.lower() not in ["low", "medium", "high"]:
        print("Invalid priority. Please choose from low, medium, or high.")
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