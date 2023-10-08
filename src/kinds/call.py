from typing import List

from src.enums.kind import Kind
from src.kinds.generics.obj import GenericNode
from src.kinds.location import Location
from src.kinds.term import Term


class Call(GenericNode):
    def __init__(self, kind: Kind, callee: Term, arguments: List[Term], location: Location):
        super(Call, self).__init__(kind, location)

        self._callee = callee
        self._arguments = arguments

    @property
    def arguments(self) -> List[Term]:
        return self._arguments

    @property
    def calle(self) -> Term:
        return self._callee
