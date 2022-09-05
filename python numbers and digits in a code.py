
alpha,string=0,"Rakesh123456"
for i in string:
    if (i.isalpha()):
        alpha+=1
print("Number of Digit is", len(string)-alpha)
print("Number of numbers is", alpha)
