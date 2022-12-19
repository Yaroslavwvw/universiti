import translate
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

translator = translate.Translator(from_lang="ru", to_lang="en")


def sort_dict(source):
    sorted_dict = {}
    for key in sorted(source, key=source.get, reverse=True):  # type: ignore
        sorted_dict.update({key: source[key]})
    return sorted_dict


def write(counted: dict[str, str], translated: dict[str, str], file: str) -> None:
    with open(file, "w", encoding="utf-8") as f:
        for k in counted:
            f.write(f"{k} | {translated[k]} | {counted[k]}\n")


def load_from_file(file: str) -> list[str]:
    words = []
    translation = str.maketrans(dict.fromkeys(map(ord, ".,!:?—-\"'0123456789«»"), None))
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                word = word.translate(translation)
                if word:
                    words.append(morph.parse(word)[0].normal_form)  # type: ignore

    return words


def main():
    words = load_from_file("data/dialog.txt")
    counted_words = {}
    for word in words:
        counted_words[word] = counted_words.get(word, 0) + 1

    counted_words = sort_dict(counted_words)

    translated_words = {}
    for k in counted_words:
        translated_words.update({k: translator.translate(k)})

    write(counted_words, translated_words, "data/8_results.txt")


if __name__ == "__main__":
    main()