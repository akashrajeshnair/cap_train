class A:
    def __init__(self, n):
        self.n = n

    def hello(self):
        print("Hello from A", self.n)

class B(A):
    def __init__(self, n):
        super().__init__(n)
    
    def hello(self):
        print("Hello from B", self.n)

class C(A):
    def __init__(self, n):
        super().__init__(n)
    
    def hello(self):
        print("Hello from C", self.n)

class D(B,C):
    def __init__(self, n):
        super().__init__(n)

    def hello(self):
        print("Hello from D", self.n)

x = D(4)
x.hello()