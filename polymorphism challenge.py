# Parent class: Vehicle
class Vehicle:
    def move(self):
        pass  # Placeholder, overridden in child classes

# Child class: Car
class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"

# Child class: Plane
class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"

# Child class: Boat
class Boat(Vehicle):
    def move(self):
        return "🚢 Sailing on water"

# Testing polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())

# Output:
# 🚗 Driving on the road
# ✈️ Flying in the sky
# 🚢 Sailing on water
