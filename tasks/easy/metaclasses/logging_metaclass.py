"""
Написать логгирующий декоратор log_decorator, который будет логгировать
вызов функции. До выполнения функции необходимо вывести в консоль строку
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}". А после вывести
строку "Выполнено {func.__name__}".

Написать логгирующий метакласс LogMeta, который ко всем методам класса добавляет
функционал декоратора log_decorator.
"""
from types import FunctionType


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Выполнено {func.__name__}")
        return result
    return wrapper


class LogMeta(type):
    def __new__(mcs, name, bases, attr):
        new_attr = {}
        for attr_name, attr_value in attr.items():
            if isinstance(attr_value, FunctionType):
                attr_value = log_decorator(attr_value)
            new_attr[attr_name] = attr_value
        new_cls = super().__new__(mcs, name, bases, attr)
        return new_cls
