class TomatoBush:

    def __init__(self, *args):
        self.tomato_list = [*args]

    def grow_all(self):
        for i in self.tomato_list:
            i.grow()

    def all_are_ripe(self):
        return all([i.is_ripe() for i in self.tomato_list])

    def give_away_all(self):
        for i in self.tomato_list:
            if i == 'Красный':
                self.tomato_list.pop(i)
            return self.tomato_list
