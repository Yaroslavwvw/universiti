lisst = input().split()
collection: dict[str, int] = {}
for i in lisst:
    n = collection.get(i, 0)
    print(n, end="")
    collection[i] = n + 1