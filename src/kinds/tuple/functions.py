from src.enums.kind import Kind
from src.kinds.location import Location
from src.kinds.term import Term

from src.kinds.generics.obj import GenericNode


class First(GenericNode):
    def __init__(self, kind: Kind, value: Term, location: Location):
        super(First, self).__init__(kind, location)

        self._value = value

    @property
    def value(self) -> Term:
        return self._value


class Second(GenericNode):
    def __init__(self, kind: Kind, value: Term, location: Location):
        super(Second, self).__init__(kind, location)

        self._value = value

    @property
    def value(self) -> Term:
        return self._value
