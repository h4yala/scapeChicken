#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import sys
from entityFactory import EntityFactory


class Level:
    def __init__(self, window: pygame.Surface, name: str):
        self.window = window
        self.name = name
        self.entity_list = []

        # Game temporary variables (will be moved to proper UI class later)
        self.score = 0
        self.lives = 3
        self.font = pygame.font.Font(None, 40)

        # 1. Background ALWAYS created first so it stays behind everything
        bg = EntityFactory.get_entity("Background", self.window)
        if bg: self.entity_list.append(bg)

        # 2. Player
        self.player = EntityFactory.get_entity("Player", self.window)
        if self.player: self.entity_list.append(self.player)

        # 3. Enemy
        self.enemy = EntityFactory.get_entity("Enemy", self.window)
        if self.enemy: self.entity_list.append(self.enemy)

        # 4. Fruit (Still using the old method for now before we upgrade to multiple fruits)
        self.fruit = pygame.image.load("../assets/fruit.png").convert_alpha()
        fruit_size = self.fruit.get_size()
        self.fruit = pygame.transform.scale(self.fruit, (fruit_size[0] * 3, fruit_size[1] * 3))
        self.fruit_rect = self.fruit.get_rect(center=(400, 300))

    def run(self) -> None:
        level_running = True
        clock = pygame.time.Clock()

        while level_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Logic
            for entity in self.entity_list:
                entity.move()

            # Collisions (No position reset anymore!)
            if self.player.rect.colliderect(self.fruit_rect):
                self.score += 1
                self.fruit_rect.center = (200, 200)  # Temporary static spawn for testing

            if self.player.rect.colliderect(self.enemy.rect):
                self.lives -= 1
                # ADD THE BLINK/INVINCIBILITY LOGIC HERE SOON
                if self.lives <= 0:
                    print("GAME OVER")  # Temporary print

            self.window.fill((104, 159, 56))

            # Drawing
            for entity in self.entity_list:
                self.window.blit(entity.surf, entity.rect)

            self.window.blit(self.fruit, self.fruit_rect)


            pygame.display.flip()
            clock.tick(60)
