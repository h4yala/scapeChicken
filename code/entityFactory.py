#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from player import Player
from enemy import Enemy
from background import Background



class EntityFactory:
    @staticmethod
    def get_entity(entity_type: str, window: pygame.Surface) -> 'Entity':

        if entity_type == "Player":
            surf = pygame.image.load("../assets/farmer.png").convert_alpha()
            original_size = surf.get_size()
            surf = pygame.transform.scale(surf, (original_size[0] * 4, original_size[1] * 4))
            rect = surf.get_rect(center=(window.get_width() // 2, window.get_height() // 2))
            return Player(surf, rect)

        elif entity_type == "Enemy":
            surf = pygame.image.load("../assets/chicken.png").convert_alpha()
            chicken_size = surf.get_size()
            surf = pygame.transform.scale(surf, (chicken_size[0] * 3, chicken_size[1] * 3))
            # Spawn at the bottom right corner
            rect = surf.get_rect(center=(window.get_width() - 100, window.get_height() - 100))
            return Enemy(surf, rect)

        elif entity_type == "Background":
            surf = pygame.image.load("../assets/cenario.png").convert()
            surf = pygame.transform.scale(surf, (window.get_width(), window.get_height()))
            rect = surf.get_rect(topleft=(0, 0))
            return Background(surf, rect)


        return None