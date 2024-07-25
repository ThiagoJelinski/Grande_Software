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

class GuitarSpec:
    def __init__(self, builder, model, typeG, back_wood, top_wood):
        self.__builder = builder
        self.__model = model
        self.__typeG = typeG
        self.__back_wood = back_wood
        self.__top_wood = top_wood

    def get_builder(self):
        return self.__builder.name

    def get_model(self):
        return self.__model

    def get_typeG(self):
        return self.__typeG.name

    def get_back_wood(self):
        return self.__back_wood.name

    def get_top_wood(self):
        return self.__top_wood.name

    def matches(self, other_spec):
        return (not other_spec.get_builder() or self.get_builder() == other_spec.get_builder()) and \
               (not other_spec.get_model() or self.get_model() == other_spec.get_model()) and \
               (not other_spec.get_typeG() or self.get_typeG() == other_spec.get_typeG()) and \
               (not other_spec.get_back_wood() or self.get_back_wood() == other_spec.get_back_wood()) and \
               (not other_spec.get_top_wood() or self.get_top_wood() == other_spec.get_top_wood())

class Guitar:
    def __init__(self, serial_number, price, spec):
        self.__serial_number = serial_number
        self.__price = price
        self.__spec = spec

    def get_serial_number(self):
        return self.__serial_number

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

    def get_spec(self):
        return self.__spec

    def __str__(self):
        spec = self.get_spec()
        return f"{spec.get_builder()} {spec.get_model()} {spec.get_typeG()} ({self.get_serial_number()})"

class Inventory:
    def __init__(self):
        self.__guitars = []

    def add_guitar(self, serial_number, price, builder, model, typeG, back_wood, top_wood):
        spec = GuitarSpec(builder, model, typeG, back_wood, top_wood)
        guitar = Guitar(serial_number, price, spec)
        self.__guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in self.__guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar
        return None

    def search_guitar(self, search_spec):
        for guitar in self.__guitars:
            if guitar.get_spec().matches(search_spec):
                return guitar
        return None

if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_guitar("V95693", 1499.95, Builder.FENDER, "Stratocaster", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER)
    inventory.add_guitar("V95694", 1699.95, Builder.FENDER, "Telecaster", TypeG.ELECTRIC, Wood.MAHOGANY, Wood.MAPLE)
    inventory.add_guitar("11277", 3999.95, Builder.MARTIN, "Collings", TypeG.ACOUSTIC, Wood.ROSEWOOD, Wood.ROSEWOOD)

    what_erin_likes = GuitarSpec(Builder.MARTIN, "Collings", TypeG.ACOUSTIC, Wood.ROSEWOOD, Wood.ROSEWOOD)
    guitar = inventory.search_guitar(what_erin_likes)

    if guitar:
        print(f"Erin, you might like this {guitar} guitar:\n"
              f"{guitar.get_spec().get_back_wood()} back and sides,\n{guitar.get_spec().get_top_wood()} top.\n"
              f"You can have it for only ${guitar.get_price()}!")
    else:
        print("Sorry, Erin, we have nothing for you.")
