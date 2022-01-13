"""Reproduce D418."""

import typing
from typing import overload as ov
from typing import overload, Any


class Magics:
    """A class with magic methods."""

    # 3 errors:
    # D107 for overloaded __init__
    # D105 for overloaded magic methods
    # D102 for naming decorator other than "overload"

    @overload
    def __init__(self, val: dict):
        """Not allowed."""
        ...

    @overload
    def __init__(self, val: str):
        ...

    def __init__(self, val):
        """Use with caution."""
        self.val = val

    @overload
    def __getitem__(self, idx_slice: int) -> int:
        ...

    @overload
    def __getitem__(self, idx_slice: slice) -> str:
        ...

    def __getitem__(self, idx_slice):
        """Return one val or slice of vals."""
        return self.val[idx_slice]

    @ov
    def greet(self, msg: str):
        ...

    @typing.overload
    def greet(self, msg: int):
        ...

    def greet(self, msg):
        """Print a greeting with `msg`."""
        print(f"Hello! {msg}")
