import pygame, sys, random, time
from pygame.locals import *

# -------------------- INITIAL SETUP --------------------
pygame.init()

# FPS & Clock
FPS = 60
clock = pygame.time.Clock()

# Screen
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Racer – Lab 9")

# -------------------- COLORS --------------------
BLUE   = (0, 0, 255)
RED    = (255, 0, 0)
GREEN  = (0, 255, 0)
BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)
GOLD   = (255, 215, 0)

# -------------------- VARIABLES --------------------
SPEED = 5
SCORE = 0
COINS = 0

# fonts
font_large = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font_large.render("Game Over", True, BLACK)

# background image
background = pygame.image.load("/Users/hatefchalak/Desktop/Lab 08/AnimatedStreet.png")

# -------------------- SPRITE CLASSES --------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/hatefchalak/Desktop/Lab 08/Enemy.png")
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), 0))
        self.speed = SPEED  # Enemy speed can increase during game

    def move(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/hatefchalak/Desktop/Lab 08/Player.png")
        self.rect = self.image.get_rect(center=(160, 520))
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.choice([1,2,3,5])  # Random weight for Lab 9
        self.image = pygame.image.load("/Users/hatefchalak/Desktop/Lab 08/pngtree-glossy-golden-coin-icon-png-image_2898883.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (28, 28))
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), random.randint(0, 100)))

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# -------------------- CREATE SPRITES --------------------
player = Player()
enemy = Enemy()

enemies = pygame.sprite.Group(enemy)
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group(player, enemy)

# Custom events
SPAWN_COIN = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_COIN, 1300)

# -------------------- GAME LOOP --------------------
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SPAWN_COIN:
            coin = Coin()
            coins.add(coin)
            all_sprites.add(coin)

    # -------------------- DRAW BACKGROUND --------------------
    screen.blit(background, (0, 0))

    # -------------------- DRAW HUD --------------------
    score_display = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_display = font_small.render(f"Coins: {COINS}", True, GOLD)
    screen.blit(score_display, (10, 10))
    screen.blit(coins_display, (SCREEN_WIDTH - 110, 10))

    # -------------------- UPDATE SPRITES --------------------
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # -------------------- COLLISIONS --------------------
    coin_hits = pygame.sprite.spritecollide(player, coins, dokill=True)
    if coin_hits:
        for c in coin_hits:
            COINS += c.weight  # collect weighted coins
            # increase enemy speed for every N coins
            if COINS % 10 == 0:
                enemy.speed += 1

    if pygame.sprite.spritecollideany(player, enemies):
        pygame.mixer.Sound("/Users/hatefchalak/Desktop/Lab 08/crash.wav").play()
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over_text, (50, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(FPS)