from pdf2docx import *
from docx2pdf import *
from PIL import Image
import os



def Docx(catalog):
    print('Список файлов с расширением .pdf:')
    file_pdf = []
    files = os.listdir(catalog)
    count = 0
    for file in files:
        if '.pdf' in file:
            count = count + 1
            print(f'{count}. {file}')
            file_pdf.append(file)
    num1 = int(input('Введите номер файла для изменения ' '(чтобы изменить все файлы из данного католога введите 0): '))

    if num1 == 0:
        for file in file_pdf:
            pdf_file = fr'{catalog}\{file}'
            docx_file = fr'{catalog}\{file}'
            docx_file = docx_file.replace('.pdf', '.docx')
            parse(pdf_file, docx_file)
    else:
        pdf_file = fr'{catalog}\{file_pdf[num1 - 1]}'
        docx_file = fr'{catalog}\{file_pdf[num1 - 1]}'
        docx_file = docx_file.replace('.pdf', '.docx')
        parse(pdf_file, docx_file)


def PDF(catalog):
    print('Список файлов с расширением .Docx:')
    files = os.listdir(catalog)
    Docxfile = []
    count = 0
    for file in files:
        if '.docx' in file:
            count = count + 1
            print(f'{count}. {file}')
            Docxfile.append(file)
    num2 = int(input('Введите номер файла для изменения ' '(чтобы изменить все файлы из данного католога введите 0): '))

    if num2 == 0:
        for file in Docxfile:
            pdf_file = fr'{catalog}\{file}'
            docx_file = fr'{catalog}\{file}'
            pdf_file = pdf_file.replace('.docx', '.pdf')
            convert(docx_file, pdf_file)
    else:
        pdf_file = fr'{catalog}\{Docxfile[num2 - 1]}'
        docx_file = fr'{catalog}\{Docxfile[num2 - 1]}'
        pdf_file = pdf_file.replace('.docx', '.pdf')
        convert(docx_file, pdf_file)


def photo(catalog):
    print("Список файлов с расширением ('.jpeg', '.gif', '.png' ,'.jpg'):")
    files = os.listdir(catalog)
    photos = []
    count = 0
    for file in files:
        if ('.jpeg' in file) or ('.gif' in file) or ('.png' in file) or ('.jpg' in file):
            count = count + 1
            print(f'{count}. {file}')
            photos.append(file)
    num = int(input('Введите номер файла для преобразования '
                    '(чтобы преобразовать все файлы из данного католога введите 0): '))
    num2 = int(input('Введите параметры сжатия (от 0 до 100%): '))
    if num == 0:
        for file in files:
            image_path = file
            image_file = Image.open(image_path)
            image_file.save(image_path, quality=num2)
    else:
        image_path = photos[num - 1]
        image_file = Image.open(image_path)
        image_file.save(image_path, quality=num2)


def delete(catalog):
    num = int(input('Выберите действие:\n\n'
                    '1. Удалить все файлы начинающиеся на определённую подстроку\n'
                    '2. Удалите все файлы заканчивающиеся на определённую подстроку\n'
                    '3. Удалить все файлы содержащие определённую подстроку\n'
                    '4. Удалить все файлы по расширению\n'
                    'Введите номер действия: '))
    num2 = input('Введите подстроку: ')
    files = os.listdir(catalog)
    if num == 1:
        for file in files:
            if file.startswith(num2) == True:
                os.remove(fr"{catalog}\{file}")
                print(f'Файл: {file} успешно удалён!')
    if num == 2:
        for file in files:
            if (num2 + '.') in file:
                os.remove(fr"{catalog}\{file}")
                print(f'Файл: {file} успешно удалён!')
    if num == 3:
        for file in files:
            if (num2) in file:
                os.remove(fr"{catalog}\{file}")
                print(f'Файл: {file} успешно удалён!')
    if num == 4:
        for file in files:
            if ('.' + num2) in file:
                os.remove(fr"{catalog}\{file}")
                print(f'Файл: {file} успешно удалён!')


def menu():
    catalog = os.getcwd()
    num = int(input(f'\nТекущий каталог: {catalog}\n\n'
                    'Выберите действие:\n\n'
                    '0. Сменить рабочий каталог\n'
                    '1. Преобразовать PDF в Docx\n'
                    '2. Преобразовать Docx в PDF\n'
                    '3. Произвести сжатие изображений\n'
                    '4. Удалить группу файлов\n'
                    '5. Выход\n\n'
                    'Ваш выбор: '))
    if num == 0:
        pyt = input('Укажите путь к каталогу: ')
        if os.path.exists(pyt) == True:
            os.chdir(pyt)
        else:
            print('Такого каталога нет')
    if num == 1:
        Docx(catalog)
    if num == 2:
        PDF(catalog)
    if num == 3:
        photo(catalog)
    if num == 4:
        delete(catalog)
    if num == 5:
        return 0
    return menu()


menu()