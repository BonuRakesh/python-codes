def simpleinterest(p,t,r):
    SI=(p*t*r)/100
    return SI
p=int(input("enter principle amount: "))
t=int(input("enter time period: "))
r=int(input("enter rate ofinterest: "))
SI=simpleinterest(p,t,r)

print("simple interest: {}".format(SI))
