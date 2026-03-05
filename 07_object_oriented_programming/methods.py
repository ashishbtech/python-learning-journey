class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

circle1 = Circle(5)
print("Area:", circle1.area())
print("Circumference:", circle1.circumference())