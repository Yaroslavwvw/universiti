a = int(input())
q = 0
w = 1
i = 1
while a > w:
    w, q = w+q, w
    i += 1
    if  a < w:
        print(-1)
        break
    elif a == w:
        print(i)