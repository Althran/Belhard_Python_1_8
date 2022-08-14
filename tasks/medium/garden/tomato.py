class Tomato:

    def __init__(self, index):
        self.index = index
        self.states = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')
        self.ripeness = self.states[index]

    def grow(self):
        self.index += 1
        self.ripeness = self.states[self.index]

    def is_ripe(self):
        if self.ripeness == 'Красный':
            return True
        else:
            return False

    def __repr__(self):
        return f'Томат: {self.ripeness}'
