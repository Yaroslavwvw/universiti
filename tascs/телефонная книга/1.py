def get_name():
    name = input("введите имя контакта: ")
    name = name.title()
    name = name.lstrip()
    name = name.rstrip()
    return name

def get_nam():
    nam = input("Введите номер телефона: ")
    nam = nam.replace(' ', '').replace('-', '')
    if nam[0] == '9' and len(nam) == 10:
        nam = '+7' + nam
    if nam[0] == '8' and len(nam) == 11:
        nam = '+7' + nam[1:]
    if nam[0] == '8' and len(nam) == 11:
        nam = '+' + nam
    if nam[:2] == '+7' and len(nam) == 12:
        return nam
    else:
        print( "Неправильно набран номер")
        return get_nam()

def get_contact(dict, name, nam):
    dict[name] = nam
    print("Контакт успешно добавлен!")

    return dict

def show_contact(dict):
    print()
    for i in dict:
        print(i, dict[i])

def menu():
    print("Выберите действие: \n1. Добавить контакт\n2.Показать список\n3. Выход")

dict1 = {}
while True:
    menu()
    p = int(input())
    if  p == 1:
        get_contact(dict1, get_name(), get_nam())
    if  p == 2:
        get_contact(dict1)
    if  p == 3:
        get_contact("Спасибо за использование!")