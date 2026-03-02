s = int(input("Enter a 1st number :"))
p = int(input("Enter a 2nd number :"))
q = int(input("Enter a 3rd number :"))
r = int(input("Enter a 4th number :"))

if(s>p and s>q and s>r) :
    print("1st is gretest number of all :",s)

elif(p>s and p>q and p>r) :
    print("2nd is gretesr number of all :",p)

elif(q>s and q>p and q>r) :
    print("3nd is gretest number of all :",q)
    
else:
    print("4th is gretest number of all :",r)

