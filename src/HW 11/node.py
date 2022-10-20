"""
CSCI-141 Computer Science 1 Presentation Code
11-StacksQueues
Node

This is the definition of a singly linked node structure that will be used as
the internal representation of our stack and queue structures.
"""

from dataclasses import dataclass
from typing import Any, Union

@dataclass
class Node:
    value: Any
    next: Union[None, 'Node']
    __slots__ = "value", "next"