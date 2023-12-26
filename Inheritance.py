class Animal:
    def make_sound(self, s):
        print(s)
class horse(Animal):
    pass

class Car:
    def __init__(self,  model, color, year):
        self.model = model
        self.color = color
        self.year = year
class Supercar(Car):
    def __init__(self, model, color, year, sponsor):
        super().__init__(model, color, year)
        self.sponsor = sponsor

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width*self.height

rectangle = Rectangle(4, 5)
print(rectangle.area)
rectangle.width = 6
print(rectangle.area)

class Worker:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
class HR_worker:
    def __init__(self, name, position):
        super().__init__(name,position)
    def view_position(self, worker_name):
        return view_name.postion
jordan = Worker('Jordan', 'Middle')
pavel = HR ('Pavel', 'HR')
print(pavel.view_position(jordan))
    
    
    
    
    
    
    
    
    
