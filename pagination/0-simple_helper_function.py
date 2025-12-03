#!/usr/bin/env python3
"""Function index_rang."""


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple for pagination."""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
