def merge_sort(mas, lower, upper):
    if len(mas) <= 1:
        return mas
    if lower >= upper:
        return
    mid = (lower + upper) // 2
    merge_sort(mas, lower, mid)
    merge_sort(mas, mid + 1, upper)

    merged = merge(mas, lower, mid, mid + 1, upper)

    for i, val in enumerate(merged):
        mas[lower + i] = val
    return mas


def merge(mas, l_lower, l_upper, r_lower, r_upper):
    i, j = l_lower, r_lower
    temp = []
    while i <= l_upper and j <= r_upper:
        if mas[i] <= mas[j]:
            temp.append(mas[i])
            i += 1
        else:
            temp.append(mas[j])
            j += 1
    while i <= l_upper:
        temp.append(mas[i])
        i += 1
    while j <= r_upper:
        temp.append(mas[j])
        j += 1
    return temp