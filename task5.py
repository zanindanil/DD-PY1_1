import random as r
import string


def get_random_password():
    ...  # TODO написать функцию генерации случайных паролей

    list1 = list(string.ascii_letters)
    list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    mainlist = list1 + list2
    password = 'Your password is : '
    for i in range(0, 8):
        j = int(r.uniform(0, len(mainlist)))
        password = password + str(mainlist[j])

    return print(password)


get_random_password()
