a = int(input("Enter value of a :"))
b = int(input("Enter value of b :"))

if(b==0):
    raise ZeroDivisionError("not divide by zero is goes to infinite")
else:
    print(f"the division is {a/b}")