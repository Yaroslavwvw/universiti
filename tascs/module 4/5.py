a = int(input())
b = int(input())
if (a > 0 or b > 0) or (a > 0 and b > 0):
    print("да")
elif a < 0 and b < 0:
    print("нет")