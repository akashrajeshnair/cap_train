class Calculator:
    def multiply(self, a=1, b=1, *args):
        res = a*b
        for num in args:
            res*=num
        return res
    
calc = Calculator()

print(calc.multiply())
print(calc.multiply(4))
print(calc.multiply(4,3))