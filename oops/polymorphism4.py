class A:
    def __init__(self, a):
        self.a = a

    def show(self):
        print(self.a)

class B(A):
    def __init__(self, b):
        self.b = b 
    
    def show(self):
        print(self.b)

b = B(3)
a = A(5)

print("Class A: ")
a.show()
print("Class B: ")
b.show()