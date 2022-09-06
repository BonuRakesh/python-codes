n1 = int(input('Enter first number : '))
n2 = int(input('Enter second number : '))

sum = n1 + n2
print('Sum =', sum)
def is_perfect_square(sum):
    x = sum // 2
    y = set([x])
    while x * x != sum:
        x = (x + (sum // x)) // 2
        if x in y: return False
        y.add(x)
    return True
print(is_perfect_square(sum))

