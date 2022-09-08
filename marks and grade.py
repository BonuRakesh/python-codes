a= int(input("enter marks in sub 1: "))
b= int(input("enter marks in sub 2: "))
c= int(input("enter marks in sub 3: "))
d= int(input("enter marks in sub 4: "))
e= int(input("enter marks in sub 5: "))
total=a+b+c+d+e
avg= total/5
if avg>=91 and avg<=100:
    print("grade is s")
elif avg>=81 and avg<=90:
    print("grade is A")
elif avg>=71 and avg<=80:
    print("grade is B")
elif avg>=61 and avg<=70:
    print("grade is c")
elif avg>=51 and avg<=60:
    print("grade is D")
elif avg<50:
    print("grade  is E")
