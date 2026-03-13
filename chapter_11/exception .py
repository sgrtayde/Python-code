try:
    a = int(input("hey,enter the number : "))
    print(a)

except ValueError as v:
    print("heyyy")
    print(v)

except Exception as e:
    print(e)
    print("thank")
    