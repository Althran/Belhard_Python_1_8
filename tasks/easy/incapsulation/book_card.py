"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""
from datetime import date

CURRENT_YEAR = date.today().year


class BookCard:
    __author: str
    __title: str
    __year: int

    def __init__(self, __author, __title, __year):
        self.__author = __author
        self.__title = __title
        self.__year = __year

    def __eq__(self, other):
        return self.__year == other

    def __ne__(self, other):
        return self.__year != other

    def __lt__(self, other):
        return self.year < other

    def __gt__(self, other):
        return self.year > other

    def __le__(self, other):
        return self.year <= other

    def __ge__(self, other):
        return self.year >= other

    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise ValueError

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError

    @year.setter
    def year(self, value):
        if not isinstance(value, int) and value > 0:
            raise ValueError
