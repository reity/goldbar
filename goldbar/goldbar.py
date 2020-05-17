"""GOLDBAR embedded language for genetic designs.

Embedded language for defining and working with genetic
design spaces using GOLDBAR.
"""

from __future__ import annotations
from typing import Sequence
import doctest

#
# Foundational data structures shared across the
# data structures defined in this module.
#

class label(str):
    '''
    Abstract data structure for a part or graph node label.
    '''
    pass

class orientation(str):
    '''
    Abstract data structure for a part orientation attribute.
    '''
    pass

class roles(list):
    '''
    Abstract data structure for a list of part roles.
    '''
    pass

class part(tuple):
    '''
    Abstract data structure for a part. This tuple may have
    one of the following three configurations:
     * (label, roles, orientation)
     * (label, roles)
     * (label, orientation)
    '''
    pass

#
# Sequences.
#

class sequence(tuple):
    '''
    Abstract data structure for a sequence of parts.
    '''
    pass

#
# GOLDBAR syntax.
#

class operation(str):
    '''
    Abstract data structure for a GOLDBAR operation.
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

#
# Design space graphs.
#

class annotation(set):
    '''
    A node annotation: a subset of {'start', 'accept'}.
    '''
    pass

class node(tuple):
    '''
    Abstract data structure for a design space graph node.
    '''
    pass

class edge(tuple):
    '''
    Abstract data structure for a design space graph edge.
    '''
    pass

class graph(tuple):
    '''
    Abstract data structure for a design space graph.
    '''
    pass

if __name__ == "__main__":
    doctest.testmod()
