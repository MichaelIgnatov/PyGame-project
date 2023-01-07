import pygame


class Button():
    def __init__(self, image, pos, level=''):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.level = level
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.sound_button = pygame.mixer.Sound("data/sounds/pressing the button.ogg")

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) \
                and position[1] in range(self.rect.top, self.rect.bottom):
            self.sound_button.play()
            if self.level != '':
                return self.level
            else:
                return True
        return False