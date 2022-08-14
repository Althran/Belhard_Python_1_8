from tomato import Tomato
from tomato_bush import TomatoBush
from gardener import Gardener

if __name__ == '__main__':
    tomato_bush1 = TomatoBush(Tomato(0), Tomato(0))
    tomato_bush2 = TomatoBush(Tomato(0), Tomato(0))
    gardener_name = Gardener('Al', tomato_bush1, tomato_bush2)
    gardener_name.work()
    gardener_name.work()

    result = gardener_name.harvest()
    if result is None:
        print('Томаты не созрели')
    else:
        print(result)
