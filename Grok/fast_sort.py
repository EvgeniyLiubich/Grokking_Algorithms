def summa(lst):
    """Сумма элементов в списке"""
    if not lst:
        return 0
    return lst[0] + summa(lst[1:])


lst = [10, 5, 2, 3]
print(summa(lst))


def count(lst):
    """Подсчет колличества элементов"""
    if not lst:
        return 0
    return 1 + count(lst[1:])


print(count(lst))


def max_item(lst):
    """Наибольший элемент в списке"""
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    sub_max = max_item(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max


print(max_item(lst))


def fast_sort(lst):
    """Быстрая сортировка"""
    if len(lst) < 2:
        return lst
    sup_item = lst[0]
    less = [i for i in lst[1:] if i <= sup_item]
    greater = [i for i in lst[1:] if i > sup_item]
    return fast_sort(less) + [sup_item] + fast_sort(greater)


print(fast_sort(lst))
