"""
Наглядные примеры различных сложностей алгоритмов Big O
"""

import time
import random

# O(1) - Константная сложность
def get_first_element(arr):
    """Всегда выполняется за одно и то же время"""
    return arr[0] if arr else None

# O(log n) - Логарифмическая сложность
def binary_search(arr, target):
    """Двоичный поиск в отсортированном массиве"""
    left, right = 0, len(arr) - 1
    operations = 0
    
    while left <= right:
        operations += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return f"Найдено за {operations} операций"
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return f"Не найдено за {operations} операций"

# O(n) - Линейная сложность
def linear_search(arr, target):
    """Поиск перебором всех элементов"""
    operations = 0
    for i, elem in enumerate(arr):
        operations += 1
        if elem == target:
            return f"Найдено за {operations} операций"
    return f"Не найдено за {operations} операций"

# O(n log n) - Линейно-логарифмическая сложность
def merge_sort(arr):
    """Сортировка слиянием"""
    operations = 0
    
    def merge(left, right):
        nonlocal operations
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            operations += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def merge_sort_recursive(lst):
        nonlocal operations
        if len(lst) <= 1:
            return lst
        
        mid = len(lst) // 2
        left = merge_sort_recursive(lst[:mid])
        right = merge_sort_recursive(lst[mid:])
        return merge(left, right)
    
    sorted_arr = merge_sort_recursive(arr)
    return sorted_arr, f"Отсортировано за {operations} операций"

# O(n²) - Квадратичная сложность
def bubble_sort(arr):
    """Пузырьковая сортировка"""
    operations = 0
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            operations += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr, f"Отсортировано за {operations} операций"

# O(2^n) - Экспоненциальная сложность
def fibonacci_recursive(n):
    """Рекурсивное вычисление чисел Фибоначчи"""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# O(n!) - Факториальная сложность
def permutations(arr):
    """Генерация всех перестановок"""
    if len(arr) <= 1:
        return [arr]
    
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for perm in permutations(rest):
            result.append([arr[i]] + perm)
    
    return result

# Демонстрация работы
def demonstrate_big_o():

    print("=== Краткое описание ===")
    print("• O(1) - не зависит от размера данных")
    print("• O(log n) - растет очень медленно, удвоение данных добавляет 1 операцию")
    print("• O(n) - растет прямо пропорционально размеру данных")
    print("• O(n log n) - немного хуже линейного, но все еще эффективен")
    print("• O(n²) - быстро становится непрактичным для больших данных")
    print("• O(2^n) - экспоненциальный рост, пригоден только для малых n")
    print("• O(n!) - факториальный рост, самый быстрорастущий, крайне непрактичен")


    print("\n\n=== Демонстрация сложностей алгоритмов Big O ===\n")
    
    # Создаем тестовые данные
    sizes = [100, 1000, 10000]
    
    print("1. O(1) - Константная сложность:")
    for size in sizes:
        arr = list(range(size))
        start = time.time()
        result = get_first_element(arr)
        end = time.time()
        print(f"   Размер: {size:5d}, Время: {(end-start)*1000000:.2f} мкс, Результат: {result}")
    
    print("\n2. O(log n) - Логарифмическая сложность (двоичный поиск):")
    for size in sizes:
        arr = list(range(size))
        target = size - 1  # Ищем последний элемент
        start = time.time()
        result = binary_search(arr, target)
        end = time.time()
        print(f"   Размер: {size:5d}, Время: {(end-start)*1000000:.2f} мкс, {result}")
    
    print("\n3. O(n) - Линейная сложность (линейный поиск):")
    for size in sizes:
        arr = list(range(size))
        target = size - 1  # Ищем последний элемент
        start = time.time()
        result = linear_search(arr, target)
        end = time.time()
        print(f"   Размер: {size:5d}, Время: {(end-start)*1000000:.2f} мкс, {result}")
    
    print("\n4. O(n log n) - Линейно-логарифмическая сложность (сортировка слиянием):")
    test_sizes = [100, 1000, 5000]
    for size in test_sizes:
        arr = [random.randint(0, 1000) for _ in range(size)]
        start = time.time()
        sorted_arr, operations = merge_sort(arr)
        end = time.time()
        print(f"   Размер: {size:5d}, Время: {(end-start)*1000:.2f} мс, {operations}")
    
    print("\n5. O(n²) - Квадратичная сложность (пузырьковая сортировка):")
    test_sizes = [100, 500, 1000]
    for size in test_sizes:
        arr = [random.randint(0, 1000) for _ in range(size)]
        start = time.time()
        sorted_arr, operations = bubble_sort(arr)
        end = time.time()
        print(f"   Размер: {size:5d}, Время: {(end-start)*1000:.2f} мс, {operations}")
    
    print("\n6. O(2^n) - Экспоненциальная сложность (Фибоначчи):")
    for n in [10, 20, 30, 35]:
        start = time.time()
        result = fibonacci_recursive(n)
        end = time.time()
        print(f"   n = {n:2d}, Время: {(end-start):.4f} с, F({n}) = {result}")
    
    print("\n7. O(n!) - Факториальная сложность (перестановки):")
    for n in [3, 4, 5, 6, 7, 8]:
        start = time.time()
        perms = permutations(list(range(1, n + 1)))
        end = time.time()
        print(f"   n = {n}, Перестановок: {len(perms):5d}, Время: {(end-start)*1000:.2f} мс")


def print_growth_table():
    print("=== Таблица роста операций для разных сложностей ===")
    header = f"{'n':>4} {'O(1)':>6} {'O(log n)':>8} {'O(n)':>6} {'O(n log n)':>10} {'O(n²)':>6} {'O(2^n)':>8}"
    print(header)
    print("-" * len(header))
    
    for n in [1, 2, 5, 10, 20, 50, 100]:
        o1 = 1
        olog = int(n.bit_length())  # приблизительно log₂(n)
        on = n
        onlog = n * olog
        on2 = n * n
        o2n = 2 ** n
        
        print(f"{n:>4} {o1:>6} {olog:>8} {on:>6} {onlog:>10} {on2:>6} {o2n:>8}")
    print('\n')

if __name__ == "__main__":
    print_growth_table()
    demonstrate_big_o()
