class Demo:
    x = 25
    
    def __init__(self, a):
        self.a = a

d1 = Demo(20)
d2 = Demo(10)

print(d1.a, d1.x, d2.a, d2.x)