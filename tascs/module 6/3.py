lst = [int(x) for x in input().split()]
count = len(lst)
for i in range(0, count - 1, 2):
    print(lst[i + 1], lst[i], end=" ")
if count % 2 != 0:
    print(lst[count - 1])