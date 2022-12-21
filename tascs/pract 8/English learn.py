import translate
import pymorphy2
from translate import Translator

morph = pymorphy2.MorphAnalyzer()
translator = Translator(from_lang="ru", to_lang="en")


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

    for str in file_source:
        file_res = file_res + " " + normal_str(str)
    return file_res


def dict_(file_res):
    a = list(file_res.split())
    dict_sample = {}
    for i in range(len(a)):
        dict_sample[a[i]] = a.count(a[i])
    return {k: v for k, v in sorted(dict_sample.items(), key=lambda item: item[1], reverse = True)}
def translate(dict):
    for state in dict.keys():
        print(f"{state} | {dict[state]} | {translator.translate(state)}")
def ful():
    return translate(dict_(normal_list()))

print(ful())