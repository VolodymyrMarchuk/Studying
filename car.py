class Car:
    """My training of Classes"""
    def __init__(self, brand, year, price, odometr):
        self.brand = brand
        self.year = year
        self.price = price
        self.odometr = odometr

    def odometr_d(self):
        new_odometr = (int(input("What is the year now? ")) - self.year)*25000 + self.odometr
        return new_odometr


car_1 = Car("BMW", 2020, 12000.00, 250000)
od = car_1.odometr_d()
print(f"{car_1.brand} year = {car_1.year} price = {car_1.price}")
print(f"Odometr = {od}")

