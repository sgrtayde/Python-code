a1 = "buy this "
a2 = "click this"
a3 = "make a lot of money"
a4 = "subscrabe this"

massage = input("Enter your comment :")

if((a1 in massage) or (a2 in massage) or (a3 in massage) or (a4 in massage)) :
    print("This comment is a spam")
    
else :
    print("This is not a spam")
