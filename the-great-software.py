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
    def __init__(self, builder, model, typeG, back_wood, top_wood, num_strings=6):
        self.builder = builder
        self.model = model
        self.typeG = typeG
        self.back_wood = back_wood
        self.top_wood = top_wood
        self.num_strings = num_strings

    def matches(self, other_spec):
        if self.builder != other_spec.builder and other_spec.builder:
            return False
        if self.model != other_spec.model and other_spec.model:
            return False
        if self.typeG != other_spec.typeG and other_spec.typeG:
            return False
        if self.back_wood != other_spec.back_wood and other_spec.back_wood:
            return False
        if self.top_wood != other_spec.top_wood and other_spec.top_wood:
            return False
        if self.num_strings != other_spec.num_strings and other_spec.num_strings:
            return False
        return True

class Guitar:
    def __init__(self, serial_number, price, spec):
        self.serial_number = serial_number
        self.price = price
        self.spec = spec

    def __str__(self):
        spec = self.spec
        return (f"{spec.builder.name} {spec.model} {spec.typeG.name.lower()} guitar "
                f"({self.serial_number})")

class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, serial_number, price, builder, model, typeG, back_wood, top_wood, num_strings=6):
        spec = GuitarSpec(builder, model, typeG, back_wood, top_wood, num_strings)
        guitar = Guitar(serial_number, price, spec)
        self.guitars.append(guitar)

    def search_guitar(self, search_spec):
        matching_guitars = []
        for guitar in self.guitars:
            if guitar.spec.matches(search_spec):
                matching_guitars.append(guitar)
        return matching_guitars

if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_guitar("V95693", 1499.95, Builder.FENDER, "Stratocaster", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    inventory.add_guitar("V99999", 1599.95, Builder.FENDER, "Stratocaster", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    inventory.add_guitar("V9857", 2000.99, Builder.TAYLOR, "Stratocaster", TypeG.ELECTRIC, Wood.MAPLE, Wood.MAPLE, 12)

    erin_likes = GuitarSpec(Builder.FENDER, "Stratocaster", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    matching_guitars = inventory.search_guitar(erin_likes)

    if matching_guitars:
        print("Erin, you might like these:")
        for guitar in matching_guitars:
            spec = guitar.spec
            print(f"\nGuitar: {guitar.serial_number} {spec.builder.name.lower()} {spec.model.lower()} {spec.typeG.name.lower()} guitar:")
            print(f"{spec.back_wood.name.lower()} back and sides,")
            print(f"{spec.top_wood.name.lower()} top, with {spec.num_strings} strings")
            print(f"It can be yours for only ${guitar.price}!")
    else:
        print("Sorry, Erin, we have nothing for you.")
