class Book:
    def __init__(self,id:int,name:str,pages:int):
        self.id=id
        self.name=name
        self.pages=pages
    def __str__(self)->str:
        return f'Книга"{self.name}"'

    def __repr__(self)->str:
        return f'Book(name={self.name!r},id={self.id!r},pages={self.pages!r})'



class Library:
    def __init__(self,books:list):
        self.books=books

    def get_next_book_id(self)->int:
        if len(self.books)==0:
            return 1
        else:
            return self.books.index(self.books[-1])+1

    def get_index_by_book_id(self,name:str):
        self.name=name
        if name in self.books:
            return self.books.index(name)
        else:
            raise ValueError('Книги с запрашиваемым id не существует')
