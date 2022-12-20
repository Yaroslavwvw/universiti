a = 1
b = 0
c = 0
d = 0
number = int(input())
while number > 0:
    if c == number:
        d += 1
    else:
        d = 1
    if d != 1 and d > a:
        a = d
    c = number
    number = int(input())

print(a)