lst = [int(s) for s in input().split()]
for a in lst:
    if a % 2 != 0:
        print(a, end=" ")