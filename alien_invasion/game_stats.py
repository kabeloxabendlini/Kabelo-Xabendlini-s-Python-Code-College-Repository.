class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.game_paused = False
        self.high_score = 0

        # ✅ Visual effect states
        self.flash_aliens = []       # list of (alien_rect, timer)
        self.show_level_up = False   # level up banner flag
        self.level_up_timer = 0      # how long to show banner
        self.show_lives_lost = False # lives lost animation flag
        self.lives_lost_timer = 0    # how long to show animation
        self.show_game_over = False  # game over screen flag

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1