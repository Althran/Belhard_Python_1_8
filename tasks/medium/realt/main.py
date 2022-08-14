from house import House
from townhouse import Townhouse
from person import Person


if __name__ == '__main__':
    house1 = House('Pushkina', 10, 25)
    house2 = House('Yarcivo', 10, 5)
    townhouse1 = Townhouse('Push', 15, 50)
    townhouse2 = Townhouse('Yar', 25, 15)
    person1 = Person('Albert', 26)
    person1.earn_money(5)
    person1.make_deal(house2)
    person1.earn_money(50)
    print(person1.info())
