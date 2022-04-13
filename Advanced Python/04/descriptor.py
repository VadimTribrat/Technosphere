class Integer:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, owner):
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise Exception("Not int")
        obj.__dict__[self.name] = value


class String:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, owner):
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise Exception("Not str")
        obj.__dict__[self.name] = value


class PositiveInteger:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, owner):
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise Exception("Not int")
        if value <= 0:
            raise Exception("Nonpositive value")
        obj.__dict__[self.name] = value


class Data:
    num = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self, num, name, price):
        self.num = num
        self.name = name
        self.price = price

    def get_values(self):
        return self.num, self.name, self.price
