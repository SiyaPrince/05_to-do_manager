def validate_description(description):
    if not description:
        print("Task description cannot be empty.")
        return False
    return True