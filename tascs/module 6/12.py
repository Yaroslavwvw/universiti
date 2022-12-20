lst = input()
f = lst.find('h')
l = lst.rfind('h')
c = list(lst.replace('h','H'))
c[f] = 'h'
c[l] = 'h'
print("".join(c))