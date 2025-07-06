import pygame

# Initialize
pygame.init()
WIDTH, HEIGHT = 800, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Aliens")
clock = pygame.time.Clock()

# Sizes
player_size = 80
enemy_size = 80

# Fonts
font = pygame.font.SysFont("arial", 28)
big_font = pygame.font.SysFont("arial", 60)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Music
pygame.mixer.init()
pygame.mixer.music.load("assets/background.wav")
click_sound = pygame.mixer.Sound("assets/click.mp3")
collision_sound = pygame.mixer.Sound("assets/collision.wav")
click_sound.set_volume(0.5)
collision_sound.set_volume(0.6)
music_on = True
