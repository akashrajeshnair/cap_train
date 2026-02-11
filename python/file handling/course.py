class CourseError(Exception):
    pass

try:
    n = input("Enter name: ")
    selc = int(input("Enter number of courses selected: "))
    maxc = int(input("Enter maximum courses allowed: "))
    if selc < 0:
        raise ValueError
    elif selc > maxc:
        raise CourseError
except ValueError:
    print("Courses have to be more than 0.")
except CourseError:
    print("Course limit exceeded.")