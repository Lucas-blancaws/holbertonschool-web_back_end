#!/usr/bin/env python3
"""Fonction to_kv avec annotations type"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return un tuple avec la chaîne k et le carré de v en float"""
    return (k, v ** 2)