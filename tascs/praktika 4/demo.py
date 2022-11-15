from codecs import open
from functools import cmp_to_key
from re import split
text = open("data.txt", "r", "utf-8")
s = text.read()
words = split('[\d\W]+', s)
d = {}
for w in words:
    if w != '':
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
items = list(d.items())
def comparator(a, b):
    x = str(a)
    y = str(b)
    t = len(x) if len(x) < len(y) else len(y)
    for j in range(t):
        if x[j] == y[j]:
            continue
        if x[j] != 'ё' and y[j] != 'ё':
            if x[j] < y[j]:
                return -1
            else:
                return 1
        elif x[j] == 'ё':
            if y[j] > 'е':
                return -1
            else:
                return 1
        elif y[j] == 'ё':
            if x[j] > 'е':
                return 1
            else:
                return -1
    if len(x) < len(y):
        return -1
    elif len(x) > len(y):
        return 1
    else:
        return 0
#items.sort(key=cmp_to_key(comparator))
for i in items:
    print(i)