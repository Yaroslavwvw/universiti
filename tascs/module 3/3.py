a = input()

n = (a.find("f"))
k = a.rfind("f")
print(n if n == k else f"{n}, {k}")