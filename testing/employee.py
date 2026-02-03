import pytest

class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Manager(Employee):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department

class Developer(Employee):
    def __init__(self, name, id, programming_language):
        super().__init__(name, id)
        self.programming_language = programming_language

def test_employee():
    emp = Employee("Alice", 101)
    assert (emp.name, emp.id) == ("Alice", 101)

def test_manager():
    mgr = Manager("Bob", 102, "Sales")
    assert (mgr.name, mgr.id, mgr.department) == ("Bob", 102, "Sales")

def test_developer():
    dev = Developer("Charlie", 103, "Python")
    assert (dev.name, dev.id, dev.programming_language) == ("Charlie", 103, "Python")