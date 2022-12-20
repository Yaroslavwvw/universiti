lst = input()
a = len(lst)
print(lst[a // 2 + a % 2:],end="")
print(lst[: a // 2 + a % 2], sep="")