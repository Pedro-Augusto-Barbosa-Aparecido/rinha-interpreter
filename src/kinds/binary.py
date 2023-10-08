from src.enums.kind import Kind
from src.kinds.binary_op import BinaryOp
from src.kinds.location import Location
from src.kinds.term import Term

from src.kinds.generics.obj import GenericNode


class Binary(GenericNode):
    def __init__(self, kind: Kind, lhs: Term, op: BinaryOp, rhs: Term, location: Location):
        super(Binary, self).__init__(kind, location)

        self._lhs = lhs
        self._op = op
        self._rhs = rhs

    @property
    def lhs(self) -> Term:
        return self._lhs

    @property
    def rhs(self) -> Term:
        return self._rhs

    @property
    def op(self) -> BinaryOp:
        return self._op
