import pygame
import pygame.font
import math


class Button:
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.width, self.height = 260, 70
        self.button_color = (0, 20, 60)        # ✅ dark navy base
        self.border_color = (0, 255, 255)      # ✅ cyan border
        self.text_color = (0, 255, 255)        # ✅ cyan text
        self.hover_color = (0, 255, 200)       # ✅ bright teal on hover
        self.font = pygame.font.SysFont("consolas", 44, bold=True)
        self.label_font = pygame.font.SysFont("consolas", 16)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.msg = msg
        self.pulse = 0  # ✅ for glow animation
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def draw_button(self):
        # ✅ Pulse glow animation
        self.pulse = (self.pulse + 0.05) % (2 * math.pi)
        glow_alpha = int(80 + 60 * math.sin(self.pulse))
        border_color = self.hover_color if self.is_hovered() else self.border_color

        # ✅ Outer glow
        glow_rect = self.rect.inflate(16, 16)
        glow_surf = pygame.Surface((glow_rect.width, glow_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(glow_surf, (*border_color, glow_alpha),
                         glow_surf.get_rect(), border_radius=20)
        self.screen.blit(glow_surf, glow_rect)

        # ✅ Button background
        pygame.draw.rect(self.screen, self.button_color, self.rect, border_radius=14)

        # ✅ Shine effect at top
        shine_rect = pygame.Rect(self.rect.x + 8, self.rect.y + 6,
                                 self.rect.width - 16, self.rect.height // 3)
        shine_surf = pygame.Surface((shine_rect.width, shine_rect.height), pygame.SRCALPHA)
        shine_surf.fill((255, 255, 255, 20))
        pygame.draw.rect(shine_surf, (255, 255, 255, 20),
                         shine_surf.get_rect(), border_radius=8)
        self.screen.blit(shine_surf, shine_rect)

        # ✅ Border
        pygame.draw.rect(self.screen, border_color, self.rect, 2, border_radius=14)

        # ✅ Corner accents
        accent_size = 8
        corners = [
            (self.rect.left, self.rect.top),
            (self.rect.right - accent_size, self.rect.top),
            (self.rect.left, self.rect.bottom - accent_size),
            (self.rect.right - accent_size, self.rect.bottom - accent_size),
        ]
        for cx, cy in corners:
            pygame.draw.rect(self.screen, border_color,
                             (cx, cy, accent_size, accent_size), 2)

        # ✅ Button text
        self.msg_image = self.font.render(self.msg, True, border_color)
        self.msg_image_rect = self.msg_image.get_rect(center=self.rect.center)
        self.screen.blit(self.msg_image, self.msg_image_rect)

        # ✅ Hint text below button
        hint = self.label_font.render("[ CLICK TO START ]", True, (0, 120, 140))
        hint_rect = hint.get_rect(centerx=self.rect.centerx,
                                   top=self.rect.bottom + 10)
        self.screen.blit(hint, hint_rect)