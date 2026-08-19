#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import sys
from menu import Menu
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Scape Chicken - HayFarm")

        # Instantiate Menu and Level
        self.menu = Menu(self.window)
        self.level = Level(self.window, "Level 1")

    def run(self) -> None:
        # 1. Run the Menu
        self.menu.run()

        # 2. Run the Level
        self.level.run()


if __name__ == "__main__":
    jogo = Game()
    jogo.run()