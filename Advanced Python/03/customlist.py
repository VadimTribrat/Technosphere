class CustomList(list):
    def __init__(self, val=None):
        if val is None:
            val = []
        super().__init__(val)

    def __sub__(self, other):
        new_list = CustomList()
        min_len = len(self) if len(self) < len(other) else len(other)
        for i in range(min_len):
            new_list.append(self[i] - other[i])
        if len(self) > len(other):
            new_list.extend(self[min_len:])
        else:
            new_list.extend(other[min_len:])
        return new_list

    def __add__(self, other):
        new_list = CustomList()
        min_len = len(self) if len(self) < len(other) else len(other)
        for i in range(min_len):
            new_list.append(self[i] + other[i])
        if len(self) > len(other):
            new_list.extend(self[min_len:])
        else:
            new_list.extend(other[min_len:])
        return new_list

    def __neg__(self):
        return CustomList([-val for val in self])

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return super().__str__()

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __gt__(self, other):
        return not ((self == other) or (self < other))

    def __ge__(self, other):
        return not self < other

    def __le__(self, other):
        return not self > other

    def __ne__(self, other):
        return not self == other
