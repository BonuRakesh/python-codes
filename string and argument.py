import re
p = re.compile("[watch]")
for m in p.finditer('what'):
    print(m.start(), m.group())
count = 0
for count, i in enumerate(range(5),1):
    print(i)
print(count)

