class MyInt:
    def __init__(self, number: int):
        if isinstance(number, int):
            self.__number = number
        else:
            try:
                self.__number = int(number)
            except TypeError:
                raise ValueError("incorrect format")

    def __str__(self):
        return str(self.__number)

    def __repr__(self):
        return f"current number: {self.__number}"

    @classmethod
    def __get_formatted(cls, number):
        if isinstance(number, int):
            return number
        else:
            try:
                return int(number)
            except TypeError:
                raise ValueError("incorrect second operand")

    def __add__(self, other):
        return MyInt(self.__number + self.__get_formatted(other))

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.__number += self.__get_formatted(other)
        return self

    def __sub__(self, other):
        return MyInt(self.__number - self.__get_formatted(other))

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        self.__number -= self.__get_formatted(other)
        return self

    def __mul__(self, other):
        return MyInt(self.__number * self.__get_formatted(other))

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.__number *= self.__get_formatted(other)
        return self

    def __truediv__(self, other):
        return MyInt(self.__number / self.__get_formatted(other))

    def __rtruediv__(self, other):
        return self / other

    def __itruediv__(self, other):
        self.__number /= self.__get_formatted(other)
        return self

    def __eq__(self, other):
        return self.__number == self.__get_formatted(other)

    def __lt__(self, other):
        return self.__number < self.__get_formatted(other)

    def __le__(self, other):
        return self.__number <= self.__get_formatted(other)


a = MyInt(6)
print(f"a={a}")
a += '4'
print(f"a+4 = {a} (refactor a)")
print(f"is (a-5) < '6'? {a-5 < '6'}")
print(f"is (a*2) = 21? {a*2 == 21}")
print(f" is a/5 <= 2? {a/5 <= 2}")

