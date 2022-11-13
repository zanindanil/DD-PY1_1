main_str = """
    Данное предложение будет разбиваться на отдельные слова.
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов.
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """
def get_count_char(str_):
    p=0
    letters = {}
    str_ = "".join(str_.split())
    str_ = str_.lower()

    for dict_ in str_:
        if dict_.isalpha():
            for j in str_:

                if j==dict_:
                    p += 1
                    letters[dict_]=p

            p=0

    return letters
print(get_count_char(main_str))

