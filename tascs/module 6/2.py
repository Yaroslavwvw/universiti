lst = [int(s) for s in input().split()]
for a in range(len(lst)):
    if lst[a] > lst[a-1]:
        print(lst[a], end=" ")