def is_ugly_num(n):
  past = set()
  while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return True
        past.add(n)
  return False
y= int(input("enter the number: "))
print(is_ugly_num(y))
