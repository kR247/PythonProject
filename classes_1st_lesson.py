class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors:
            a = list(range(1, int(new_floor + 1)))
            for i in a:
                print(i)
        else:
            print('Такого этажа не сущестувует')

h1 = House('Эльдорадо', 25)
h2 = House('Эдем', 30)
h1.go_to(15)
h2.go_to(32)