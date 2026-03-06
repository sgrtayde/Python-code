def rem(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append (item.strip (word))
            return n
        
l = ["sagar", "harshal","ritesh","mukesh"]
print(rem(l,"mukesh"))