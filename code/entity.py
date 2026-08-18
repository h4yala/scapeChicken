#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

class Entity:
    def __init__(self, name: str, surf: pygame.Surface, rect: pygame.Rect):
        self.name = name
        self.surf = surf
        self.rect = rect

    def move(self) -> None:
        # To be overridden by child classes (Player, Enemy, etc.)
        pass
