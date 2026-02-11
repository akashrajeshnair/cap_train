class Person:
    def __init__ (self, name, age, phone, email, address, aadhaar):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email
        self.address = address
        self.aadhaar = aadhaar
    
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.email}\nAadhaar: {self.aadhaar}")

name = input("Enter name: ")
age = int(input("Enter age: "))
phone = int(input("Enter phone no.: "))
email = input("Enter email: ")
address = input("Enter address: ")
aadhaar = int(input("Enter aadhaar no.: "))

p = Person(name, age, phone, email, address, aadhaar)
p.display()