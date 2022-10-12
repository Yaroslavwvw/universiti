def get_name():
    name = input("введите имя контакта: ")
    name = name.title()
    name = name.lstrip()
    name = name.rstrip()
    return name

def get_nam1():
    nam = input("Введите новый номер телефона: ")
    nam = nam.replace(' ', '').replace('-', '')
    if nam[0] == '9' and len(nam) == 10:
        nam = '+7' + nam
    if nam[0] == '8' and len(nam) == 11:
        nam = '+7' + nam[1:]
    if nam[0] == '8' and len(nam) == 11:
        nam = '+' + nam
    if nam[:2] == '+7' and len(nam) == 12:
        print("Номер успешно изменён!")
        return nam
    else:
        print("Неправильно набран номер")
        return get_nam1()

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
    print("Список контактов:")
    for i in dict:
        print(i, dict[i])

def menu():
    print("Выберите действие: \n1. Добавить контакт\n2. Показать список\n3. Выход\n4. Удалить контакт\n5. Редактировать номер")

def dell(dict, name):
    del dict[name]
    print("Контакт успешно удалён!")
    return dict1
def check_list(dict, name):
    if not(name in dict):
        print("Такого контакта не существует")
        return False
    else:
        return True

def fix_numb(dict, name, nam):
    if check_list(dict1, get_name()):
        dict[name] = nam
        print("Номер успешно изменён!")
        return dict
    else:
        print("Такого имени нет в списке контактов")





dict1 = {}
while True:
    menu()
    p = int(input())
    if  p == 1:
        get_contact(dict1, get_name(), get_nam())
    if  p == 2:
        show_contact(dict1)
    if  p == 3:
        print(("Спасибо за использование!"))
        break
        #get_contact("Спасибо за использование!")
    if p == 4:
        dell(dict1, get_name())
    if p == 5:
        fix_numb(dict1, get_name(), get_nam1())