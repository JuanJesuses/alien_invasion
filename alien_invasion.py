import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Clase general para gestionar los activos y el comportamiento del juego."""

    def __init__(self):
        """Inicializa y crea los recursos del juego."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_witdh, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Inicia el bucle inicial para el juego."""
        while True:
            # Vigila los eventos de ratón y teclado.
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Responde a pulsaciones de teclas y eventos de ratón."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Actualiza las imágenes en la pantalla y cambia a la pantalla nueva."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Hace visible la pantalla dibujada más recientemente.
        pygame.display.flip()

if __name__ == '__main__':
    # Crea una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()