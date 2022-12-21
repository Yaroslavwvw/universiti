import os
keys = ['a', 'b', 'c']
values = [1, 2, 3, 4]

def createDict(keys, values):
    ddi = {}
    for i in range(len(keys)):
        try:
            ddi[keys[i]] = values[i]
        except IndexError:
            ddi[keys[i]] = "none"
    return ddi

print(createDict(keys, values))
print(dir())
print(os.getcwd())
print(__file__)