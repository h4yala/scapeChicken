#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from menu import Menu
from level import Level
from game_over import GameOver
from game_win import GameWin


class Game:
    def __init__(self):
        pygame.init()
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
            while jogador_vivo and current_level <= 6:
                level = Level(self.window, current_level, total_score)
                venceu, total_score = level.run()

                if venceu:
                    current_level += 1
                else:
                    jogador_vivo = False

            if not jogador_vivo:
                tela_final = GameOver(self.window, total_score)
            else:
                tela_final = GameWin(self.window, total_score)

            tela_final.run()


if __name__ == "__main__":
    jogo = Game()
    jogo.run()