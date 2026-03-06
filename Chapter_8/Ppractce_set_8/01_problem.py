
def gratest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = 33
b = 66
c = 98

print(gratest(a,b,c))