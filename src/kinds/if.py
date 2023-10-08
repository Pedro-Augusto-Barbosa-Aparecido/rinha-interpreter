from src.enums.kind import Kind
from src.kinds.location import Location
from src.kinds.term import Term
from src.kinds.generics.obj import GenericNode


class If(GenericNode):
    def __init__(self, kind: Kind, condition: Term, then: Term, otherwise: Term, location: Location):
        super(If, self).__init__(kind, location)

        self._condition = condition
        self._then = then
        self._otherwise = otherwise

    @property
    def condition(self) -> Term:
        return self._condition

    @property
    def then(self) -> Term:
        return self._then

    @property
    def otherwise(self) -> Term:
        return self._otherwise
