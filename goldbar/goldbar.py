"""GOLDBAR embedded language for genetic designs.

Embedded language for defining and working with genetic
design spaces.
"""

from __future__ import annotations
from typing import Sequence
import doctest

class operation(str):
    '''
    Abstract data structure for an operation.
    '''
    pass

class goldbar(dict):
    """
    Class for GOLDBAR genetic design data structure instances.
    """

    def zero_or_one(self: goldbar) -> goldbar:
        return goldbar({operation('zero-or-one'): [self]})

    def __invert__(self: goldbar) -> goldbar:
        '''Embedded operator synonym for `zero_or_one`.'''
        return self.zero_or_one()

    def zero_or_more(self: goldbar) -> goldbar:
        return goldbar({operation('zero-or-more'): [self]})

    def __neg__(self: goldbar) -> goldbar:
        '''Embedded operator synonym for `zero_or_more`.'''
        return self.zero_or_more()

    def one_or_more(self: goldbar) -> goldbar:
        return goldbar({operation('one-or-more'): [self]})

    def __pos__(self: goldbar) -> goldbar:
        '''Embedded operator synonym for `one_or_more`.'''
        return self.one_or_more()

    def then(self: goldbar, other: goldbar) -> goldbar:
        return are({operation('then'): [self, other]})

    def __rshift__(self: goldbar, other: goldbar) -> goldbar:
        return self.then(other)

    def or_(self: goldbar, other: goldbar) -> goldbar:
        return are({operation('then'): [self, other]})

    def __or__(self: goldbar, other: goldbar) -> goldbar:
        return self.or_(other)

    def and_(self: goldbar, other: goldbar) -> goldbar:
        return are({operation('then'): [self, other]})

    def __and__(self: goldbar, other: goldbar) -> goldbar:
        return self.and_(other)

if __name__ == "__main__":
    doctest.testmod()
