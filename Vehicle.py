class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def display_info(self, b, y):
        print(self.brand, self.year)

class Car(Vehicle):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        self.color = color
    def display_info(self, b, y, c):
        print(self.brand, self.year, self.color)
class Motorcycle(Vehicle):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        self.color = color
    def display_info(self, b, y, c):
        print(self.brand, self.year, self.color)

brand1 = input('Введите бренд: ')
year1 = input('Введите год выпуска: ')
color1 = input('Введите цвет: ')
Vehicle1 = Vehicle(brand = brand1, year = year1)
Car1 = Car(brand = brand1, year = year1, color = color1)
Motorcycle1 = Motorcycle(brand = brand1, year = year1, color = color1)

while True:
    action = input('Введите название транспорта ')
    if action.lower() == 'транспорт':
        Vehicle1.display_info(brand1, year1)
    elif action.lower() == 'машина':
        Car1.display_info(brand1, year1, color1)
    elif action.lower() == 'мотоцикл':
        Motorcycle1.display_info(brand1, year1, color1)
    else:
        print('Неизвестная операция!')
