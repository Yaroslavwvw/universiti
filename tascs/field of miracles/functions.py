import random

spis = ["книга", "месяц"]
slovo = list(random.choice(spis))
print(slovo)

print(f'{"■ "* len(slovo)} | ♥ x3')
b = input("Введите букву или слово полностью: ")
for i in slovo:
    if i == b: