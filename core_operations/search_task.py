from support_operations.display_task_details import display_task_details

# Search for tasks based on a keyword
def search_task(tasks):
    searchd_keyword = input("Enter a keyword to search for tasks: ").strip().lower()

    for task in tasks:
        if searchd_keyword in task["title"].lower() or searchd_keyword in task["description"].lower():
            print(f"Task found: {display_task_details(task)}")
            return
        
    print(f"No task found with the keyword '{searchd_keyword}'.")