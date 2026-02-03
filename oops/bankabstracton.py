from abc import ABC, abstractmethod

class AbstractBank(ABC):
    def __init__(self, balance, time):
        self.balance = balance
        self.time = time

    @abstractmethod
    def interest(self):
        pass

class HDFC(AbstractBank):
    def __init__(self, balance, time):
        super().__init__(balance, time)

    def interest(self):
        return (self.balance*self.time*6)/100
    
class SBI(AbstractBank):
    def __init__(self, balance, time):
        super().__init__(balance, time)

    def interest(self):
        return (self.balance*self.time*8)/100

class ICICI(AbstractBank):
    def __init__(self, balance, time):
        super().__init__(balance, time)

    def interest(self):
        return (self.balance*self.time*7)/100

h = HDFC(10000, 5)
s = SBI(10000, 5)
i = ICICI(10000, 5)
print(h.interest())
print(s.interest())
print(i.interest())