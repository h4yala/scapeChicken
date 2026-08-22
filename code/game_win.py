import pygame
import sys
from const import *


class GameWin:
    def __init__(self, window: pygame.Surface, final_score: int):
        self.window = window
        self.final_score = final_score

        self.title_font = pygame.font.Font("../assets/scapeChicken.ttf", 80)
        self.font = pygame.font.Font("../assets/game.ttf", 35)
        self.bg_img = pygame.image.load("../assets/menu_bg.png").convert()
        self.bg_img = pygame.transform.scale(self.bg_img, (self.window.get_width(), self.window.get_height()))

        pygame.mixer.init()
        pygame.mixer.music.load("../assets/you_win.mp3")
        pygame.mixer.music.play()

    def run(self) -> None:
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False

            # background
            self.window.blit(self.bg_img, (0, 0))

            # Textos
            title = self.title_font.render("YOU WIN!", True, C_RED)
            self.window.blit(title, title.get_rect(center=(WIN_WIDTH / 2, 150)))

            score_text = self.font.render(f"Final Score: {self.final_score}", True, C_BLUE)
            self.window.blit(score_text, score_text.get_rect(bottomright=(WIN_WIDTH / 3, 375)))

            instrucao = self.font.render("Aperte ESPAÇO para voltar ao Menu", True, C_WHITE)
            self.window.blit(instrucao, instrucao.get_rect(center=(WIN_WIDTH / 2, 575)))

            pygame.display.flip()
            clock.tick(60)