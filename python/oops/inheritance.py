class Bird:
    def __init__ (self, name):
        self.name = name

    def disp_name(self):
        print(f"Bird name: {self.name}")

class Pigeon(Bird): #single inheritance
    def sound(self):
        print("Koo Koo")

class Messenger(Pigeon): #multi-level inheritance
    def message(self):
        print(f"{self.name} sends a message")

class Hungry:
    def hunger(self):
        print("Hungry")

class Crow(Bird, Hungry): #multiple inheritance
    def sound(self):
        print("Caw Caw")

p = Messenger("John")
p.disp_name()
p.sound()
p.message()

c = Crow("Raj")
c.disp_name()
c.sound()
c.hunger()