import pygame
import sys
import random

pygame.init()

# Window configuration
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scape Chicken - HayFarm")
clock = pygame.time.Clock()

# --- 1. LOADING ASSETS ---
# Farmer
farmer_img = pygame.image.load("assets/farmer.png").convert_alpha()
original_size = farmer_img.get_size()
farmer_img = pygame.transform.scale(farmer_img, (original_size[0] * 4, original_size[1] * 4))
farmer_rect = farmer_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Fruit
fruit_img = pygame.image.load("assets/fruit.png").convert_alpha()
fruit_size = fruit_img.get_size()
fruit_img = pygame.transform.scale(fruit_img, (fruit_size[0] * 3, fruit_size[1] * 3))


def spawn_fruit():
    random_x = random.randint(50, WIDTH - 50)
    random_y = random.randint(50, HEIGHT - 50)
    return fruit_img.get_rect(center=(random_x, random_y))


fruit_rect = spawn_fruit()

# Chicken (NEW)
chicken_img = pygame.image.load("assets/chicken.png").convert_alpha()
chicken_size = chicken_img.get_size()
chicken_img = pygame.transform.scale(chicken_img, (chicken_size[0] * 3, chicken_size[1] * 3))
# Spawn the chicken far away from the farmer to be safe at the start
chicken_rect = chicken_img.get_rect(center=(WIDTH - 100, HEIGHT - 100))

# Game Variables
speed = 5
score = 0
lives = 3  # NEW: Player lives
chicken_speed_x = 4  # NEW: Chicken horizontal speed
chicken_speed_y = 4  # NEW: Chicken vertical speed

font = pygame.font.Font(None, 40)
game_over_font = pygame.font.Font(None, 80)  # Larger font for the Game Over screen

# Game State
game_over = False

# Main game loop
running = True
while running:
    # --- 2. EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # --- 3. GAME LOGIC ---

        # Farmer Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: farmer_rect.x -= speed
        if keys[pygame.K_RIGHT]: farmer_rect.x += speed
        if keys[pygame.K_UP]: farmer_rect.y -= speed
        if keys[pygame.K_DOWN]: farmer_rect.y += speed

        # Farmer Screen boundaries
        if farmer_rect.left < 0: farmer_rect.left = 0
        if farmer_rect.right > WIDTH: farmer_rect.right = WIDTH
        if farmer_rect.top < 0: farmer_rect.top = 0
        if farmer_rect.bottom > HEIGHT: farmer_rect.bottom = HEIGHT

        # Chicken Movement (NEW)
        chicken_rect.x += chicken_speed_x
        chicken_rect.y += chicken_speed_y

        # Chicken Bouncing Logic (NEW)
        if chicken_rect.left < 0 or chicken_rect.right > WIDTH:
            chicken_speed_x *= -1  # Reverse horizontal direction
        if chicken_rect.top < 0 or chicken_rect.bottom > HEIGHT:
            chicken_speed_y *= -1  # Reverse vertical direction

        # Fruit Collision Logic
        if farmer_rect.colliderect(fruit_rect):
            score += 1
            fruit_rect = spawn_fruit()

        # Chicken Collision Logic (NEW)
        if farmer_rect.colliderect(chicken_rect):
            lives -= 1
            # Reset positions to avoid losing multiple lives instantly
            farmer_rect.center = (WIDTH // 2, HEIGHT // 2)
            chicken_rect.center = (WIDTH - 100, HEIGHT - 100)

            if lives <= 0:
                game_over = True  # Triggers the Game Over screen

        # --- 4. DRAWING ON THE SCREEN ---
        screen.fill((104, 159, 56))  # Darker green background

        screen.blit(fruit_img, fruit_rect)
        screen.blit(chicken_img, chicken_rect)  # Draw Chicken
        screen.blit(farmer_img, farmer_rect)

        # Draw UI Texts
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))

        lives_text = font.render(f"Lives: {lives}", True, (255, 50, 50))  # Red color
        screen.blit(lives_text, (WIDTH - 120, 20))  # Top-right corner

    else:
        # --- GAME OVER SCREEN ---
        screen.fill((0, 0, 0))  # Black screen

        # Display Game Over text
        go_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
        go_rect = go_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        screen.blit(go_text, go_rect)

        # Display Final Score
        final_score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
        final_score_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
        screen.blit(final_score_text, final_score_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()