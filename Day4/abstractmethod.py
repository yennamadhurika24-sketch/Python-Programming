'''Create an abstract class Shape that defines:
 
An abstract method area() (no implementation).

Create two child classes that inherit from Shape:
Rectangle → has attributes length, breadth, and implements area().
Circle → has attribute radius, and implements area().

Task:
Define the abstract class Shape using the abc module.
Implement Rectangle and Circle classes by providing their own version of area().
Create one object of Rectangle and one of Circle, then display their areas.
 
from abc import ABC, abstractmethod
 
# Abstract class
class Shape(ABC):
 
    @abstractmethod           # Abstract method
    def area(self):
        pass'''

from abc import ABC,abstractmethod
import math
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        A=self.l*self.b
        print("Area of reactangle=",round(A,2))
class circle(shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        A=math.pi*self.r*self.r
        print('Area of circle=',round(A,2))
r1=rectangle(2,4)
r1.area()
c1=circle(2)
c1.area()
    