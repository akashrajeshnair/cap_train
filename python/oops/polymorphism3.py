class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def jumping_jacks(self):
        print("Enjoying Jumping Jacks")

    def beach(self):
        if self.age < 10:
            print("Not allowed to go to the beach")
        else:
            print("Enjoying the beach")

    def drinking(self):
        if self.age < 21:
            print("Not allowed to drink")
        else:
            print("Enjoying drinking")   

    def party(self):
        if self.age < 25:
            print("Not allowed in the party")
        else:
            print("Enjoying the party")

    def temple(self):
        if self.age < 30:
            print("Not interested in temple")
        else:
            print("Enjoying the temple")

name = input("Enter name: ")
age = int(input("Enter age: "))
p = Person(name, age)
p.jumping_jacks()
p.beach()
p.drinking()
p.party()
p.temple()