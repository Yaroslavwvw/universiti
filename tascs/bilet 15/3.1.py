import os


catalog = os.getcwd()
otvet = input(f'Вы находитесь в каталоге {catalog}\nСменить каталог ?\nНапишите "да" или "нет"\n')
if otvet == 'да':
    otvet = input('Укажите корректный путь к существующему каталогу: ')
    if os.path.exists(otvet) == True: #проверяет, существует ли каталог
        os.chdir(otvet) #изменяет католог на тот , что ввели в консоль
        catalog = os.getcwd()
        print(f'Текущий каталог:{catalog}')
    else:
        print('Такого каталога не существует')
if otvet == 'Нет':
    print('Каталог остался таким же')

files_list = os.listdir(catalog) #список с именами файлов
sch = 0
for file in files_list:
    sch = sch + 1
    print(f'{sch}. {file}')

puttern = input('Введите паттерн: ')
rasshirenie = input('Введите расширение: ')
num = ''
k = 0
for file in files_list:
    if rasshirenie in file:
        lis = []
        for b in file:
            if b != '.':
                lis.append(b)
            if b == '.':
                break
        lis = ''.join(lis)
        file2 = file.replace(lis, f'{puttern}{num}')
        os.rename(fr'{catalog}\{file}', fr'{catalog}\{file2}')
        k = k + 1
        num = f'_{k}'
