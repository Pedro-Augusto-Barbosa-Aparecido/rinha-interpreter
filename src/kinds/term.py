from typing import Any

from src.kinds.location import Location
from src.enums.kind import Kind


class Term:
    def __init__(self, kind: Kind, value: Any, location: Location):
        self._kind = kind
        self._value = value
        self._location = location

    @property
    def kind(self) -> Kind:
        return self._kind

    @property
    def value(self) -> Any:
        return self._value

    @property
    def location(self) -> Location:
        return self._location
