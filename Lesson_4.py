
import random
print()
print("Lesson 1. Селект 100 имен из списка")
list_names = 'Ник Гена Влад Иван Коля Гера Натали Дуня Виля Никита Сергей Виталий Сара Питр Витя Сева Элеонора Макс Володя Роджер'.split()
def name_n(list_names, n):
    '''
    :param list_names: список имен
    :param n: длина списка на выходе
    :return: список из 20 случайных имен
    '''
    list_names_random = []
    len_list = len(list_names)
    newName = ''
    for i in range(1, n + 1):
        # randomChoice - это случайное число в пределах длины начального списка,
        # случайным образом выбираем индекс
        randomChoice = random.randint(0, len_list-1)
        # newName - это случайное слово по индексу
        newName = list_names[randomChoice]
        # Добавляем случайное слово newName в список
        list_names_random.append(newName)
    return list_names_random
list_names_random = name_n(list_names, 100) # n == 100
print('Список: \n%s\nПолучилось слов: %s\nБыло: %s' % (list_names_random, len(list_names_random), len(list_names)))
print()
print()
###############################################################################
# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;

print("Lesson 2. \nПопулярное имя:"
          "Э")

def popular_name(list_names_random):
    # Словарь упоминаний
    list_names_random = {a: list_names_random.count(a) for a in list_names_random}
    print(list_names_random) # для проверки - словарь с именем и количеством упоминаний

    # Список
    values_list = []

    for values in list_names_random.values():
        values_list.append(values)

    # максимальное значение,
    # список из ключей, которым соответсвует максимальное значение
    popular_names_list = []

    for items, values in list_names_random.items():
        if values == max(values_list):
            popular_names_list.append(items)


    return popular_names_list

print('Популярные:', popular_name(list_names_random))
print()

print('Lesson 3.\nРедкая буква, с которой начинается имя:'
      'Э')



def get_most_rare_letter(items=[]):
    """
    :param items: item list to find out the most rarely occurred
    :return: one object from the item list
    """

    from operator import itemgetter
    if len(items) == 0:
        return 'Not existed'
    else:
        # get all first letters list
        first_letters_list = list(map(lambda x: x[0], items))

        # get the unique letters set
        first_letters_set = set(first_letters_list)

        # counts for each unique letter
        pairs = list(map(lambda x: (x, first_letters_list.count(x)), first_letters_set))
        sorted_pairs = sorted(pairs, key=itemgetter(1), reverse=False)
        print('General statistics: ', sorted_pairs)
        pair_min = sorted_pairs[0]
        return pair_min


min_counts_letter = get_most_rare_letter( get_random_items(test_list, 200))
print('The word with minimum counts: ', min_counts_letter)


def rare_letter(lst):
    lst = map(lambda x: x[0], lst)  # 'Список' из первых букв
    return Counter(lst).most_common()[-1:][0][0]

print(rare_letter(list_names))
list_F += ['xxxxxxxxx']  # Добавим редкую букву)
print(rare_letter(list_names))

print()

