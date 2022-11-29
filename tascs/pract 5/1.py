def f():
    try:
        a = input('Введите имя файла с расширением: ')
        b = open(a, 'r')
        col = int(b.readline())
        st = list(map(int, b.readlines()))
        for i in range(col):
            st[i]
        if col != len(st):
            raise KeyError

    except ValueError:
        print("в списке присутствует не число")
    except KeyError:
        print("количество чисел не соответствует первому числу в списке")
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