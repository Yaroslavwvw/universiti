lst = [int(x) for x in input().split()]
v = set()
for i in lst:
    if i not in v:
        print("нет")
        v.add(i)
    else :
        print("да")