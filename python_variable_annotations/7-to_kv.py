#!/usr/bin/env python3
"""Fonction to_kv avec annotations de type"""

def to_kv(k: str, v: int | float) -> tuple:
    """Return un tuple avec la chaîne k et le carré de v en float"""
    return (k, v)