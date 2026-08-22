import pygame
import sys


class GameOver:
    def __init__(self, window: pygame.Surface, final_score: int):
        self.window = window
        self.final_score = final_score

        self.font = pygame.font.Font("../assets/game.ttf", 25)
        self.bg_img = pygame.image.load("../assets/game_over.png").convert()
        self.bg_img = pygame.transform.scale(self.bg_img, (self.window.get_width(), self.window.get_height()))

        pygame.mixer.init()
        pygame.mixer.music.load("../assets/game-over.wav")
        pygame.mixer.music.set_volume(1.0)

    def run(self) -> None:
        pygame.mixer.music.play()

        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # play again
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.stop()
                        running = False

            self.window.blit(self.bg_img, (0, 0))

            # final score
            score_text = self.font.render(f"Final Score: {self.final_score}", True, (255, 255, 255))
            score_rect = score_text.get_rect(bottomright=(self.window.get_width() - 30, self.window.get_height() - 30))
            self.window.blit(score_text, score_rect)

            pygame.display.flip()
            clock.tick(60)