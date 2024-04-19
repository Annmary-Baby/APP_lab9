import pygame
import random
import sys

pygame.init()

WHITE = (255, 255, 255)
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 30

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Jet Plane Bombing Animation")
clock = pygame.time.Clock()

# Load and scale images
jet_image = pygame.image.load('image.png').convert_alpha()
jet_image = pygame.transform.scale(jet_image, (40, 20))  # Resize jet image
house_image = pygame.image.load('image1.png').convert_alpha()
house_image = pygame.transform.scale(house_image, (80, 60))  # Resize house image

class Jet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = jet_image
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH // 2
        self.rect.bottom = WINDOW_HEIGHT - 10
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 255))  # Blue color for the bomb
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = -10  # Upwards movement
        self.exploded = False  # Flag to track collision with house
        self.explosion_radius = 1  # Initial explosion radius
        self.explosion_max_radius = 30  # Maximum explosion radius

    def update(self):
        if not self.exploded:
            self.rect.y += self.speed
            if self.rect.colliderect(image1.rect):  # Check if bomb collides with image1
                self.exploded = True  # Set flag to True
                self.kill_image1()  # Remove image1 from the screen
                self.regenerate_image1()  # Regenerate image1

                # Create explosion effect
                self.explode()

    def kill_image1(self):
        all_sprites.remove(image1)
        image1.kill()

    def regenerate_image1(self):
        # Create and add a new image1 sprite at a random position
        global image1  # Use global variable for image1
        image1 = pygame.sprite.Sprite()
        image1.image = house_image
        image1.rect = image1.image.get_rect()
        image1.rect.topleft = (random.randint(50, WINDOW_WIDTH - 50), random.randint(50, WINDOW_HEIGHT - 200))
        all_sprites.add(image1)

    def explode(self):
        self.image.fill((255, 0, 0))  # Change bomb color to red for explosion
        pygame.draw.circle(screen, WHITE, self.rect.center, self.explosion_radius)
        self.explosion_radius += 1  # Increase explosion radius

        if self.explosion_radius > self.explosion_max_radius:
            self.kill()  # Remove bomb after explosion

all_sprites = pygame.sprite.Group()
jets = pygame.sprite.Group()
bombs = pygame.sprite.Group()
jet = Jet()
all_sprites.add(jet)
jets.add(jet)

# Create initial image1 sprite
image1 = pygame.sprite.Sprite()
image1.image = house_image
image1.rect = image1.image.get_rect()
image1.rect.topleft = (50, 50)  # Initial image1 position
all_sprites.add(image1)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bomb = Bomb(jet.rect.centerx, jet.rect.top)
            all_sprites.add(bomb)
            bombs.add(bomb)

    all_sprites.update()

    screen.fill(WHITE)

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
