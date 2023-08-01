class NDimSlottedPointMeta(type):
    def __new__(mcs, name, bases, namespace):
        if "__slots__" not in namespace:
            raise AttributeError(f"{name} class must have __slots__ attribute.")

        slots = namespace["__slots__"]
        dim = len(slots)

        def __init__(self, *args):
            if len(args) != dim:
                raise TypeError(
                    f"{self.__class__.__name__} __init__ takes {dim} coordinates."
                )
            for i, slot in enumerate(slots):
                setattr(self, slot, args[i])

        def __repr__(self):
            coordinates = ", ".join(
                f"{slot}={str(getattr(self, slot))}" for slot in self.__slots__
            )
            return f"{self.__class__.__name__} ({coordinates})"

        def __eq__(self, other):
            return isinstance(other, self.__class__) and all(
                getattr(self, slot) == getattr(other, slot) for slot in slots
            )

        def __hash__(self):
            return hash(tuple(getattr(self, slot) for slot in slots))

        namespace["__init__"] = __init__
        namespace["__repr__"] = __repr__
        namespace["__eq__"] = __eq__
        namespace["__hash__"] = __hash__

        return super().__new__(mcs, name, bases, namespace)


class Point2D(metaclass=NDimSlottedPointMeta):
    __slots__ = ("x", "y")


class Point3D(metaclass=NDimSlottedPointMeta):
    __slots__ = ("x", "y", "z")


if __name__ == "__main__":
    p1 = Point2D(5, 10)
    p2 = Point2D(5, 10)
    p3 = Point3D(6, 6, 6)

    print(p2 == p1)
    print(p2 == p3)

    print(p2)
    print(p3)

    print(hash(p1))
    print(hash(p2))

    p3.z = 10
    print(p3)
