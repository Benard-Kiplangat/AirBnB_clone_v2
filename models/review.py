#!/usr/bin/python3
""" Review module for the HBNB project """
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes the class Review"""
        super().__init__(*args, **kwargs)
