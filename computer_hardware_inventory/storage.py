from resource import Resource


class Storage(Resource):
    """Base class for Storage devices"""

    def __init__(
        self,
        name: str,
        manufacturer: str,
        capacity_GB: int,
        total: int = 0,
        allocated: int = 0,
    ) -> None:
        super().__init__(name, manufacturer, total, allocated)
        self._capacity_GB = capacity_GB

    @property
    def capacity_GB(self):
        return self._capacity_GB
