import sys
import pygame

from settings import Settings

class AlienInvasion:
    """Clase general para gestionar los activos y el comportamiento del juego."""

    def __init__(self):
        """Inicializa y crea los recursos del juego."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_witdh, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Inicia el bucle inicial para el juego."""
        while True:
            # Vigila los eventos de ratón y teclado.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redibuja la pantalla a cada paso por el bucle.
            self.screen.fill(self.settings.bg_color)

            # Hace visible la pantalla dibujada más recientemente.
            pygame.display.flip()

if __name__ == '__main__':
    # Crea una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()