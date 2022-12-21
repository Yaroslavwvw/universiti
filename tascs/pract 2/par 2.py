import random
days = 336
def birthday(count,iter):
    paradox = 0
    for i in range(count):
        birth = [random.randint(1,days) for x in range(iter)]
        day = set(birth)
        if len(day) == len(birth):
            paradox += 1
    return f"""iterations: {count}
paradoxes percent: {paradox / count * 100} %"""


def montyhall(iter):
    x = 0
    у = 0
    Z = 0
    V = 0
    for i in range(iter):
        doors = [0, 1, 0]
        b = int(random.choice(doors))
        doors.remove(b)
        if 0 in doors:
            doors.remove(0)
        c = doors[0]
        if b == 1:
            x += 1
        else:
            у += 1
        if c == 0:
            V += 1
        else:
            Z += 1
    print(f'win percentage: {x / 100}% и  lose percentage: {у / 100}%')

    print(f'win percetage without changing mind : {Z / 100}% lose percetage without changing mind: {V / 100}%')