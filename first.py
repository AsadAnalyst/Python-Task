class AquaFlow:
    def __init__(self, dimensions):
        self.length = dimensions[0]
        self.width = dimensions[1]
        self.depth = dimensions[2]
        self.area = 0
        self.volume = 0

    def Calculate_area(self):
        self.area = self.length * self.width

    def Calculate_volume(self):
        self.volume = self.area * self.depth

    def display(self):
        print("Field Area:", self.area, "square units")
        print("Water Volume Required:", self.volume, "cubic units")


dimensions = (10, 5, 2)

field = AquaFlow(dimensions)
field.Calculate_area()
field.Calculate_volume()
field.display()

print("Irrigation Starts…")
