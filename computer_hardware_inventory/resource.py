class Resource:
    """Base class for inventory resources"""

    def __init__(
        self, name: str, manufacturer: str, total: int = 0, allocated: int = 0
    ) -> None:
        self._name = name
        self._manufacturer = manufacturer
        self._total = total
        self._allocated = allocated

    @property
    def category(self) -> str:
        return self.__class__.__name__.lower()

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    def claim(self, n: int) -> None:
        n = self.__validate_n(n)
        if self._allocated + n > self._total:
            raise ValueError(f"Not enough {self._name}(s) to claim.")

        self._allocated += n
        print(f"Successfully claimed {n} {self._name}(s).")

    def freeup(self, n: int) -> None:
        n = self.__validate_n(n)
        if n > self._allocated:
            raise ValueError("Can't free more than allocated.")

        self._allocated -= n
        print(f"Successfully freed up {n} {self._name}(s).")

    def died(self, n: int) -> None:
        n = self.__validate_n(n)
        if n > self._total:
            raise ValueError(f"Can't remove more {self._name}(s) than exists.")
        # Assuming that we first remove from not allocated
        if self._allocated > self._total:
            self.allocated = self.total
        print(f"Successfully removed {n} {self._name}(s).")

    def purchased(self, n: int) -> None:
        n = self.__validate_n(n)
        self._total += n
        print(f"Successfully purchased {n} {self._name}(s).")

    def __validate_n(self, n: int) -> int:
        if not isinstance(n, int):
            raise ValueError("Number must be integer")
        if n < 0:
            raise ValueError("Number must be positive")

        return n

    def __str__(self) -> str:
        return self.__name

    def __gather_attrs(self) -> str:
        attrs = []
        for key in self.__dict__:
            attrs.append(f"{key}={getattr(self, key)}")
        return ", ".join(attrs)

    def __repr__(self):
        return f"[{self.__class__.__name__}: {self.__gather_attrs()}]"
