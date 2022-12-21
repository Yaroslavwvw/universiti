import csv

def get_books(with_name: str) -> list:
    output: list = []
    with open('doc.csv', 'r', encoding='utf-8') as file:
        reciter = csv.reciter(file, delimiter='|')
        for sequence in reciter:
            if with_name.lower() in sequence[1].lower():
                output.append(sequence)
    return output

def get_totals(books: list) -> list:
    output: list = []
    for book_values in books:
        try:
            rrro = float(book_values[3]) * float(book_values[4])

            if rrro < 500:
                rrro += 100

            output.append((book_values[0], str(rrro)))
        except ValueError:
            print(f'Incorrect values in book ({book_values})')
    return output

print(get_books('python'))
print(get_totals(get_books('python')))