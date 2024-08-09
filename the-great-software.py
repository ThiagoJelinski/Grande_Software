from abc import ABC, abstractmethod
from enum import Enum, auto

# Enums for instrument attributes
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

# Abstract base classes for Instruments and Specs
class Instrument(ABC):
    def __init__(self, serial_number, price, spec):
        self.serial_number = serial_number
        self.price = price
        self.spec = spec

    @abstractmethod
    def __str__(self):
        pass

class InstrumentSpec(ABC):
    def __init__(self, builder, model, typeG, back_wood, top_wood, num_strings=6):
        self.builder = builder
        self.model = model
        self.typeG = typeG
        self.back_wood = back_wood
        self.top_wood = top_wood
        self.num_strings = num_strings

    @abstractmethod
    def matches(self, other_spec):
        pass

# Concrete classes for Guitar and GuitarSpec
class GuitarSpec(InstrumentSpec):
    def matches(self, other_spec):
        return (
            isinstance(other_spec, GuitarSpec) and
            (self.builder == other_spec.builder or not other_spec.builder) and
            (self.model == other_spec.model or not other_spec.model) and
            (self.typeG == other_spec.typeG or not other_spec.typeG) and
            (self.back_wood == other_spec.back_wood or not other_spec.back_wood) and
            (self.top_wood == other_spec.top_wood or not other_spec.top_wood) and
            (self.num_strings == other_spec.num_strings or not other_spec.num_strings)
        )

class Guitar(Instrument):
    def __str__(self):
        return f"{self.spec.builder.name} {self.spec.model} {self.spec.typeG.name.lower()} guitar ({self.serial_number})"

# Concrete classes for Mandolin and MandolinSpec
class MandolinSpec(InstrumentSpec):
    def matches(self, other_spec):
        return (
            isinstance(other_spec, MandolinSpec) and
            (self.builder == other_spec.builder or not other_spec.builder) and
            (self.model == other_spec.model or not other_spec.model) and
            (self.typeG == other_spec.typeG or not other_spec.typeG) and
            (self.back_wood == other_spec.back_wood or not other_spec.back_wood) and
            (self.top_wood == other_spec.top_wood or not other_spec.top_wood) and
            (self.num_strings == other_spec.num_strings or not other_spec.num_strings)
        )

class Mandolin(Instrument):
    def __str__(self):
        return f"{self.spec.builder.name} {self.spec.model} {self.spec.typeG.name.lower()} mandolin ({self.serial_number})"

# Abstract Inventory class
class Inventory(ABC):
    def __init__(self):
        self.instruments = []

    @abstractmethod
    def add_instrument(self, serial_number, price, builder, model, typeG, back_wood, top_wood, num_strings=6):
        pass

    def search_instruments(self, search_spec):
        return [instrument for instrument in self.instruments if instrument.spec.matches(search_spec)]

# Concrete classes for Guitar and Mandolin inventories
class GuitarInventory(Inventory):
    def add_instrument(self, serial_number, price, builder, model, typeG, back_wood, top_wood, num_strings=6):
        spec = GuitarSpec(builder, model, typeG, back_wood, top_wood, num_strings)
        guitar = Guitar(serial_number, price, spec)
        self.instruments.append(guitar)

class MandolinInventory(Inventory):
    def add_instrument(self, serial_number, price, builder, model, typeG, back_wood, top_wood, num_strings=8):
        spec = MandolinSpec(builder, model, typeG, back_wood, top_wood, num_strings)
        mandolin = Mandolin(serial_number, price, spec)
        self.instruments.append(mandolin)

# Main program for testing
if __name__ == "__main__":
    guitar_inventory = GuitarInventory()
    guitar_inventory.add_instrument("V95693", 1499.95, Builder.FENDER, "Stratocaster", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER)
    guitar_inventory.add_instrument("V99999", 1599.95, Builder.FENDER, "Stratocaster", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER)
    guitar_inventory.add_instrument("V9857", 2000.99, Builder.TAYLOR, "Stratocaster", TypeG.ELECTRIC, Wood.MAPLE, Wood.MAPLE, 12)

    mandolin_inventory = MandolinInventory()
    mandolin_inventory.add_instrument("M12345", 1299.95, Builder.MARTIN, "Mandolin Model X", TypeG.ACOUSTIC, Wood.MAHOGANY, Wood.CEDAR)

    erin_guitar_pref = GuitarSpec(Builder.FENDER, "Stratocaster", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER)
    matching_guitars = guitar_inventory.search_instruments(erin_guitar_pref)

    erin_mandolin_pref = MandolinSpec(Builder.MARTIN, "Mandolin Model X", TypeG.ACOUSTIC, Wood.MAHOGANY, Wood.CEDAR)
    matching_mandolins = mandolin_inventory.search_instruments(erin_mandolin_pref)

    if matching_guitars:
        print("Erin, you might like these guitars:")
        for guitar in matching_guitars:
            print(f"\n{guitar}")
            print(f"Back: {guitar.spec.back_wood.name.lower()}, Top: {guitar.spec.top_wood.name.lower()}, Strings: {guitar.spec.num_strings}")
            print(f"Price: ${guitar.price}")
    else:
        print("Sorry, Erin, we have no guitars for you.")

    if matching_mandolins:
        print("\nErin, you might like these mandolins:")
        for mandolin in matching_mandolins:
            print(f"\n{mandolin}")
            print(f"Back: {mandolin.spec.back_wood.name.lower()}, Top: {mandolin.spec.top_wood.name.lower()}, Strings: {mandolin.spec.num_strings}")
            print(f"Price: ${mandolin.price}")
    else:
        print("Sorry, Erin, we have no mandolins for you.")
ce}!")
    else:
        print("Sorry, Erin, we have nothing for you.")
