class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwds)
        return cls._instances[cls]


if __name__ == "__main__":

    class DB(metaclass=SingletonMeta):
        pass

    class State(metaclass=SingletonMeta):
        pass

    d1 = DB()
    d2 = DB()

    s1 = State()
    s2 = State()

    print(d1 is d2)
    print(s1 is s2)
