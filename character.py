import pygame

class Character:
    """Clase para gestionar el personaje."""

    def __init__(self, ai_game):
        """Inicializa el personaje y establece su posición de inicio."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Carga la imagen del personaje y obtiene su rectángulo.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Comienza una nueva imagen en el centro de la pantalla.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Dibuja el personaje en su localización actual."""
        self.screen.blit(self.image, self.rect)
