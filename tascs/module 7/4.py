words_list = []
ans_word = ''
max_count = 0

input_count = int(input())

for i in range(0, input_count):
    inp = input().split(' ')

    for j in inp:
        words_list.append(j)

words_list = sorted(words_list)

for word in words_list:
    if words_list.count(word) > max_count:
        ans_word = word
        max_count = words_list.count(word)

print(ans_word)