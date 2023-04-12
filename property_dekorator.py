from string import ascii_letters


class Person:
    S_UKR = 'абвгдеєжзиіїклмнопрстуфхцчшщюя-'
    S_UKR_UPPER = S_UKR.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_ps(ps)
        self.verify_weight(weight)

        self.__fio = fio.split()
        self.__old = old
        self.__ps = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("FIO - have to be STRING")
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Wrong format FIO")

        letters = ascii_letters + cls.S_UKR + cls.S_UKR_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("FIO has has to have min one symbol")
            if len(s.strip(letters)) != 0:
                raise TypeError("FIO must use only words and -")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('Wrong format OLD. Example - [14 - 120]')

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError('Wrong format WEIGHT')

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('Passport must be STRING')

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 2 or len(s[1]) != 6:
            raise TypeError('Wrong format PASSPORT [XX XXXXXX]')
        for p in s:
            if not p.isdigit():
                raise TypeError('Seria and number of passport must be INTEGER')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def ps(self):
        return self.__ps

    @ps.setter
    def ps(self, ps):
        self.verify_ps(ps)
        self.__ps = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight
p = Person('Марчук Володимир Володимирович', 38, '77 028387', 88.0)

