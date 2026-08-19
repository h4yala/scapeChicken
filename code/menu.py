#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import sys


class Menu:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.title_font = pygame.font.Font(None, 80)
        self.font = pygame.font.Font(None, 40)
        self.instruction_font = pygame.font.Font(None, 30)

    def run(self) -> None:
        menu_running = True
        clock = pygame.time.Clock()

        # Menu loop
        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # If SPACE is pressed, exit the menu loop to start the game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        menu_running = False

                        # Drawing the Menu
            self.window.fill((104, 159, 56))  # Darker green background

            title_text = self.title_font.render("SCAPE CHICKEN", True, (255, 255, 255))
            self.window.blit(title_text, title_text.get_rect(center=(self.window.get_width() // 2, 150)))

            # Displaying required controls
            controls_text = self.font.render("CONTROLS:", True, (0, 0, 0))
            self.window.blit(controls_text, controls_text.get_rect(center=(self.window.get_width() // 2, 300)))

            arrows_text = self.instruction_font.render("Use ARROW KEYS to move", True, (255, 255, 255))
            self.window.blit(arrows_text, arrows_text.get_rect(center=(self.window.get_width() // 2, 350)))

            start_text = self.instruction_font.render("Press SPACE to Start", True, (255, 255, 0))
            self.window.blit(start_text, start_text.get_rect(center=(self.window.get_width() // 2, 450)))

            pygame.display.flip()
            clock.tick(60)