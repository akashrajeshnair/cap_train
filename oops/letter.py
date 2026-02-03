vowels = 'aeiou'

c = input("Enter a letter: ")

if c in vowels:
    print("It is a vowel")
elif c.isalpha():
    print("It is a consonant")
else:
    print("Not an alphabet")