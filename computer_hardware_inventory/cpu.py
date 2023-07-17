from resource import Resource


class CPU(Resource):
    def __init__(
        self,
        name: str,
        manufacturer: str,
        cores: int,
        interface: str,
        socket: str,
        power_watts: int,
        total=0,
        allocated=0,
    ):
        super().__init__(name, manufacturer, total, allocated)
        self._cores = cores
        self._interface = interface
        self._socket = socket
        self._power_watts = power_watts

    @property
    def cores(self) -> int:
        return self._cores

    @property
    def socket(self) -> str:
        return self._socket

    @property
    def interface(self) -> str:
        return self._interface

    @property
    def power_watts(self) -> int:
        return self._power_watts
