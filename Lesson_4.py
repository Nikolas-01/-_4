#1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка
# (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);
print("Задача 1.")
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
print('Список: \n%s\nКоличество слов: %s\nИзначально слов: %s' % (list_names_random, len(list_names_random), len(list_names)))
print()
print()
###############################################################################
# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;

print("Задача 2. \nСамое популярное имя:")

def popular_name(list_names_random):
    # Создаем словарь, который считает количество упоминаний
    list_names_random = {a: list_names_random.count(a) for a in list_names_random}
    print(list_names_random) # для проверки - словарь с именем и количеством упоминаний

    # Создаем список со значениями
    values_list = []

    for values in list_names_random.values():
        values_list.append(values)

    # из списка со значениями выбираем максимальное значение,
    # создаем список из ключей, которым соответсвует максимальное значение
    popular_names_list = []

    for items, values in list_names_random.items():
        if values == max(values_list):
            popular_names_list.append(items)


    return popular_names_list

print('Имя:', popular_name(list_names_random))
print()


#########################################################################################################
# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.

def rare_letter(lst):
    lst = map(lambda x: x[0], lst)  # 'Список' из первых букв
    return Counter(lst).most_common()[-1:][0][0]

print(rare_letter(list_F))
list_F += ['xxxxxxxxx']  # Добавим редкую букву)
print(rare_letter(list_F))

print()
#########################################################################
# 4. В файле с логами найти дату самого позднего лога (по метке времени).

with open('log', mode='rt', encoding='utf-8') as f:
    text = f.read()
print(text, '\n')

text = text.split('\n')
last_log = max(text, key=lambda x: x[:23])
print('Cамый поздний лог:', last_log)
print('И его метка времени:', last_log[:23])
