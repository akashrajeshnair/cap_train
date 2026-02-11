class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary

class SalesEmployee(Employee):
    def __init__(self, id, salary, sales, bonus, pf, advance, income):
        super().__init__(id, salary)
        self.sales = sales
        self.bonus = bonus
        self.pf = pf
        self.advance = advance
        self.income = income

id = input("Enter Employee Id: ")
salary = input("Enter salary: ")
sales = input("Enter sales: ")
bonus = input("Enter bonus: ")
pf = input("Enter pf: ")
advance = input("Enter advance: ")
income = input("Enter income: ")

s = SalesEmployee(id, salary, sales, bonus, pf, advance, income)
print(s.id)
print(s.salary)
print(s.sales)
print(s.bonus)
print(s.pf)
print(s.advance)
print(s.income)