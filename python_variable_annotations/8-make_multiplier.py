#!/usr/bin/env python3
"""Fonction sum_mixed_list avec annotations type"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return une fonction qui multiplie un float par multiplier"""
    def multiply(n: float) -> float:
        """Multiplie n par multiplier"""
        return n * multiplier
    return multiply
