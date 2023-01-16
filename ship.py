import pygame

class Ship:
    """Una clase para gestionar la nave."""

    def __init__(self, ai_game):
        """Inicializa la nave y configura su posición de inicio."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Carga la imagen de la nave y obtiene su rectángulo.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Comieza cada nueva nave en la parte inferior central de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Dibuja la nave en su localización actual."""
        self.screen.blit(self.image, self.rect)
