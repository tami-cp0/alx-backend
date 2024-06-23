#!/usr/bin/env python3
"""
Module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns:
        Atuple containing the start and end indexes of the required data
    """
    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)
