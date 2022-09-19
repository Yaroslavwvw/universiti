a = int(input())
b = int(input())
c = int(input())
k = 0
if a % 2 == 0:
    k += a // 2
else:
    k += a // 2 + 1
if b % 2 == 0:
    k += b // 2
else:
    k += b // 2 + 1
if c % 2 == 0:
    k += c // 2
else:
    k += c // 2 + 1

print(k)
