from storage import Storage


class HDD(Storage):
    def __init__(
        self,
        name: str,
        manufacturer: str,
        capacity_GB: int,
        size: float,
        rpm: int,
        total: int = 0,
        allocated: int = 0,
    ) -> None:
        super().__init__(name, manufacturer, capacity_GB, total, allocated)
        self._size = size
        self._rpm = rpm

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm
