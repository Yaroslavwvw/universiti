import random

F = open("text.txt", "r", encoding='UTF-8')
spis = F.read().split("\n")
def osn(life):
    #global slovo
    #global prov
    #global slovo1
    #global life

    slovo = list(random.choice(spis))
    prov = "".join(slovo)
    slovo1 = list("■"* len(slovo))
    print(f'{" ".join(slovo1)} | ♥ x {life}')
    print(prov)
    return slovo, prov, slovo1
life = 3
def ur():
    li = input("Выберите уровень игры лёгкий, средний или сложный: ")
    if li == "лёгкий":
        life = 7
    elif li == "средний":
        life = 5
    else:
        life = 3
    return life
sk = 0


def povtor(sk, prov):
    #global sk
    #global prov
    sk = 1
    povtor1 = input("Если хотите сыграть еще раз нажмите 1, если нет, нажмите 2: ")
    if povtor1 == '1':
        if len(spis) > 0:
            spis.remove(prov)
            if len(spis) > 0:
                return 1
            else:
                print("слова закончились")
                return 0
        else:
            print("слова закончились")
            return 0
    else:
        return 0
def f(life, sk, slovo, slovo1, prov):
    b = input("Введите букву или слово полностью: ")
    #global life
    #global sk
    l = False
    for i in range(len(slovo)):
        if slovo[i] == b:
            slovo1[i] = b
            l = True
            #slovo1 = slovo1.replace(slovo1[i], b, 1)
    if b == prov:
        print(*slovo, sep=' ')
        print("Вы выиграли! Приз в студию!")
        l = True
        return povtor(sk, prov)
    if l:
        if slovo == slovo1:
            print(*slovo, sep=' ')
            print("Вы выиграли! Приз в студию!")
            return povtor(sk, prov)
        else:
            print(*slovo1, sep=' ')
            print(f" | ♥ x{life}")
    else:
        life -= 1
        if life > 0:
            print("Неправильно. Вы теряете жизнь!")
            print(*slovo1, sep=' ')
            print(f" | ♥ x{life}")
        else:
            print("Вы проиграли;)")
            return povtor(sk, prov)

m = 0

def play(life, m, sk):
    #global m
    #global sk
    #global life
    life = ur()
    osn(life)
    while sk < 1:
        m = f(life, sk, osn())
    if m == 1:
        m = 0
        sk = 0
        life = 3
        play()
    else:
        print("Игра окончена!")
play(life, m, sk)

