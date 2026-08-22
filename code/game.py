#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from menu import Menu
from level import Level
from game_over import GameOver


class Game:
    def __init__(self):
        pygame.init()
        # Se você colocou WIN_WIDTH no Const.py, pode importar e usar aqui também!
        self.width = 800
        self.height = 600
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Scape Chicken - HayFarm")

    def run(self) -> None:
        while True:
            menu = Menu(self.window)
            menu.run()

            current_level = 1
            total_score = 0
            jogador_vivo = True

            # loop das fases
            while jogador_vivo:
                level = Level(self.window, current_level, total_score)

                venceu, total_score = level.run()

                if venceu:
                    current_level += 1
                    print(f"Iniciando Nível {current_level}...")
                else:
                    jogador_vivo = False

            tela_morte = GameOver(self.window, total_score)
            tela_morte.run()


if __name__ == "__main__":
    jogo = Game()
    jogo.run()