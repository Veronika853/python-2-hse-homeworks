def read_data(path):
    file = open(path, encoding="utf8")
    data = file.read()
    return data


def format_text(text):
    text = text.lower().replace('.', '').replace(',', '')
    words = text.split()
    words_count = dict.fromkeys(set(words), 0)
    for i in words:
        words_count[i] += 1
    sorted_words_count = sorted(words_count.items(), key=lambda x: [x[1], x[0]], reverse=True)
    top_words_count = sorted_words_count[:10]
    new_text = '\n'.join([f"{word},{count}" for word, count in top_words_count])
    return new_text


def write_data(path, data):
    file = open(path, "w", encoding="utf8")
    file.write(data)
    file.close()


write_data('output.txt', format_text(read_data('input.txt')))
