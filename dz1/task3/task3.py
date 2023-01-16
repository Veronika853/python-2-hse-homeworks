def read_data(path):
    file = open(path, encoding="utf8")
    data = file.read()
    return data


def format_text(text, row_length):
    words = text.split()
    lines = []
    line = ""
    for word in words:
        if len(line + " " + word) <= row_length:
            line += " " + word
        else:
            lines.append(line.strip())
            line = word
    lines.append(line.strip())
    new_text = "\n".join(lines)
    return new_text


def write_data(path, data):
    file = open(path, "w", encoding="utf8")
    file.write(data)
    file.close()


write_data('output.txt', format_text(read_data('input.txt'), 40))
