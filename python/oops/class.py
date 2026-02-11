class Dog:
    species = "Canine"
    def __init__ (self, name, age):
        self.name = name
        self.age = age

d1 = Dog("Shiro", "3")
print(d1.name)
print(d1.age)
print(d1.species)

d2 = Dog("Goofy", "11")
print(d2.name)
print(d2.age)
print(d2.species)