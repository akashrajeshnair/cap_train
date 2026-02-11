from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass

class English(Greet):
    def say_hello(self):
        return "Hello"
    
e = English()
print(e.say_hello())