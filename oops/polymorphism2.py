class Animal:
    def sound(self):
        return "Generic"
    
class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"
    

animals = [Animal().sound(), Dog().sound(), Cat().sound()]
for a in animals:
    print(a)