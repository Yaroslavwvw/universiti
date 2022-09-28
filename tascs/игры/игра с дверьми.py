import random

winn1 = 0
fale1 = 0
winn2 = 0
fale2 = 0
for i in range(10000):
    a = [0, 1, 0]
    b = int(random.choice(a))
    a.remove(b)
    #print(a)
    if 0 in a:
        a.remove(0)
    #print(a)
    c = a[0]
    if c == 0:
        fale2 += 1
    else:
        winn2 += 1
    if b == 1:
        winn1 += 1
    else:
        fale1 += 1
    #print(b, c, a)
print(f'Процент выигрыша при замене выбора: {winn1/100}, а проигрыша: {fale1/100}')

print(f'Процент выигрыша без замены выбора: {winn2/100}, а проигрыша: {fale2/100}')