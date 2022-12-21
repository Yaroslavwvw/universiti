a = int(input())
c = int(input())
b = int(input())
if a == b == c:
    print('3')
elif a != b == c:
    print('2')
elif a != c == b:
    print('2')
elif b != c == a:
    print('2')
elif a == b != c:
    print('2')
elif a != b != c:
    print('0')