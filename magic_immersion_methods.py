class Clock:
    """Магічні методи порівняльних операцій"""
    """__eq__, __ne__, __lt__, __le__, __gt__, __ge__"""
    __DAY = 86400  # quantity of seconds in one day

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("The seconds have to be INTEGER!")
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Operand need to be INTEGER or Clock!')
        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc


c1 = Clock(1000)
c2 = Clock(1000)
print(c1 < c2)