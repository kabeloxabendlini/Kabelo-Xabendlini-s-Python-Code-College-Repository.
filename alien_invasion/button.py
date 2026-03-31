import pygame
import pygame.font


class Button:
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 220, 60
        self.button_color = (0, 180, 80)       # ✅ richer green
        self.hover_color = (0, 220, 100)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("consolas", 42, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.msg = msg
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw rounded button with border
        pygame.draw.rect(self.screen, self.button_color, self.rect, border_radius=12)
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect, 2, border_radius=12)
        self.screen.blit(self.msg_image, self.msg_image_rect)