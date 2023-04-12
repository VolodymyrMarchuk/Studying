from dataclasses import dataclass, field


class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f"Thing: {self.__dict__}"


@dataclass
class ThingData:
    name: str
    weight: int
    price: float = 0
    dims: list = field(default_factory=list)


td = ThingData('Vova', 90, 25)
t = Thing('Vova', 90, 25)
print(td)
