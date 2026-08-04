def validate_priority(priority):
    if priority.lower() not in ["low", "medium", "high"]:
        print("Invalid priority. Please choose from low, medium, or high.")
        return False
    return True