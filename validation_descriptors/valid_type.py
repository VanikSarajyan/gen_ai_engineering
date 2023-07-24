class ValidType:
    def __init__(self, type):
        self._type = type

    def __set_name__(self, owner, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise ValueError(f"{self.prop_name} must be type of {self._type.__name__}")
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)


class Person:
    age = ValidType(int)
    height = ValidType(float)
    tags = ValidType(list)
    favorite_foods = ValidType(tuple)
    name = ValidType(str)


if __name__ == "__main__":
    p = Person()

    try:
        p.age = 22.5
    except ValueError as ex:
        print(ex)

    try:
        p.height = 12
    except ValueError as ex:
        print(ex)

    p.age = 15

    print(p.age)

    print(p.tags)
    p.tags = ["a", "b"]
    print(p.tags)
