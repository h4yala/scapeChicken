#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import sys
import random
from entityFactory import EntityFactory


class Level:
    def __init__(self, window: pygame.Surface, name: str):
        self.window = window
        self.name = name
        self.entity_list = []
        self.score = 0
        self.lives = 3
        self.fruit_count = 0
        self.jelly_count = 0
        self.ui_font = pygame.font.Font("../assets/game.ttf", 36)

        # --- UI Elements ---
        # Lives
        self.tomato_img = pygame.image.load("../assets/tomato.png").convert_alpha()
        tomato_size = self.tomato_img.get_size()
        self.tomato_img = pygame.transform.scale(self.tomato_img, (tomato_size[0] * 3, tomato_size[1] * 3))

        # Jellies
        self.jelly_img = pygame.image.load("../assets/fruit_jar.png").convert_alpha()
        jelly_size = self.jelly_img.get_size()
        self.jelly_img = pygame.transform.scale(self.jelly_img, (jelly_size[0] * 3, jelly_size[1] * 3))

        # --- Audio Setup (SFX & BGM Volume) ---
        # Efeitos sonoros (SFX)
        self.som_dano = pygame.mixer.Sound("../assets/dano.wav")
        self.som_geleia = pygame.mixer.Sound("../assets/geleia.wav")
        self.som_dano.set_volume(1.0)
        self.som_geleia.set_volume(1.0)

        # --- Invincibility Variables ---
        self.is_invincible = False
        self.last_hit_time = 0
        self.invincibility_duration = 1500  # 1.5 seconds in milliseconds

        # 1. Background
        bg = EntityFactory.get_entity("Background", self.window)
        if bg: self.entity_list.append(bg)

        # 2. Player
        self.player = EntityFactory.get_entity("Player", self.window)
        if self.player: self.entity_list.append(self.player)

        # 3. Enemy
        self.enemy = EntityFactory.get_entity("Enemy", self.window)
        if self.enemy: self.entity_list.append(self.enemy)

        # 4. Fruit (Temporary static logic)
        self.fruit = pygame.image.load("../assets/fruit.png").convert_alpha()
        fruit_size = self.fruit.get_size()
        self.fruit = pygame.transform.scale(self.fruit, (fruit_size[0] * 3, fruit_size[1] * 3))
        random_x = random.randint(50, 750)
        random_y = random.randint(50, 550)
        self.fruit_rect = self.fruit.get_rect(center=(random_x, random_y))

    def run(self) -> int:
        level_running = True
        clock = pygame.time.Clock()

        pygame.mixer.music.set_volume(0.2)

        while level_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # --- LOGIC & MOVEMENT ---
            current_time = pygame.time.get_ticks()

            for entity in self.entity_list:
                entity.move()

            # Fruit Collision & Crafting Logic
            if self.player.rect.colliderect(self.fruit_rect):
                self.fruit_count += 1
                self.score += 10  # 10 points per fruit just for fun!

                # Move the fruit to a new random location
                random_x = random.randint(50, 750)
                random_y = random.randint(50, 550)
                self.fruit_rect.center = (random_x, random_y)

                # Check if we have enough fruits to craft a jelly
                if self.fruit_count >= 3:
                    self.fruit_count = 0
                    self.jelly_count += 1
                    self.som_geleia.play()
                    print("Jelly Crafted!")
                    # AQUI É ONDE VAMOS COLOCAR O SOM DA GELÉIA NO PRÓXIMO PASSO!

            # Enemy Collision (Only hits if NOT invincible)
            if self.player.rect.colliderect(self.enemy.rect) and not self.is_invincible:
                self.lives -= 1
                self.is_invincible = True
                self.last_hit_time = current_time
                self.som_dano.play()

                if self.lives <= 0:
                    pygame.mixer.music.stop()
                    return self.score

            # --- Invincibility & Blinking Logic ---
            if self.is_invincible:
                # Check if the time is up
                if current_time - self.last_hit_time > self.invincibility_duration:
                    self.is_invincible = False
                    self.player.surf.set_alpha(255)  # Back to normal (fully visible)
                else:
                    # Blinking math: switch between 0 (invisible) and 255 (visible) every 200ms
                    if (current_time // 200) % 2 == 0:
                        self.player.surf.set_alpha(255)
                    else:
                        self.player.surf.set_alpha(0)

            # --- DRAWING ---
            self.window.fill((0, 0, 0))  # Base cleaner

            for entity in self.entity_list:
                self.window.blit(entity.surf, entity.rect)

            self.window.blit(self.fruit, self.fruit_rect)

            # --- Drawing the Inventory UI ---
            fruit_text = self.ui_font.render(f"Fruits: {self.fruit_count}/3", True, (255, 255, 255))
            self.window.blit(fruit_text, (20, 20))

            for i in range(self.jelly_count):
                x_pos = 20 + (i * 40)
                y_pos = 60
                self.window.blit(self.jelly_img, (x_pos, y_pos))

            self.window.blit(fruit_text, (20, 20))

            # --- Drawing the Tomato Lives UI ---
            for i in range(self.lives):
                x_position = 750 - (i * 50)
                y_position = 20
                self.window.blit(self.tomato_img, (x_position, y_position))

            pygame.display.flip()
            clock.tick(60)