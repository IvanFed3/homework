list_1 = [1, 10, 9, 4, 5, 7, 2, 0]


def list_sort(n: int, m: int) -> list:
    """Функція, яка приймає  індекс початку сортування (n)  та індекс кінця сортування (m) та список із змінної list_1,
і повертає список у якому відсортовані лише ті елементи,  які укладені між індексом початку сортування(n) та індексом
кінця сортування (m). Сортується від мешого індекса до більшого, інакше виводиться вхідний список"""

    global list_1
    list_1 = (list_1[:n] + sorted(list_1[n:m]) + list_1[m:]) if n < m else (list_1[:m] + sorted(list_1[m:n]) + list_1[n:]) if n > m else list_1
    return list_1


print(list_sort(2, 6))
