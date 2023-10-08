from src.enums.kind import Kind
from src.kinds.location import Location
from src.kinds.generics.obj import GenericNode


class Var(GenericNode):
    def __init__(self, kind: Kind, text: str, location: Location):
        super(Var, self).__init__(kind, location)

        self._text = text

    @property
    def text(self) -> str:
        return self._text
