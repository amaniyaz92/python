class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")
class Cat(Animal):
    def make_sound(self):
        print("Meow!")
class Cow(Animal):
    def make_sound(self):
        print("Moo!")
name = Dog
name = Cat
name = Cow

while True:
    action = input('Введите название животного ')
    if action.lower()=='собака':
        Dog.make_sound(Dog)
    elif action.lower()=='кошка':
        Cat.make_sound(Cat)
    elif action.lower()=='корова':
        Cow.make_sound(Cow)
    else:
        print('Неизвестная операция!')

