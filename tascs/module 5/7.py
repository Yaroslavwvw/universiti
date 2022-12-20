i = int(input())
q = 0
w = 1
j = 1
while i > j:
    w, q = w+q, w
    if i == j+1:
        print(w)
    j += 1
