def get_words_in_txt():
    """получить слова из 5 букв и записать в новый блокнот, приведение к нижнему регистру"""
    lists = []
    with open('rus.txt', 'r', encoding="UTF-8") as file:
        for i in file:
            if len(i) == 6 and i[0] != '-':
                lists.append(i)
            if len(i) == 7 and i[0] == '-':
                lists.append(i[1:])

    with open('new_rus.txt', 'w', encoding="UTF-8") as file:
        for i in lists:
            file.write(i.lower())


def get_text():
    """получить слова из словаря"""
    list_word = []
    with open('new_rus.txt', 'r', encoding="UTF-8") as file:
        for i in file:
            list_word.append(i)
    return list_word
