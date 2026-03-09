f = open("poem.txt")
data = f.read()
if("twinkle" in data):
    print(" The word twinkle is present in content")

else:
    print("The word is not present in the content")

f.close