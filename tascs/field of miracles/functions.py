import random

spis = ["кника", "сесяц"]
slovo = list(random.choice(spis))
slovo1 = list("■"* len(slovo))
print((slovo))

#print(list(slovo1))

print(f'{"■ "* len(slovo)} | ♥ x3')
b = input("Введите букву или слово полностью: ")
for i in range(len(slovo)):
    if slovo[i] == b:
        slovo1[i] = b
        #slovo1 = slovo1.replace(slovo1[i], b, 1)
print(*slovo1, sep=' ')