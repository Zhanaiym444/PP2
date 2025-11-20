import pygame
import time
import random

# -------------------- INITIAL SETUP --------------------
snake_speed = 10
timer = 0  # Timer for special food

window_x = 1000
window_y = 500

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
orange = (255, 140, 0)  # special food color

pygame.init()
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Snake – Lab 9')
fps = pygame.time.Clock()

# -------------------- SNAKE SETUP --------------------
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# -------------------- FOOD SETUP --------------------
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# direction control
direction = 'RIGHT'
change_to = direction

# score and level
score = 0
level = 1
food = 0

# Two types of food: 0 = regular, 1 = special
fruit_type = 0
fruit_value = [1, 3]   # growth value
score_value = [10, 30] # score value

# -------------------- FUNCTIONS --------------------
def show_score_and_level(choice, color, font, size):
    """Display current score and level on screen"""
    score_font = pygame.font.SysFont(font, size)
    level_font = pygame.font.SysFont(font, size)

    score_surface = score_font.render(f'Score : {score}', True, color)
    level_surface = level_font.render(f'Level : {level}', True, color)
    score_rect = score_surface.get_rect()
    level_rect = level_surface.get_rect(topright=(995,0))

    game_window.blit(score_surface, score_rect)
    game_window.blit(level_surface, level_rect)

def game_over():
    """Display game over screen and quit"""
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        f'Your Score is : {score}    Your level is : {level}', True, red)
    game_over_rect = game_over_surface.get_rect(center=(window_x/2, window_y/4))
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()

# -------------------- MAIN LOOP --------------------
while True:
    # Avoid placing fruit inside border
    if 475 <= fruit_position[0] <= 525 and fruit_position[1] >= 200:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]

    # -------------------- HANDLE KEYS --------------------
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: change_to = 'UP'
            if event.key == pygame.K_DOWN: change_to = 'DOWN'
            if event.key == pygame.K_LEFT: change_to = 'LEFT'
            if event.key == pygame.K_RIGHT: change_to = 'RIGHT'

    # Prevent snake reversing
    if change_to == 'UP' and direction != 'DOWN': direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP': direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT': direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT': direction = 'RIGHT'

    # -------------------- MOVE SNAKE --------------------
    if direction == 'UP': snake_position[1] -= 10
    if direction == 'DOWN': snake_position[1] += 10
    if direction == 'LEFT': snake_position[0] -= 10
    if direction == 'RIGHT': snake_position[0] += 10

    # Check border collision (rect)
    c = pygame.Surface((1,1))
    d = c.get_rect(center=(snake_position[0], snake_position[1]))
    border = pygame.Surface((50,300))
    border.fill((120,0,0))
    b = border.get_rect(midbottom=(500,500))
    if b.colliderect(d):
        game_over()

    # -------------------- SNAKE BODY & FOOD --------------------
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += score_value[fruit_type]
        food += fruit_value[fruit_type]
        fruit_spawn = False
    else:
        snake_body.pop()

    # Level up every 3 growth points
    if food >= 3:
        snake_speed += 10
        food -= 3
        level += 1

    # -------------------- SPAWN NEW FOOD --------------------
    if not fruit_spawn:
        fruit_type = random.randrange(0,2)
        if fruit_type: timer=0  # reset timer for special food
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
    fruit_spawn = True

    # -------------------- DRAWING --------------------
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    if fruit_type == 0:
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    else:
        pygame.draw.rect(game_window, orange, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10: game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10: game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]: game_over()

    # Display score and level
    show_score_and_level(1, blue, 'times new roman', 35)

    game_window.blit(border,b)

    # -------------------- SPECIAL FOOD TIMER --------------------
    timer += 1
    if timer >= 10*snake_speed and fruit_type:
        timer = 0
        fruit_type = 0
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]

    pygame.display.update()
    fps.tick(snake_speed)