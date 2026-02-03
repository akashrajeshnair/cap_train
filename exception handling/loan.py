class LoanError(Exception):
    pass

try:
    l = int(input("Enter Salary: "))
    if l > 20000:
        print("Loan Approved")
    else:
        raise LoanError
except LoanError:
    print("Loan Rejected")