def quick_sort(mas):
    if len(mas) <= 1:
        return mas
    else:
        mid = mas[len(mas)//2]
        s_part = []
        b_part = []
        m_part = []
        for n in mas:
            if n < mid:
                s_part.append(n)
            elif n > mid:
                b_part.append(n)
            else:
                m_part.append(n)
        return quick_sort(s_part) + m_part + quick_sort(b_part)
