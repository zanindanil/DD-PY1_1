class School:

    def __init__(self,students:int,classes:int):
        '''students-количество учеников в школе
            classes-количество классов в школе'''
        if not isinstance(students,(int)):
            raise TypeError("Количество учеников должно быть строго целым числом")
        if students<=0:
            raise ValueError("Количество учеников должно быть больше нуля")
        self.students=students

        if not isinstance(classes,(int)):
            raise TypeError("Количество классов должно быть строго целым числом")
        if classes<=0:
            raise ValueError("Должен присутствовать как минимум один класс с учениками")

    def add_students(self,potential_student:str)->str:
        """potential student- потенциально возможный школьник, которого добавят в школу
           метод добавляет конкретного потенциального ученика в школу """
        ...
    def to_get_mark(self,mark:int)->None:
        """mark-оценка за ответы на уроке
            метод выставления оценки ученику"""
        ...
        if mark<2:
            raise ValueError("Минимально возможная оценка 2")



class Library:

    def __init__(self,books:int,employees:str):
        """

        :param books: Количество книг в библиотеке
        :param employees: Персонал библиотеки
        """

        if not isinstance(books, (int)):
            raise TypeError("Количество книг должно быть целым числом")
        if books < 0:
            raise ValueError("Количество книг должно быть больше либо равно нулю")
        self.books=books

        self.employees=employees

    def to_get_books(self,new_books:int)->None:
        """

        :param new_books: Количество поступивших книг
        :return: Метод добалвения новых книг в библиотеку
        """
        if not isinstance(new_books, (int)):
            raise TypeError("Количество новых книг должно быть типа int")
        if new_books<=0:
            raise ValueError("Количество поступивших книг должно быть строго больше нуля")
        ...
    def remove_old_books(self,old_books:int)->None:
        """

        :param old_books: Количество старых книг
        :return: Метод удаляет старые книги из библиотеки
        """
        if not isinstance(old_books, (int)):
            raise TypeError("Количество старых книг должно быть типа int")
        if old_books<0:
            raise ValueError("Количество старых книг длжно быть больше либо равно нулю")




class Prison:
    def __init__(self,prisoners:int,security:str):
        """
        :param prisoners: Количество заключенных
        :param security:  Список личного состава охраны тюрьмы
        """
        if not isinstance(prisoners,(int)):
            raise TypeError("Количество заключенных должно быть типа int")
        if prisoners<0:
            raise ValueError("Количество заключенных должно быть больше или равно нулю")
        self.prisoners=prisoners

        if not isinstance(security,str):
            raise TypeError("Список личного состава охраны должен быть типа STR")
        self.security=security

    def death_penalty(self,name_prisoners:str)->str:
        """

        :param name_prisoners: Имя и Фамилия заключенного
        :return: Метод смертной казни , при срабатывании метода , в тюрьме казнят конкретного заключенного

        """

        ...
    def freedom_prisoner(self,namep_prisoner:str)->str:
        """

        :param namep_prisoner:  Имя и Фамилия заключенного
        :return: Метод выпускает заключенного из тюрьмы
        """
        ...