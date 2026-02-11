class ValidationError(Exception):
    pass

try:
    id = int(input("Enter student id: "))
    if len(str(id)) != 6:
        raise ValidationError
    else:
        print("Logged in.")
except ValueError:
    print("Id should only have digits.")
except ValidationError:
    print("Id should have only 6 digits.")