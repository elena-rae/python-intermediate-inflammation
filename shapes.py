import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2*math.pi*self.radius

    def __repr__(self): 
        return f"Circle(radius={self.radius})"


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def circumference(self):
        return 2*self.a + 2*self.b 

    def __repr__(self):
        return f"Rectangle(a={self.a}, b={self.b})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __repr__(self):
        return f"Square(side={self.a})"



if __name__ == "__main__":  # the following code snippit is only excuted when called from commandline (than the users(?) name is set to __main__)
    my_circle = Circle(10)
    my_square = Square(5)
    my_rectangle = Rectangle(3,5)

    for shape in [my_circle, my_square, my_rectangle]:

        print(type(shape))
        print(shape)
        #print(my_circle.radius)
        print(f"shape has circumference {shape.circumference()}\n")

        