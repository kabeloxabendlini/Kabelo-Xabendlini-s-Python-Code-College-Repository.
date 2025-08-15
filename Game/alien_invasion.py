import sys
import pygame
from settings import Settings


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        # Load settings
        self.settings = Settings()

        # Set up the display
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

            # Limit the frame rate to 60 FPS
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
    
def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()
    self.clock = pygame.time.Clock()
    
def run_game(self):
    """Start the main loop for the game."""
    while True:
        # --snip-- (event handling, updates, etc.)

        # Update the display
        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        self.clock.tick(60)
        
def __init__(self):
    # --snip--
    pygame.display.set_caption("Alien Invasion")
    
    # Set the background color
    self.bg_color = (230, 230, 230)

def run_game(self):
    # --snip--
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Redraw the screen during each pass through the loop
    self.screen.fill(self.bg_color)

    # Make the most recently drawn screen visible
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    self.clock.tick(60)