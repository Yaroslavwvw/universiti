a = int(input())
b = 0
while a != 0:
    c = int(input())
    if c != 0 and a < c:
       b += 1
    a = c
print(b)