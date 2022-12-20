a = int(input())
c: dict[str, str] = dict([input().split() for c in range(a)])
f = int(input())
for c in range(a):
    for key, value in c.items():
        if f == key:
            print(value)
        elif f == value:
            print(key)
        else:
            continue