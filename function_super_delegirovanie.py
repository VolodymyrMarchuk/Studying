class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        print(f"Inicialisation of {self.__class__}")


class Line(Geom):
    def draw(self):
        print("Draw a line!")


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        self.fill = fill
        print("Inicialisation of Rect")

    def draw(self):
        print("Draw a Square!")


l = Line(0, 0, 10, 20)
r = Rect(10, 20, 30, 40)
