F = open('data.txt', 'r', encoding='UTF-8')
st = list(map(str, F.readlines()))
#print(st)
ss = '/?.,@#$^%&*()_-!"№;;%:?*<>|'
ss1 = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
new = []

for i in range(len(st)):
    for j in st[i]:
        if j not in ss1:
            st[i] = st[i].replace(j, ' ')
    st[i] = st[i].lower()
    st[i] = st[i].split()
    for j in range(len(st[i])):
        if st[i][j]+'\n' not in new:
            new.append(st[i][j]+'\n')

print(st)
print(new)