words = ["eat", "tea", "tan", "ate", "nat", "bat"]


def find_anagrams(word_list):
    anagrams = {}
    for word in word_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    anagrams_list = list(map(lambda x: sorted(x), list(anagrams.values())))
    anagrams_list = sorted(anagrams_list)
    return anagrams_list


print(find_anagrams(words))
