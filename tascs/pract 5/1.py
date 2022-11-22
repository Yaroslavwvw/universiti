def f():
    try:
        a = input('Введите имя файла с расширением: ')
        b = open(a, 'r')
        col = b.readline()
        st = list(map(int, b.readlines()))
    except EOFError:
        print("ну зачем вы сделали мне EOF?")
    except FileNotFoundError:
        print("Такого файла не существует")
    except KeyboardInterrupt:
        print("вы отменили операцию")
    except:
        print("Фатальная ошибка")
    else:
        print(st)
f()