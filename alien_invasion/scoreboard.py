import pygame
import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (0, 255, 255)
        self.label_color = (100, 180, 255)
        self.divider_color = (0, 100, 160)
        self.font = pygame.font.SysFont("consolas", 34, bold=True)
        self.label_font = pygame.font.SysFont("consolas", 14)
        self.ship_icon_font = pygame.font.SysFont("consolas", 22, bold=True)
        self.hud_height = 80

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 30
        self.score_rect.top = 38

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 38

    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.top = 38

    def prep_ships(self):
        """Store ship count — drawn directly in show_score."""
        self.ships = Group()  # kept for compatibility but not drawn below HUD

    def show_score(self):
        w = self.screen_rect.width

        # Gradient HUD background
        hud_surf = pygame.Surface((w, self.hud_height), pygame.SRCALPHA)
        for i in range(self.hud_height):
            alpha = int(220 - (i / self.hud_height) * 180)
            pygame.draw.line(hud_surf, (0, 0, 40, alpha), (0, i), (w, i))
        self.screen.blit(hud_surf, (0, 0))

        # Bottom border glow
        pygame.draw.line(self.screen, (0, 180, 255),
                         (0, self.hud_height - 2), (w, self.hud_height - 2), 1)
        pygame.draw.line(self.screen, (0, 80, 120),
                         (0, self.hud_height - 1), (w, self.hud_height - 1), 1)

        # ✅ 4 equal sections
        quarter = w // 4
        for x in (quarter, quarter * 2, quarter * 3):
            pygame.draw.line(self.screen, self.divider_color,
                             (x, 10), (x, self.hud_height - 10), 1)

        # ✅ Section center x positions
        level_cx   = quarter // 2
        best_cx    = quarter + quarter // 2
        score_cx   = quarter * 2 + quarter // 2
        ships_cx   = quarter * 3 + quarter // 2

        # Section labels
        label_y = 8
        sections = [
            ("LEVEL", level_cx),
            ("BEST",  best_cx),
            ("SCORE", score_cx),
            ("LIVES", ships_cx),  # ✅ new ships section
        ]
        for label, cx in sections:
            lbl = self.label_font.render(label, True, self.label_color)
            lbl_rect = lbl.get_rect(centerx=cx, top=label_y)
            underline_y = lbl_rect.bottom + 2
            pygame.draw.line(self.screen, self.divider_color,
                             (lbl_rect.left, underline_y),
                             (lbl_rect.right, underline_y), 1)
            self.screen.blit(lbl, lbl_rect)

        # Update positions to center in their sections
        self.level_rect.centerx = level_cx
        self.high_score_rect.centerx = best_cx
        self.score_rect.centerx = score_cx

        # Draw values
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.score_image, self.score_rect)

        # ✅ Draw ship icons in LIVES section
        ship_icon = self.ship_icon_font.render("▲", True, (0, 255, 255))
        icon_w = ship_icon.get_width() + 4
        total_w = icon_w * self.stats.ships_left
        start_x = ships_cx - total_w // 2
        icon_y = 36

        for i in range(self.stats.ships_left):
            self.screen.blit(ship_icon, (start_x + i * icon_w, icon_y))

        # ✅ If no lives left show GAME OVER in red
        if self.stats.ships_left == 0:
            over = self.label_font.render("GAME OVER", True, (255, 60, 60))
            self.screen.blit(over, over.get_rect(centerx=ships_cx, top=38))