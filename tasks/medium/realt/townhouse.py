from house import House


class Townhouse(House):

    def __init__(self, address, area, cost):
        super().__init__(address, area, cost)
        self.area = 60

    def __repr__(self):
        return f'Адрес: {self.address}, Площадь: {self.area} кв.м, Цена: {self.cost} тугриков'
