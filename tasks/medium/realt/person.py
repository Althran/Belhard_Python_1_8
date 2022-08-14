class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cash = 0
        self.realty = []

    def info(self):
        return f'Имя: {self.name}, Возраст: {self.age}, Список домов: {self.realty}, Количество денег: {self.cash}'

    def earn_money(self, value):
        self.cash += value

    def make_deal(self, obj):
        if self.cash >= obj.cost:
            self.cash -= obj.cost
            self.realty.append(obj)
