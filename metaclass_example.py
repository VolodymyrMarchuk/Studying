class Meta(type):
    def creat_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, bases, attrs):
        super().__init__()
        cls.class_attrs = attrs
        cls.__init__ = Meta.creat_local_attrs


class Women(metaclass=Meta):
    title = 'Заголовки'
    content = 'Контент'
    photo = 'Шлях до фото'


w = Women()
print(w.__dict__)
