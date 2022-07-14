"""
This is the file that actually does things

CI Attempt: 4
"""

from typing import Sequence

import sqlparse

class ShouldConsole:
    def __init__(self):
        self.x: int = 1
        print(sqlparse.format)

    def other(self):
        print(self.x)

class InheritsConsole(ShouldConsole):
    def other(self):
        print("OTHER", self.x)

def x(s: Sequence[int]):
    print([x for x in s])
