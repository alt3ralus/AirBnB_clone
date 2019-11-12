#!/usr/bin/python3
"""City class that inherits from BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """All the cities the user can choose in the app."""
        super().__init__(self, *args, **kwargs)
