lst = [int(x) for x in input().split()]
max_lst = lst.index(max(lst))
min_lst = lst.index(min(lst))
lst[min_lst], lst[max_lst] = lst[max_lst], lst[min_lst]
print("".join(str(lst)))