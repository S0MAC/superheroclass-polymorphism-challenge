# Parent class: Superhero
class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def introduce(self):
        return f"I am {self.name} from {self.universe}, and my power is {self.power}!"

# Child class: Villain (inherits from Superhero)
class Villain(Superhero):
    def __init__(self, name, power, universe, evil_plan):
        super().__init__(name, power, universe)  # Inherit attributes from Superhero
        self.__evil_plan = evil_plan  # Private attribute (Encapsulation)

    def reveal_plan(self):
        return f"My evil plan is: {self.__evil_plan} 😈"

# Creating objects
hero = Superhero("Spider-Man", "Web-slinging", "Marvel")
villain = Villain("Green Goblin", "Super Intelligence", "Marvel", "Destroy Spider-Man")

# Testing methods
print(hero.introduce())  # Output: I am Spider-Man from Marvel, and my power is Web-slinging!
print(villain.introduce())  # Output: I am Green Goblin from Marvel, and my power is Super Intelligence!
print(villain.reveal_plan())  # Output: My evil plan is: Destroy Spider-Man 😈
