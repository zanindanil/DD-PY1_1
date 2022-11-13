import random as r


def get_unique_list_numbers():
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    s = []
    k = 0
    t=0
    while True:
        p = int(r.uniform(-10, 10))
        s.append(p)

        if len(s) >= 15:
            break

    while not len(s) == len(set(s)):
        p = int(r.uniform(-10, 10))
        s[k] = p
        k += 1
        if k >= 15:
            k = 0
        t+=1
    print(t)
    return s


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
