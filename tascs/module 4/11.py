a = int(input())
f = 0
g = 0
b = int(input())
if (a + b) % 2 == 0:
    print('черный')
    f = 1
else :
    print("белый")
    f = 2
c = int(input())
x = int(input())
if (c + x) % 2 == 0:
    print('черный')
    g = 1
else :
    print("белый")
    g = 2
if f == g :
    print("da")
else :
    print('net')