lst = [int(x) for x in input().split()]
list = [int(d) for d in input().split()]
c = 0
for i in range(len(lst)):
    for g in range(len(list)):
        if lst[i] == list[g]:
            c += 1
            break
print(c)