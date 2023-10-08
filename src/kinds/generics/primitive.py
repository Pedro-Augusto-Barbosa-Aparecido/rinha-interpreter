from typing import Generic, TypeVar

from src.enums.kind import Kind
from src.kinds.location import Location


T = TypeVar("T")


class Primitive(Generic[T]):
    def __init__(self, kind: Kind, value: T, location: Location):
        self._kind = kind
        self._value = value
        self._location = location

    @property
    def kind(self) -> Kind:
        return self._kind

    @property
    def value(self) -> T:
        return self._value

    @property
    def location(self) -> Location:
        return self._location
