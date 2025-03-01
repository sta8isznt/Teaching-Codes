import pygame

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Load explosion image
explosion_img = pygame.image.load("explosion.png")  # Replace with your image
explosion_img = pygame.transform.scale(explosion_img, (100, 100))  # Resize if needed

class Explosion:
    def __init__(self, x, y, duration=500):  # duration in milliseconds
        self.image = explosion_img
        self.x = x
        self.y = y
        self.start_time = pygame.time.get_ticks()  # Get the start time
        self.duration = duration  # Duration of explosion in milliseconds
        self.active = True  # Explosion state

    def update(self):
        # Check if the explosion has lasted long enough
        if pygame.time.get_ticks() - self.start_time > self.duration:
            self.active = False  # Hide the explosion

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, (self.x, self.y))

# List to store active explosions
explosions = []

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Simulate explosion on click
            x, y = event.pos
            explosions.append(Explosion(x - 50, y - 50))  # Center explosion
    
    # Update and draw explosions
    for explosion in explosions:
        explosion.update()
        explosion.draw(screen)

    # Remove expired explosions
    explosions = [e for e in explosions if e.active]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
