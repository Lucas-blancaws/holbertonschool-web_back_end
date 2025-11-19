#!/usr/bin/env python3
"""Fonction sum_mixed_list avec annotations type"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return la somme d'une liste d'entiers et de floats"""
    return sum(mxd_lst)