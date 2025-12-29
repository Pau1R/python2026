import timeit
import sys

setup = """
data_list = list(range(100_000))
data_dict = {i: i for i in range(100_000)}
data_set = set(range(100_000))
"""

tests = {
    # Списки
    "доступ по индексу в списке": ("x = data_list[50000]", "O(1)"),
    "добавление в конец списка": ("data_list.append(-1)", "O(1) амортизированное"),
    "удаление с конца списка": ("data_list.pop()", "O(1)"),
    "вставка в середину списка": ("data_list.insert(50000, -1)", "O(n)"),
    "удаление из середины списка": ("del data_list[50000]", "O(n)"),
    "поиск элемента в списке": ("99999 in data_list", "O(n)"),
    "копирование списка срезом": ("copy = data_list[:]", "O(n)"),
    "итерация по списку": ("for x in data_list: pass", "O(n)"),
    "сортировка списка": ("sorted(data_list)", "O(n log n)"),
    "создание списка из другой коллекции": ("list(range(100_000))", "O(n)"),
    "объединение списков": ("data_list + data_list", "O(n)"),
    "min/max/sum списка": ("min(data_list); max(data_list); sum(data_list)", "O(n)"),

    # Словари
    "доступ по ключу в словаре": ("x = data_dict[50000]", "O(1)"),
    "поиск по значению в словаре": ("50000 in data_dict.values()", "O(n)"),
    "копирование словаря": ("copy = data_dict.copy()", "O(n)"),
    "итерация по словарю": ("for k,v in data_dict.items(): pass", "O(n)"),
    "создание словаря из другой коллекции": ("dict((i,i) for i in range(100_000))", "O(n)"),

    # Множества
    "проверка принадлежности в множестве": ("50000 in data_set", "O(1)"),
    "пересечение множеств": ("data_set & set(range(50000,150000))", "O(min(len(s1),len(s2)))"),
    "вычитание множеств": ("data_set - set(range(50000))", "O(len(s2))"),
    "объединение множеств": ("data_set | set(range(50000))", "O(len(s1)+len(s2))"),
    "копирование множества": ("copy = data_set.copy()", "O(n)"),
    "итерация по множеству": ("for x in data_set: pass", "O(n)"),
}

print(f"{'Операция':45s} {'Время (сек)':15s} {'Big O':15s}")

for name, (stmt, big_o) in tests.items():
    t = timeit.timeit(stmt, setup=setup, number=500)
    
    print(f"{name:45s} {t:<15.6f} {big_o:15s}")