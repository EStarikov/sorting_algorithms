def bubble_sort(mas):
    n = len(mas)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if mas[j] > mas[j + 1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]
                swapped = True
        if not swapped:
            break
    return mas.copy()