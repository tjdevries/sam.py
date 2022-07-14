"""
This is the file that actually does things

CI Attempt: 4
"""

from typing import Sequence

import sqlparse

from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        print("starting save...")
        super().save(*args, **kwargs)  # Call the "real" save() method.
        print("... all done!")

class ShouldConsole:
    def __init__(self):
        self.x: int = 1
        print(sqlparse.format)

    def other(self):
        print(self.x)

class InheritsConsole(ShouldConsole):
    def other(self):
        print("OTHER", self.x)

    def unrelated(self):
        print("NOT RELATED")

def x(s: Sequence[int]):
    print([x for x in s])
