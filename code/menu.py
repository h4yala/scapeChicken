#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import sys
from const import *

class Menu:
    def __init__(self, window: pygame.Surface):
        self.window = window

        # Carrega a arte de fundo do Menu
        self.bg_img = pygame.image.load("../assets/menu_bg.png").convert()
        self.bg_img = pygame.transform.scale(self.bg_img, (WIN_WIDTH, WIN_HEIGHT))

        pygame.mixer.init()
        pygame.mixer.music.load("../assets/menu-music.wav")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, align: str = "topleft"):
        font = pygame.font.Font("../assets/game.ttf", text_size)
        text_surf = font.render(text, True, text_color)

        if align == "center":
            text_rect = text_surf.get_rect(center=text_pos)
        else:
            text_rect = text_surf.get_rect(topleft=text_pos)

        self.window.blit(text_surf, text_rect)


    def run(self) -> None:
        menu_running = True
        clock = pygame.time.Clock()

        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        menu_running = False

            # drawing
            self.window.blit(self.bg_img, (0, 0))

            title_font = pygame.font.Font("../assets/scapeChicken.ttf", 60)
            title_surf = title_font.render("SCAPE CHICKEN", True, C_RED)
            self.window.blit(title_surf, title_surf.get_rect(center=(WIN_WIDTH / 2, 150)))

            # loop menu
            for i in range(len(MENU_OPTION)):
                self.menu_text(40, MENU_OPTION[i], C_BLUE, (50, 230 + 50 * i))

            self.menu_text(25, "Aperte a tecla ESPAÇO para jogar", C_WHITE, (WIN_WIDTH / 2, 575), "center")

            pygame.display.flip()
            clock.tick(60)