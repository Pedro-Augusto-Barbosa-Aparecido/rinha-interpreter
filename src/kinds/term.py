from typing import TypeVar, Generic

from src.kinds.location import Location
from src.enums.kind import Kind
from src.kinds.generics.obj import GenericNode
from src.kinds.primitives.int import Int
from src.kinds.primitives.str import Str
from src.kinds.primitives.bool import Bool

TermType = TypeVar("TermType", bound=Int | Str | Bool)


class Term(GenericNode, Generic[TermType]):
    def __init__(self, kind: Kind, value: TermType, location: Location):
        super(Term, self).__init__(kind, location)

        self._value = value

    @property
    def value(self) -> TermType:
        return self._value
