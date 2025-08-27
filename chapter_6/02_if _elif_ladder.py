a = int(input("Enter your age:"))

if(a>18):
    print("you are above the age Of consent")
elif(a<0):
    print("you are entered envalid negative age")
elif(a==0):
    print("you are entered 0 which is not valide age")
else:
    print("you are below the age of consent")
print(a)