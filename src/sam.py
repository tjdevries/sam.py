"""
This is the file that actually does things

CI Attempt: 2
"""

import sqlparse
from sqlparse import sql

import json_to_model
from yaml import dump

class ShouldConsole:
    def __init__(self):
        self.x: int = 1
        print(sqlparse.format)
        print(sql.NameAliasMixin)
        print(json_to_model)
        print(dump)

    def other(self):
        print(self.x)
