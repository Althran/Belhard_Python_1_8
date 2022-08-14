class House:

    def __init__(self, address, area, cost):
        self.address = address
        self.area = area
        self.cost = cost

    def increase_cost(self, value):
        self.cost += value

    def decrease_cost(self, value):
        self.cost -= value

    def __repr__(self):
        return f'Адрес: {self.address}, Площадь: {self.area} кв.м, Цена: {self.cost} тугриков'
