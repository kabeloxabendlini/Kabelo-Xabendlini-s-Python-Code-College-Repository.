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

        self.text_color = (0, 255, 255)        # ✅ cyan text
        self.label_color = (150, 150, 200)     # ✅ soft purple labels
        self.font = pygame.font.SysFont("consolas", 36, bold=True)
        self.label_font = pygame.font.SysFont("consolas", 20)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def prep_level(self):
        level_str = "LVL  " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 8

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * (ship.rect.width + 5)
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        # Draw HUD background bar
        hud_rect = pygame.Rect(0, 0, self.screen_rect.width, 70)
        hud_surface = pygame.Surface((hud_rect.width, hud_rect.height), pygame.SRCALPHA)
        hud_surface.fill((0, 0, 60, 160))
        self.screen.blit(hud_surface, hud_rect)

        # Labels
        score_label = self.label_font.render("SCORE", True, self.label_color)
        self.screen.blit(score_label, (self.score_rect.right - score_label.get_width(), 6))

        high_label = self.label_font.render("BEST", True, self.label_color)
        self.screen.blit(high_label, (self.high_score_rect.centerx - high_label.get_width() // 2, 6))

        # Values
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)