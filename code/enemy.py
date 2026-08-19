#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from entity import Entity

class Enemy(Entity):
    def __init__(self, surf: pygame.Surface, rect: pygame.Rect):
        super().__init__("Enemy", surf, rect)
        self.speed_x = 4
        self.speed_y = 4

    def move(self) -> None:
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bouncing logic (Assuming an 800x600 window)
        if self.rect.left < 0 or self.rect.right > 800:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.speed_y *= -1
