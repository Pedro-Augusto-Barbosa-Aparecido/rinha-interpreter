from src.enums.kind import Kind
from src.kinds.location import Location
from src.kinds.term import Term

from src.kinds.generics.obj import GenericNode


class Tuple(GenericNode):
    def __init__(self, kind: Kind, first: Term, second: Term, location: Location):
        super(Tuple, self).__init__(kind, location)

        self._first = first
        self._second = second

    @property
    def first(self) -> Term:
        return self._first

    @property
    def second(self) -> Term:
        return self._second
