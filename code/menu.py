#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import sys


class Menu:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.title_font = pygame.font.Font("../assets/hayFarm.TTF", 65)
        self.font = pygame.font.Font("../assets/scapeChicken.ttf", 40)
        self.instruction_font = pygame.font.Font("../assets/game.ttf", 30)

    def run(self) -> None:
        menu_running = True
        clock = pygame.time.Clock()

        # --- Audio Setup ---
        pygame.mixer.init()
        pygame.mixer.music.load("../assets/menu-music.wav")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)

        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Para a música antes de sair do menu e ir para a fase
                        #pygame.mixer.music.stop()
                        menu_running = False

            # Drawing the Menu
            self.window.fill((104, 159, 56))

            title_text = self.title_font.render("SCAPE CHICKEN", True, (255, 255, 255))
            self.window.blit(title_text, title_text.get_rect(center=(self.window.get_width() // 2, 150)))

            controls_text = self.font.render("CONTROLS:", True, (0, 0, 0))
            self.window.blit(controls_text, controls_text.get_rect(center=(self.window.get_width() // 2, 300)))

            arrows_text = self.instruction_font.render("Use ARROW KEYS to move", True, (255, 255, 255))
            self.window.blit(arrows_text, arrows_text.get_rect(center=(self.window.get_width() // 2, 350)))

            start_text = self.instruction_font.render("Press SPACE to Start", True, (255, 255, 0))
            self.window.blit(start_text, start_text.get_rect(center=(self.window.get_width() // 2, 450)))

            pygame.display.flip()
            clock.tick(60)