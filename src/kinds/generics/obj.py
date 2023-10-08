from src.enums.kind import Kind
from src.kinds.location import Location


class GenericNode:
    def __init__(self, kind: Kind, location: Location):
        self._kind = kind
        self._location = location

    @property
    def kind(self) -> Kind:
        return self._kind

    @property
    def location(self) -> Location:
        return self._location
