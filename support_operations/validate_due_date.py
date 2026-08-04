def validate_due_date(due_date):
    try:
        year, month, day = map(int, due_date.split('-'))
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError
    except ValueError:
        print("Invalid due date format. Please use YYYY-MM-DD.")
        return False
    return True