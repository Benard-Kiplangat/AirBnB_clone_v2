#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the class Amenity"""
        super().__init__(*args, **kwargs)
