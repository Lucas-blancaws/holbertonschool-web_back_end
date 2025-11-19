#!/usr/bin/env python3
"""Fonction element_length avec annotations de type"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Retourne une liste de tuples avec chaque séquence et sa longueur"""
    return [(i, len(i)) for i in lst]
