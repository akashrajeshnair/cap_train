class Animal:
    def speak(self):
        return "I am an animal"
    
class Dog(Animal):
    def speak(self):
        return "Woof"
    
print(Dog().speak())