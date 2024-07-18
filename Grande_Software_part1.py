from enum import Enum, auto

class Builder(Enum):
    FENDER = auto()
    MARTIN = auto()
    GIBSON = auto()
    TAYLOR = auto()
    PRS = auto()

class TypeG(Enum):
    ACOUSTIC = auto()
    ELECTRIC = auto()

class Wood(Enum):
    ALDER = auto()
    MAHOGANY = auto()
    MAPLE = auto()
    ROSEWOOD = auto()
    CEDAR = auto()

class Guitar:
    def __init__(self, serial_number, price, builder, model, typeG, back_wood, top_wood):
        self.serial_number = serial_number
        self.price = price
        self.builder = builder
        self.model = model
        self.typeG = typeG
        self.back_wood = back_wood
        self.top_wood = top_wood

    def get_serial_number(self):
        return self.serial_number

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def get_builder(self):
        return self.builder.name

    def get_model(self):
        return self.model

    def get_typeG(self):
        return self.typeG.name

    def get_back_wood(self):
        return self.back_wood.name

    def get_top_wood(self):
        return self.top_wood.name

    def __str__(self):
        return f"{self.get_builder()} {self.get_model()} {self.get_typeG()} ({self.get_serial_number()})"

class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, serial_number, price, builder, model, typeG, back_wood, top_wood):
        guitar = Guitar(serial_number, price, builder, model, typeG, back_wood, top_wood)
        self.guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in self.guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar
        return None

    def search_guitar(self, search_guitar):
        for guitar in self.guitars:
            if self.__matches_criteria(guitar, search_guitar):
                return guitar
        return None

    def __matches_criteria(self, guitar, search_guitar):
        return (not search_guitar.get_builder() or guitar.get_builder() == search_guitar.get_builder()) and \
               (not search_guitar.get_model() or guitar.get_model() == search_guitar.get_model()) and \
               (not search_guitar.get_typeG() or guitar.get_typeG() == search_guitar.get_typeG()) and \
               (not search_guitar.get_back_wood() or guitar.get_back_wood() == search_guitar.get_back_wood()) and \
               (not search_guitar.get_top_wood() or guitar.get_top_wood() == search_guitar.get_top_wood())


if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_guitar("V95693", 1499.95, Builder.FENDER, "Stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER)
    inventory.add_guitar("V95694", 1699.95, Builder.FENDER, "Telecaster", TypeG.ELECTRIC, Wood.MAHOGANY, Wood.MAPLE)
    inventory.add_guitar("11277", 3999.95, Builder.MARTIN, "Collings", TypeG.ACOUSTIC, Wood.ROSEWOOD, Wood.ROSEWOOD)

    what_erin_likes = Guitar("", 0, Builder.MARTIN, "Collings", TypeG.ACOUSTIC, Wood.ROSEWOOD, Wood.ROSEWOOD)
    guitar = inventory.search_guitar(what_erin_likes)

    if guitar:
        print(f"Erin, you might like this {guitar} guitar:\n"
              f"{guitar.get_back_wood()} back and sides,\n{guitar.get_top_wood()} top.\n"
              f"You can have it for only ${guitar.get_price()}!")
    else:
        print("Sorry, Erin, we have nothing for you.")
