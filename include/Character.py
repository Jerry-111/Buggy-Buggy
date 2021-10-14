import pygame
import time
import random
import include.rooms
import random

MONSTER_SPEED = 0.01


# from PIL import Image
# size = Image.open().size


class Player(pygame.sprite.Sprite):
    """the characteristic of character
        speed in x,speed in y,the acceleration of speed in x,the acceleration of speed in y,health point,its strength"""

    def __init__(self, max_hp, strength): 
        self.stand_right = pygame.image.load(
            "./assets/character_file_compressed/stand_right.png").convert_alpha()
        self.stand_left = pygame.image.load(
            "./assets/character_file_compressed/stand_left.png").convert_alpha()
        self.move_left = pygame.image.load(
            "./assets/character_file_compressed/move_left.png").convert_alpha()
        self.move_right = pygame.image.load(
            "./assets/character_file_compressed/move_right.png").convert_alpha()
        self.status_avatar = self.stand_right
        self.rect = self.status_avatar.get_rect()
        self.w, self.h = self.stand_right.get_rect().size
        self.SCREEN_W = 1000
        self.SCREEN_H = int(self.SCREEN_W * 2 / 3)
        self.x = 500
        self.y = 250 
        self.abs_y = self.SCREEN_H - self.y
        self.velocityX = 0
        self.velocityY = 0
        self.hp = max_hp
        self.strength = strength

    def updateMovement(self):
        self.x += self.velocityX;
        self.y += self.velocityY;

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


class Monster(pygame.sprite.Sprite):
    def __init__(self, lc: tuple):
        # The monster would attack the player if their distance is too close or the player has alraedy attack him.

        # Monsters would go towards the player when they are in the same layer. 
        # They also go back and forth in their platform.
        # If the player is shooting at them more than three times, they would go towards the player together.
        # The player won't be allowed to go through the door without shooting all of the monsters.
        x, y = lc
        self.stand_right = pygame.transform.scale(pygame.image.load(
            "./assets/character_file_compressed/Monster_stand_right.png").convert_alpha(), (48, 42))
        self.stand_left = pygame.transform.scale(pygame.image.load(
            "./assets/character_file_compressed/Monster_stand_left.png").convert_alpha(), (48, 42))
        self.move_left = pygame.transform.scale(pygame.image.load(
            "./assets/character_file_compressed/Monster_move_left.png").convert_alpha(), (48, 42))
        self.move_right = pygame.transform.scale(pygame.image.load(
            "./assets/character_file_compressed/Monster_move_right.png").convert_alpha(), (48, 42))
        self.status_avatar = self.stand_right  # the image of Monster

        self.rect = self.stand_left.get_rect()
        self.w, self.h = self.rect.size
        self.x, self.y = x, y
        self.face_right = False
        self.last_move = 0
