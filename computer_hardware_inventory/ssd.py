from storage import Storage


class SSD(Storage):
    def __init__(
        self,
        name: str,
        manufacturer: str,
        capacity_GB: int,
        interface: str,
        total: int = 0,
        allocated: int = 0,
    ) -> None:
        super().__init__(name, manufacturer, capacity_GB, total, allocated)
        self._interface = interface

    @property
    def interface(self) -> str:
        return self._interface
