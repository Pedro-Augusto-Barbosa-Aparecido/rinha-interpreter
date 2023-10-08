from src.enums.kind import Kind
from src.kinds.generics.obj import GenericNode
from src.kinds.location import Location
from src.kinds.parameter import Parameter
from src.kinds.term import Term


class Let(GenericNode):
    def __init__(self, kind: Kind, name: Parameter, value: Term, _next: Term, location: Location):
        super(Let, self).__init__(kind, location)

        self._name = name
        self._value = value
        self._next = _next

    @property
    def name(self) -> Parameter:
        return self._name

    @property
    def then(self) -> Term:
        return self._value

    @property
    def otherwise(self) -> Term:
        return self._next
