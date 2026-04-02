class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.game_paused = False
        self.high_score = 0

        self.flash_aliens = []
        self.show_level_up = False
        self.level_up_timer = 0
        self.show_lives_lost = False
        self.lives_lost_timer = 0
        self.show_game_over = False
        self.show_quit_confirm = False  # ✅ quit state

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1