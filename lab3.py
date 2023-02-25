
#ОСНОВНОЙ КЛАСС Book,имеет 2 аргумента (name,author).
class Book:

  def __init__(self,name:str,author:str):
    self._name=name  #инкасуляпция (недопустимость менять значение атрибута вне класса)
    self._author=author


  def __str__(self):
    return f"Name:{self._name}\nAuthor:{self._author}"

#дочерний класс  PaperBook,наследует 2 из основного класса 2 атрибута (name,author)
#  и имеет собственный атрибут (pages)-->int
class PaperBook(Book):
  def __init__(self,name:str,author:str,pages:int):
      super().__init__(name,author)


      self.pages=pages
      if type(pages) is not int :
         raise TypeError
      elif pages<=0:
        raise 'Неверный ввод pages, введите число >0'
  def __str__(self):
    return f'{self._name} \n{self.pages}'


#дочерний класс  AudioBook,наследует 2 из основного класса 2 атрибута (name,author)
#  и имеет собственный атрибут (duration)-->float

class AudioBook(Book):

  def __init__(self,name:str,author:str,duration:float):
      super().__init__(name,author)
      self.duration:float=duration

      if type(duration) is not float:
        raise TypeError

  def __str__(self):

    return f'{self.name}\n{self.duration}'


abook=PaperBook('Name','Author',23)
print(abook)