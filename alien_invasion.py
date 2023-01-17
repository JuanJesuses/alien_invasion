import sys
import pygame

from settings import Settings
from ship import Ship
from character import Character # Importo la clase Character

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
        self.character = Character(self) # Creo una instancia de Character

    def run_game(self):
        """Inicia el bucle inicial para el juego."""
        while True:
            # Vigila los eventos de ratón y teclado.
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Responde a pulsaciones de teclas y eventos de ratón."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Mueve la nave a la derecha
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    def _update_screen(self):
        """Actualiza las imágenes en la pantalla y cambia a la pantalla nueva."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.character.blitme() # Añado la imagen del personaje

        # Hace visible la pantalla dibujada más recientemente.
        pygame.display.flip()

if __name__ == '__main__':
    # Crea una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()