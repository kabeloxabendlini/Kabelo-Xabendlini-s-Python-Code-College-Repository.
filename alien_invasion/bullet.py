import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height
        )
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top

        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw a glowing cyan bullet."""
        # Outer glow
        glow_rect = self.rect.inflate(4, 4)
        pygame.draw.rect(self.screen, (0, 100, 100), glow_rect, border_radius=3)
        # Inner bright core
        pygame.draw.rect(self.screen, self.color, self.rect, border_radius=2)