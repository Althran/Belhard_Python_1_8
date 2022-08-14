"""
Предположим, нас утомило задание атрибутов в конструкторе init(self, *args,
**kwargs). Хотелось бы ускорить этот процесс таким образом, чтобы была
возможность задавать атрибуты прямо при создании объекта класса.

class Man:
    pass

me = Man(height = 180, weight = 80)
TypeError: Man() takes no arguments

Сделать возможным данный механизм с помощью метакласса DynamicInitMeta
"""


class DynamicInitMeta(type):
    def __new__(mcs, name, base, attr):
        return super().__new__(mcs, name, base, attr)

    def __call__(self, *args, **kwargs):
        new_obj = super().__call__(*args)
        for i in kwargs:
            setattr(new_obj, i, kwargs[i])
        return new_obj
