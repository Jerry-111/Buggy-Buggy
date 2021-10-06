import pygame

WIDTH = 1000
HEIGHT = int(WIDTH * 2 / 3)

def render(surface, n: dict):
    for key, value in n.items():
        surface.blit(value, key)

    return surface


class BackgroundChanger:

    def __init__(self):
        self.background_id = 0

    def background(self, id:int = None):
        if id != self.background_id:
            self.background_id = id
        background = pygame.image.load(f"./assets/backgrounds/background_{self.background_id}.jpg")
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        return background
