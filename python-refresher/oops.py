# classes and objects
import datetime
from typing import List


class Student:
    name = ""
    roll_number = None
    class_name = ""

    def get_name(self):
        return self.name


# initialize the object

stu1 = Student()
stu1.name = "John Doe"
# stu1.roll_number = "123"
stu1.class_name = "Student Class"


# Constructor
class Teacher:
    def __init__(self, name, assigned_classes):
        self.name = name
        self.assigned_classes = assigned_classes

    def get_name(self):
        return self.name

    def get_assigned_classes(self):
        return self.assigned_classes


teacher1 = Teacher("Alex", ["1st", "2nd", "3rd"])


class BaseEntity:
    def __init__(self, id):
        self.id = id
        created_at: datetime.datetime
        updated_at: datetime.datetime


class Player(BaseEntity):
    def __init__(self, player_id):
        super().__init__(player_id)

    def get_id(self):
        return self.id


player1 = Player(10)
print(player1.get_id())


import math
from abc import ABC, abstractmethod


# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape."""
        pass


# Concrete subclass
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


# Another concrete subclass
class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side**2

    def perimeter(self) -> float:
        return 4 * self.side


# Usage example
if __name__ == "__main__":
    shapes = [Circle(5), Square(4)]
    for shape in shapes:
        print(
            f"{type(shape).__name__}: area = {shape.area():.2f}, "
            f"perimeter = {shape.perimeter():.2f}"
        )
