class LoanError(Exception):
    pass

try:
    s = int(input("Enter your salary: "))
    cs = int(input("Enter your credit score: "))
    if s < 25000:
        raise LoanError("Low Salary")
    elif cs < 700:
        raise LoanError("Low Credit Score")
    print("Loan Approved")
except LoanError as e:
    print(e)