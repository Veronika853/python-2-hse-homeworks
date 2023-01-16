def read_data(path):
    file = open(path, encoding="utf8")
    data = file.read()
    return data


def format_text(text):
    rows = text.splitlines()
    indexes_keys = [i[i.index('KP') + 2:i.index(' - ')].replace('-', '.').split('.') for i in rows]
    indexes_keys = [[int(k) for k in i] for i in indexes_keys]
    row_index = list(zip(indexes_keys, rows))
    new_text = '\n'.join([i[1] for i in sorted(row_index)])
    return new_text


def write_data(path, data):
    file = open(path, "w", encoding="utf8")
    file.write(data)
    file.close()


write_data('output.txt', format_text(read_data('input.txt')))
