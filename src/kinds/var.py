from src.enums.kind import Kind
from src.kinds.location import Location


class Var:
    def __init__(self, kind: Kind, text: str, location: Location):
        self._kind = kind
        self._text = text
        self._location = location

    @property
    def kind(self) -> Kind:
        return self._kind

    @property
    def text(self) -> str:
        return self._text

    @property
    def location(self) -> Location:
        return self._location
