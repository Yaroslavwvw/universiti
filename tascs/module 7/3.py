dict = {}

input_count = int(input())

for i in range(0, input_count):
    name, voice_count = input().split()

    if name in dict:
        dict[name] = str(int(voice_count) + int(dict[name]))
    else:
        dict[name] = voice_count

for name, voice_count in sorted(dict.items()):
    print(name + ' ' + voice_count)