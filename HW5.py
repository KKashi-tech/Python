# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("file.txt", "x+", encoding="utf-8") as new_file:
    while True:
        text = (input('Введите данные. Для окончания ввода оставьте строку пустой. '))
        if not text:
            break
        new_file.writelines(f"{text}\n")

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("task2", "r", encoding="utf-8") as file2:
    strings = sum(1 for _ in file2)
    lines = file2.readlines()
    for i, value in enumerate(lines, 1):
        words = len(value.split())
        print(f"Количество строк в файле: {strings}\nКоличество слов в строке {i + 1}: {words}")

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


def salaries():
    dict1 = {}
    with open("task3", "r+", encoding='utf-8') as file3:
        print('Орлов 20000\nКалымагин 10000\nКаштанов 15000\nМилявская 50000', file=file3)
        for line in file3:
            dict1[line.split()[0]] = float(line.split()[1])
        print('Следующие сотрудники получают менее 20 тысяч рублей: ')
        for name, sal in dict1.items():
            if sal < 20000:
                print(name)
        print(f"Средняя величина дохода: {sum(dict1.values()) / len(dict1)}")


salaries()

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый файл.

dict1 = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("task4_2", "w", encoding="utf-8") as file4:
    with open("task4", encoding="utf-8") as file4_1:
        file4.writelines([line.replace(line.split()[0], dict1.get(line.split()[0])) for line in file4_1])


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

with open("task5", "w+", encoding="utf-8") as file5:
    print(' '.join(map(str, [random.randint(0, 100) for i in range(10)])), file=file5)
with open("task5", "r", encoding="utf-8") as file5:
    for line in file5:
        print(line)
        print(f"Сумма чисел: {sum(map(int, line.split()))}")


# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

dict2 = {}
with open("task6", "r", encoding="utf-8") as file6:
    for line in file6:
        first, sec = line.split(':')
        sumall = sum(map(int, "".join([i for i in sec if i == " " or '9' >= i >= '0']).split()))
        dict2[first] = sumall
    print(dict2)

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json


with open("js.json", "w", encoding="utf-8") as js:
    with open("task7", "r", encoding="utf-8") as file7:
        profit = {i.split()[0]: int(i.split()[2]) - int(i.split()[3]) for i in file7}
        print(f"Прибыль каждой компании: {profit}")
        result = [profit, {'avg_profit': round(sum([int(a) for a in profit.values() if int(a) > 0]) / len([int(a)
                                                                        for a in profit.values() if int(a) > 0]), 2)}]
        print(result)
        json.dump(result, js, ensure_ascii=False, indent=4)
