class Gardener:

    def __init__(self, name, *args):
        self.name = name
        self.plants = [*args]

    def work(self):
        for i in self.plants:
            i.grow_all()

    def harvest(self):
        if all([i.all_are_ripe() for i in self.plants]):
            result = []
            for i in self.plants:
                result += i.give_away_all()
            return result
        else:
            return None
