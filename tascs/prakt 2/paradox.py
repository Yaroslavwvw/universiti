import random
days = 336

def birthday(count,nem):
    paradox = 0
    for i in range(count):
        mons = [random.randint(1,days) for x in range(nem)]
        day = set(mons)
        if len(day) == len(mons):
            paradox += 1
    return f"iterations: {count} \nparadoxes percent: {paradox / count * 100} %"


def monty_hall(nem):
    A = 0
    B = 0
    S = 0
    N = 0
    for i in range(nem):
        dveeer = [0, 1, 0]
        b = int(random.choice(dveeer))
        dveeer.remove(b)
        if 0 in dveeer:
            dveeer.remove(0)
        c = dveeer[0]
        if b == 1:
            A += 1
        else:
            B += 1
        if c == 0:
            N += 1
        else:
            S += 1
    print(f'win percentage: {A / 100}% и  lose percentage: {B / 100}%')
    print(f'win percetage without changing mind : {S / 100}% lose percetage without changing mind: {N / 100}%')
