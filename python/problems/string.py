def is_valid_parenthesis_string(s: str) -> bool:
    left = 0  
    right = 0  
    for c in s:
        if c == '(':
            left += 1
            right += 1
        elif c == ')':
            left = max(left - 1, 0)
            right -= 1
        elif c == '*':
            left = max(left - 1, 0) 
            right += 1              
        else:
            continue
        if right < 0:
            return False
    return left == 0


data = input("Enter the parenthesis string: ")
s = ''.join(data.split())  
print("true" if is_valid_parenthesis_string(s) else "false")