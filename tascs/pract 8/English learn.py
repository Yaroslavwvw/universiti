import translate
import pymorphy2
from translate import Translator

morph = pymorphy2.MorphAnalyzer()
translator = Translator(from_lang="ru", to_lang="en")
#text = str(input())
#end_text = translator.translate(text)
#import os, sys
# Выводит абсолютный путь программы D:\Папка_1\Папка_2\Папка_3.1\Программа.py
#print(os.path.abspath(__file__))
# Выводит путь к папке с программой D:\Папка_1\Папка_2\Папка_3.1\
#print(os.getcwd())
#print(os.listdir())


def normal_str(input_str):
    spis = input_str.split()
    res = []
    for i in spis:
        if "-" not in i:
            f = filter(str.isalpha, i)
            i = "".join(f)
        p = morph.parse(i)[0]
        res.append(p.normal_form)
    return ' '.join(res)

def normal_list():
    filename = "new"
    file_source = open(filename, encoding="UTF-8")
    file_res = ''
    #file_res = open(filename + "2.txt", "w", encoding="UTF-8")

    #def list_kol(F_list):
    #    F = open(F_list, 'r', encoding="UTF-8")
    #   st = F.readlines()
    #    print(st)

    for str in file_source:
        file_res = file_res + " " + normal_str(str)
        #print(file_res)
    #file_res.append(normal_str(str))
    #file_res.writelines(normal_str(str))
    return file_res


#print(normal_list())
def dict_(file_res):
    a = list(file_res.split())
    dict_sample = {}
    for i in range(len(a)):
        dict_sample[a[i]] = a.count(a[i])
    return {k: v for k, v in sorted(dict_sample.items(), key=lambda item: item[1], reverse = True)}
#print(dict_(normal_list()))
#print(dict_(normal_list()).keys())
def translate(dict):
    for state in dict.keys():
        print(f"{state} | {dict[state]} | {translator.translate(state)}")
#print(a, a.count("создать"))
#print(dict_sample)
#list_kol('new2.txt')
def ful():
    return translate(dict_(normal_list()))

print(ful())