lst = list(range(100))
# print(len(lst))


def binary_search(lst, item):
    """Если искомое значение присутствует во входящем массиве, то функция выведет номер позиции нашего значения"""
    """Входящий массив должен быть отсортирован"""
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_lst = [1, 3, 5, 7, 9]

print(binary_search(lst, 33))
