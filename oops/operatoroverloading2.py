class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    
print(ComplexNumber(2, 3) + ComplexNumber(3, 4))