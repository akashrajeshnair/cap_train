n = int(input("Enter length of the expression: "))
tokens = input("Enter the expression: ").split()

s = []

for token in tokens:
    if token in ['+', '-', '*', '/']:
        b = s.pop()
        a = s.pop()
        if token == '+':
            s.append(a + b)
        elif token == '-':
            s.append(a - b)
        elif token == '*':
            s.append(a * b)
        elif token == '/':
            s.append(int(a / b))
    else:
        s.append(int(token))

print(s[0])