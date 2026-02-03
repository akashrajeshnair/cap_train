class AgeError(Exception):
    pass

def set(age):
    if age < 0:
        raise AgeError("Age can't be negative")
    print(f"age = {age}")

try:
    set(-5)
except AgeError as e:
    print(e)