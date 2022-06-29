"""
This is the file that actually does things

CI Attempt: 2
"""

import sqlparse
from sqlparse import sql

class ShouldConsole:
    def __init__(self):
        self.x = 1
        print(sqlparse.format)
        print(sql.NameAliasMixin)

    def other(self):
        print(self.x)
