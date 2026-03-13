a = int(input("Enter a second number : "))
b = int(input("Enter a anumber : "))

if(b == 0):
    raise ZeroDivisionError("hey our program is not ment to divide number b zero")

else:
    print(f"the divison a/b is {a/b}")


