""""
Class SocialNet представляет собой общий класс социальных сетей
Дочерние классы наследуют базовые инструкции для пользователя

"""
class SocialNet:
    def defender(self,arg):
      self.arg=arg
      if type(arg) is not str:
        raise TypeError
    def __init__(self,login,password):
      """

      :param login: Инкапсуляция выполнена с целью скрыть логин
      :param password: Инкапсуляция выполнена с целью скрыть пароль
      """
      self._login=login
      login:str
      self._password=password
      password:str
      if type(password) and type(login) is not str:
        raise TypeError

    def __str__(self):
      return f"Login:{self._login}\nPassword:{self._password}"

    def __repr__(self):
      return f"{self.__class__.__name__}:{self._login}"

    def registration(self,users:dict):
      """
      Метод регистрирует пользователя
      на вход он получает словарь в который добавляет данные
      пользователя
      :param users: Словарь с ключами Login:Password
      :return:
      """
      self.users=users
      users={
        f'{self._login}':self._password
      }
      return users

    def publication(self,text:str):
      """
      Метод публикации новости
      :param text: Текст который необходимо опубликовать
      :return:
      """
      self.text=text

      if type(text) is not str:
        raise TypeError
      return f'User {self._login} is publicated new post:{text}'

#Класс Телеграм социальная сеть которая наследует и перегружает методы
#из основного класса
class Telegram(SocialNet):
  def __init__(self,login,password,telephone:int):
    super().__init__(login,password)
    self.telephone=telephone
    if type(telephone) is not int:
      raise TypeError
  def __str__(self):
    return f'The phone number:{self.telephone}'

  def __repr__(self):
    return f"{self.__class__.__name__}:{self.telephone}"

  def add_phone(self):
    """
    Метод помимо данных логин и пароль добавляет телефона пользователя
    унаследование выполнено для расширения функционала родного метода класса
    :return:
    """
    user=super().registration({})
    user[f'Telephone']=self.telephone
    return user
  def publication(self,text:str,topik:str):
    """
    Метод перегружен в связи с добавлением новых атрибутов
    :param text: Тест публикации
    :param topik: Заголовок публикации
    :return:
    """
    self.text=text
    self.topik=topik
    return f'Пользователь {self._login} опубликовал ' \
           f'новость связанную с {topik}' \
           f' содержание новости:{text}'


tg=Telegram('Kolya','12345',89145757)
print(tg.publication('Видеокарты подорожали','Компьютеры'))