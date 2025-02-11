class CityNavigation:
    def __init__(self):
        self.cityMap = {}

    def add_location(self, location):
        if location not in self.cityMap:
            self.cityMap[location] = []
        else:
            print("Location '{location}' already exists.")

    def add_road(self, l1, l2, distance):
        if l1 in self.cityMap and l2 in self.cityMap:
            self.cityMap[l1].append((l2, distance))
            self.cityMap[l2].append((l1, distance))
        else:
            print("Both locations must exist before adding a road.")

    def display_city_map(self):
        print("City Map:")
        for location in self.cityMap:
            print(f"{location}: {self.cityMap[location]}")

# Example Usage:
city = CityNavigation()
city.add_location("Nawabshah")
city.add_location("Karachi")
city.add_location("Islamabad")
city.add_location("Haripur")
city.add_location("Sakurdu")
city.add_road("Nawabshah", "Karachi", 5)
city.add_road("Karachi", "Islamabad", 10)
city.add_road("Haripur", "Nawabshah", 15)
city.add_road("Islamabad", "Sakurdu", 25)
city.display_city_map()
