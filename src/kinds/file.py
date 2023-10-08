from src.kinds.location import Location
from src.kinds.term import Term
from src.enums.kind import Kind

from src.kinds.generics.obj import GenericNode


class File(GenericNode):
    def __init__(self, name: str, expression: Term, location: Location):
        super(File, self).__init__(Kind.NoneType, location)

        self._name = name
        self._expression = expression

    @property
    def name(self) -> str:
        return self._name

    @property
    def expression(self) -> Term:
        return self._expression
