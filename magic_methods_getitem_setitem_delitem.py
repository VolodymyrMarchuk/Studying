class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        return self.marks[item]

    def __setitem__(self, key, value):
        self.marks[key] = value

    def __delitem__(self, key):
        del self.marks[key]



s1 = Student("Sergey", [5, 5, 3, 2, 5])
del s1[4]
print(s1.marks)