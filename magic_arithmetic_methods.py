class Clock:
    """Магічні методи арифметичних операцій"""
    """__add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__"""
    """__iadd__, __isub__, __imul__, __itruediv__, __ifloordiv__, __imod__"""
    __DAY = 86400  # quantity of seconds in one day

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("The seconds have to be INTEGER!")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):  # Оператор додавання знаходиться зправа
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("The right operand has to be INTEGER or Clock!")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):  # Оператор додавання знаходиться зліва
        return self + other

    def __iadd__(self, other):  # Операція +=
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("The right operand has to be INTEGER or Clock!")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds += sc
        return self


c1 = Clock(620)
print(c1.get_time())
c1 = 100 + c1
print(c1.get_time())
