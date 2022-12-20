lst = set(int(x) for x in input().split())
list = set(int(d) for d in input().split())
print(lst, list)
v = []
c = 0
for i in lst:
    for g in list:
        if i == g:
            v.append(i)
print(" ".join(map(str,v)))
