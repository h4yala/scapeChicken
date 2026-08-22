#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from entity import Entity

class Background(Entity):
    def __init__(self, surf: pygame.Surface, rect: pygame.Rect):
        super().__init__("Background", surf, rect)

    def move(self) -> None:
        pass