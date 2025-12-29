import timeit

data = list(range(1, 1000))

def quadratic():
    # O(n^2) — проверяем все пары
    result = []
    for i in data:
        for j in data:
            if i + j == 10:
                result.append((i,j))
    return result

def linear_with_set():
    # O(n) — используем множество для поиска дополнения
    result = []
    s = set(data)
    for x in data:
        if 10 - x in s:
            result.append((x, 10 - x))
    return result

# Проверка времени
for func in [quadratic, linear_with_set]:
    t = timeit.timeit(func, number=10)
    print(f"{func.__name__:20s} -> {t:.6f} сек")