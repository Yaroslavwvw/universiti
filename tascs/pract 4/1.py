F = open('data.txt', 'r', encoding='UTF-8')
st = list(map(str, F.readlines()))
#print(st)
#ss = '/?.,@#$^%&*()_-!"№;;%:?*<>|'
ss1 = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
new = []

def clear_sort(st):
    for i in range(len(st)):
        for j in st[i]:
            if j not in ss1:
                st[i] = st[i].replace(j, ' ')
        st[i] = st[i].lower()
        st[i] = st[i].split()
        for j in range(len(st[i])):
            if st[i][j]+'\n' not in new:
                new.append(st[i][j]+'\n')
    return new

clear_sort(st)

#def save_file(st):
#import sys
new_text = open("new_text.txt", mode='w')
new_text.write(f'Всего уникальных слов: {len(new)}\n')
new_text.write('\n')
for i in sorted(new):
    new_text.write(i)
print()
#print(st)
#print()
#print(new)