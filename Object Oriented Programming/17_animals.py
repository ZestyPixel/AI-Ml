class Herbivore:
    def __init__(self):
        self.food_type = "Plants"

    def eat_plants(self):
        return "Eating plants"

class Carnivore:
    def __init__(self):
        self.food_type = "Meat"

    def eat_meat(self):
        return "Eating meat"

class Omnivore(Herbivore, Carnivore):
    def __init__(self):
        Herbivore.__init__(self)
        Carnivore.__init__(self)

    def eat_both(self):
        return "Eating plants and meat"

class Bear(Omnivore):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def info(self):
        return f"{self.name} is an omnivore"

b = Bear("Bear")
print(b.eat_plants())
print(b.eat_meat())
print(b.eat_both())
print(b.info())