class A:
    def __init__(self, a):
        self.a = a

    def show(self):
        print(f"Hello from A... {self.a}")

class B:
    def __init__(self, b):
        self.b = b 
    
    def show(self):
        a = A(5)
        a.show()
        print(f"Hello from B... {self.b}")

b = B(20)
b.show()
