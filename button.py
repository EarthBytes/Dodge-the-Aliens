import pygame
from settings import font, GRAY, click_sound, WHITE

class Button:
    def __init__(self, text, x, y, w, h, action):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.action = action

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        color = (180, 180, 180) if self.rect.collidepoint(mouse_pos) else GRAY
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        label = font.render(self.text, True, WHITE)
        surface.blit(label, (
            self.rect.x + (self.rect.width - label.get_width()) // 2,
            self.rect.y + (self.rect.height - label.get_height()) // 2
        ))

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            click_sound.play()
            self.action()
