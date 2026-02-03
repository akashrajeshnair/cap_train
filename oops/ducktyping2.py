class Cat:
    def speak(self):
        return "Meow"
    
class Dog:
    def speak(self):
        return "Woof"
    
def animal_speak(animal):
    return animal.speak()

print(animal_speak(Cat()))
print(animal_speak(Dog()))