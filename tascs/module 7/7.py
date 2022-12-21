import operator

db = {}

words_input_count = int(input())

for i in range(0, words_input_count):
    words = input().split()

    for word in words:
        if word in db:
            db[word] = str(int(db[word]) + 1)
        else:
            db[word] = str(1)

for name, count in sorted(db.items(), key=operator.itemgetter(1), reverse=True):
    print(name + ' ' + count)
