def read_data(path):
    file = open(path, encoding="utf8")
    data = file.read()
    return data


def format_text(text):
    rows = text.splitlines()
    rows = [i[i.index('. ') + 2:].replace(': ', ',') for i in rows]
    rows = sorted(rows)
    first_row = 'name,grade\n'
    new_text = first_row + '\n'.join(rows)
    return new_text


def write_data(path, data):
    file = open(path, "w", encoding="utf8")
    file.write(data)
    file.close()


write_data('output.csv', format_text(read_data('data.txt')))
