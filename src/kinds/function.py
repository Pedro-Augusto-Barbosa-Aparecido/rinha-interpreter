from typing import List

from src.enums.kind import Kind
from src.kinds.generics.obj import GenericNode
from src.kinds.location import Location
from src.kinds.parameter import Parameter
from src.kinds.term import Term


class Function(GenericNode):
    def __init__(self, kind: Kind, parameters: List[Parameter], value: Term, location: Location):
        super(Function, self).__init__(kind, location)

        self._parameters = parameters
        self._value = value

    @property
    def parameters(self) -> List[Parameter]:
        return self._parameters

    @property
    def value(self) -> Term:
        return self._value
