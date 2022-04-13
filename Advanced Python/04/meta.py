class CustomMeta(type):
    def __new__(cls, name, bases, classdict):
        def __setattr__(self, name, value):
            self.__dict__['custom_' + name] = value
        new_dict = {}
        new_dict['__setattr__'] = __setattr__
        for key, val in classdict.items():
            if not (key[:2] == '__' and key[-2:] == '__'):
                new_dict['custom_' + key] = val
            else:
                new_dict[key] = val
        return super().__new__(cls, name, bases, new_dict)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def print(self):
        pass

    def get_x(self):
        return CustomClass.custom_x

    def get_val(self):
        return self.custom_val
