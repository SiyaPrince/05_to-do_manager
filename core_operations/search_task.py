from support_operations.display_task_details import display_task_details

# Search for tasks based on a keyword
def search_task(tasks):
    if not tasks:
        print("No tasks avaliable!")
        return

    searched_keyword = input("Enter a keyword to search for tasks: ").strip().lower()
    
    if not searched_keyword:
        print("Search word cannot be empty")
        return

    found_tasks = []

    for task in tasks:
        if (searched_keyword in task["title"].lower()
            or searched_keyword in task["description"].lower()):
            found_tasks.append(task)

    if not found_tasks:
        print(f"No tasks found for the keyword '{searched_keyword}'.")
        return


    print(f"Found {len(found_tasks)} matching tasks.")

    for task in found_tasks:
        display_task_details(task)