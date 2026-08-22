#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import sys
import random
from entityFactory import EntityFactory


class Level:
    def __init__(self, window: pygame.Surface, level_number: int, accumulated_score: int = 0):
        self.window = window
        self.level_number = level_number
        self.entity_list = []

        self.score = accumulated_score
        self.lives = 3

        self.fruit_count = 0
        self.jelly_count = 0

        self.ui_font = pygame.font.Font("../assets/game.ttf", 36)

        # --- visual design ---
        # lives
        self.tomato_img = pygame.image.load("../assets/tomato.png").convert_alpha()
        tomato_size = self.tomato_img.get_size()
        self.tomato_img = pygame.transform.scale(self.tomato_img, (tomato_size[0] * 3, tomato_size[1] * 3))

        # jellies
        self.jelly_img = pygame.image.load("../assets/fruit_jar.png").convert_alpha()
        jelly_size = self.jelly_img.get_size()
        self.jelly_img = pygame.transform.scale(self.jelly_img, (jelly_size[0] * 3, jelly_size[1] * 3))

        # --- audio setup ---
        self.som_dano = pygame.mixer.Sound("../assets/dano.wav")
        self.som_geleia = pygame.mixer.Sound("../assets/geleia.wav")
        self.som_dano.set_volume(1.0)
        self.som_geleia.set_volume(1.0)

        # --- invincibility variables ---
        self.is_invincible = False
        self.last_hit_time = 0
        self.invincibility_duration = 1500

        # 1. Background
        if self.level_number % 2 != 0:
            bg = EntityFactory.get_entity("Background_Claro", self.window)
        else:
            bg = EntityFactory.get_entity("Background_Escuro", self.window)

        if bg: self.entity_list.append(bg)

        # 2. Player
        self.player = EntityFactory.get_entity("Player", self.window)
        if self.player: self.entity_list.append(self.player)

        # 3. Enemy
        self.enemy = EntityFactory.get_entity("Enemy", self.window)
        if self.enemy:
            aumento_velocidade = (self.level_number - 1)
            self.enemy.speed_x += aumento_velocidade
            self.enemy.speed_y += aumento_velocidade

            self.entity_list.append(self.enemy)

        # 4. Fruit
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

            # --- movements ---
            current_time = pygame.time.get_ticks()

            for entity in self.entity_list:
                entity.move()

            # fruit collision & crafting logic
            if self.player.rect.colliderect(self.fruit_rect):
                self.fruit_count += 1
                self.score += 10

                # move the fruit to a new random location
                random_x = random.randint(50, 750)
                random_y = random.randint(50, 550)
                self.fruit_rect.center = (random_x, random_y)

                # check if we have enough fruits to craft a jelly
                if self.fruit_count >= 3:
                    self.fruit_count = 0
                    self.jelly_count += 1
                    self.som_geleia.play()
                    print("Jelly Crafted!")

                    if self.jelly_count >= self.level_number:
                        return True, self.score

            # enemy collision (only hits if NOT invincible)
            if self.player.rect.colliderect(self.enemy.rect) and not self.is_invincible:
                self.lives -= 1
                self.is_invincible = True
                self.last_hit_time = current_time
                self.som_dano.play()

                if self.lives <= 0:
                    return False, self.score

            # --- invincibility & blinking logic ---
            if self.is_invincible:

                if current_time - self.last_hit_time > self.invincibility_duration:
                    self.is_invincible = False
                    self.player.surf.set_alpha(255)
                else:

                    if (current_time // 200) % 2 == 0:
                        self.player.surf.set_alpha(255)
                    else:
                        self.player.surf.set_alpha(0)

            # --- drawing ---
            self.window.fill((0, 0, 0))  # cleaner

            for entity in self.entity_list:
                self.window.blit(entity.surf, entity.rect)

            self.window.blit(self.fruit, self.fruit_rect)

            # --- drawing inventory ---
            fruit_text = self.ui_font.render(f"Fruits: {self.fruit_count}/3", True, (255, 255, 255))
            self.window.blit(fruit_text, (20, 20))

            level_text = self.ui_font.render(f"Fase: {self.level_number}", True, (255, 255, 255))
            self.window.blit(level_text, level_text.get_rect(center=(self.window.get_width() // 2, 30)))


            for i in range(self.jelly_count):
                x_pos = 20 + (i * 40)
                y_pos = 60
                self.window.blit(self.jelly_img, (x_pos, y_pos))

            # --- drawing tomato lives ---
            for i in range(self.lives):
                x_position = 750 - (i * 50)
                y_position = 20
                self.window.blit(self.tomato_img, (x_position, y_position))

            pygame.display.flip()
            clock.tick(60)