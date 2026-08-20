#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import sys
from menu import Menu
from level import Level
from game_over import GameOver  # Importa a classe nova!


class Game:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Scape Chicken - HayFarm")

    def run(self) -> None:
        # Loop infinito da Máquina de Estados
        while True:
            # 1. Roda o Menu
            menu = Menu(self.window)
            menu.run()

            # 2. Roda a Fase e salva os pontos quando o jogador morrer
            level = Level(self.window, "Level 1")
            pontuacao_final = level.run()

            # 3. Roda o Game Over passando os pontos
            tela_morte = GameOver(self.window, pontuacao_final)
            tela_morte.run()


if __name__ == "__main__":
    jogo = Game()
    jogo.run()