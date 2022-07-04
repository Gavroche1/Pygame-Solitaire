""" This file contains the class which manages the events """

import pygame

class Event:
    """ This class manages the events """

    def __init__(self):
        """ Initialize """

        self.dict_evt = {}

    def add_event(self, type_evt, callback):
        """ Add a event """

        self.dict_evt[type_evt] = callback

    def execute(self):
        """ Execute the callbacks of the events """

        for evt in pygame.event.get():
            if evt.type in self.dict_evt:
                self.dict_evt[evt.type](evt)
