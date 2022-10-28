import math

pi = 3.141592653589793


def remainder(a: int, b: int):
    return a % b


def subtract(a: int, b: int, c: int = 0, d: int = 0):
    """
    Subtract :: Function\n
    \tto subtract 2 numbers use: subtract(number, number)\n
    \tto subtract 3 numbers use: subtract(number, number, number)\n
    \tto subtract 4 numbers use: subtract(number, number, number, number)\n
    :param a:
    :param b:
    :param c:
    :param d:
    :return: a-b-c-d
    """
    return int(a) - int(b) - int(c) - int(d)


def add(a: int or float, b: int or float, c: int or float = 0, d: int or float = 0):
    return a + b + c + d


def multiply(a: int or float, b: int or float, c: int or float = 1, d: int or float = 1):
    return a * b * c * d


def divide(a: int or float, b: int or float, c: int or float = 1, d: int or float = 1):
    return a / b / c / d


def findPerimeter_ofRectangle(RectangleLength: int or float, RectangleBreadth: int or float):
    per = 2 * (RectangleLength + RectangleBreadth)
    return per


def findArea_ofRectangle(RectangleLength: int or float, RectangleBreadth: int or float):
    area = RectangleLength * RectangleBreadth
    return area


def findPerimeter_ofSquare(SideLength: int or float):
    per = 4 * SideLength
    return per


def findArea_ofSquare(SideLength: int or float):
    return SideLength * SideLength


def findPerimeter_ofTriangle(a: int or float, b: int or float, c: int or float):
    per = a + b + c
    return per


def findArea_ofTriangle(base: int or float, height: int or float):
    area = 1 / 2 * base * height
    return area


def findPerimeter_ofParallelogram(base: int or float, height: int or float):
    per = 2 * (base + height)
    return per


def findArea_ofParallelogram(base: int or float, height: int or float):
    area = base * height
    return area


def findCircumference(radius: int or float):
    cir = 2 * 22 / 7 * radius
    return cir


def findArea_ofCircle(radius: int or float):
    area = 22 / 7 * radius * radius
    return area


def findLength_Rectangle(breadth: int or float, area: int or float):
    return area / breadth


def findBreadth_Rectangle(length: int or float, area: int or float):
    return area / length


def findSide_Square(perimeter: int or float):
    return perimeter / 4


def find_Square(number: int or float):
    return number * number


def find_Exponent(number: int or float, power: int or float):
    return pow(number, power)


def squareRoot(number: int or float):
    return math.sqrt(number)


class find:
    class area:
        @staticmethod
        def triangle(base: int or float, height: int or float):
            area = 1 / 2 * base * height
            return area

        @staticmethod
        def square(side: int or float):
            area = side * side
            return area

        @staticmethod
        def rectangle(length: int or float, breadth: int or float):
            area = length * breadth
            return area

        @staticmethod
        def parallelogram(base: int or float, height: int or float):
            area = base * height
            return area

        @staticmethod
        def rhombus():
            pass

    class perimeter:
        @staticmethod
        def triangle(a: int or float, b: int or float, c: int or float):
            return a + b + c

        @staticmethod
        def square(side: int or float):
            return side * 4

        @staticmethod
        def rectangle(length: int or float, breadth: int or float):
            value = 2 * (length + breadth)
            return value

        @staticmethod
        def parallelogram(base: int or float, height: int or float):
            value = 2 * (base + height)
            return value

        @staticmethod
        def rhombus():
            pass

    @staticmethod
    def exponent(number: int or float, power: int):
        return pow(number, power)

    @staticmethod
    def square(number):
        return number * number

    @staticmethod
    def squareRoot(number):
        return math.sqrt(number)
# -------------------------------------------------------------------------------#