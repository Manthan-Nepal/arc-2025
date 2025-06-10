# def check_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     else:
#         print(f"Age {age} is valid.")

# try:
#     user_age = -5 
#     check_age(user_age)
# except ValueError as e:
#     print(f"Validation Error: {e}")


class ValidationError(Exception):
    pass

def validate_status(status):
    valid_statuses = ['pending', 'in progress', 'done']
    if status not in valid_statuses:
        raise ValidationError(f"Invalid status: '{status}'. Valid statuses are: {valid_statuses}")


try:
    validate_status('completed')  # invalid status
except ValidationError as e:
    print(f"Error: {e}")
