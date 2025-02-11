class AquaFlow:
    def __init__(self, calculation):
        self.area = 0
        self.volume = 0
        self.length = calculation[0]
        self.width = calculation[1]
        self.depth = calculation[2]


    def Calculate_Area(self):
        self.area = self.length * self.width

    def Calculate_Volume(self):
        self.volume = self.area * self.depth

    def display(self):
        print("Field Area:", self.area, "square")
        print("Water Volume Required:", self.volume, "cubic")


calculation = (10, 5, 2)

field = AquaFlow(calculation)
field.Calculate_Area()
field.Calculate_Volume()
field.display()

print("Irrigation Start...")
