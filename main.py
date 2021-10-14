import pygame
import include.controller
import include.rooms
import include.renderer
import include.Character
import include.physics
import random
import time
import math
import os

# import utils.pic_compressor

WIDTH = 1000
HEIGHT = int(WIDTH * 2 / 3)
SCALE = 0.7


#
# class example_class:
#
#     def __init__(self):
#         self.move_right = pygame.image.load("./assets/character_file_compressed/move_right.png").convert_alpha()
#         self.move_left = pygame.image.load("./assets/character_file_compressed/move_left.png").convert_alpha()
#         self.stand_right = pygame.image.load("./assets/character_file_compressed/stand_right.png").convert_alpha()
#         self.stand_left = pygame.image.load("./assets/character_file_compressed/stand_left.png").convert_alpha()
#         self.x = 0
#         self.y = 0
#         self.speedx = 5
#         self.speedy = 5


def main():
    pygame.init()
    os.getcwd()
    pygame.mixer.init()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Buggy Buggy")
    # background = pygame.image.load("./assets/backgrounds/background_1.jpg")
    # background = pygame.image.load("./assets/debug_resource/debug_m1.png")
    # background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    running = True
    blue_screen = False
    wasted = False

    c = include.Character.Player(max_hp=random.randint(15, 20), strength=random.randint(5, 7))
    p = include.physics.physics(c)
    # r = include.rooms.Room(1)
    r0, r1, r2, r3, r4, r5, r6, r7, r8, r9 = [include.rooms.Room(i) for i in range(10)]
    rs = {0: r0, 1: r1, 2: r2, 3: r3, 4: r4, 5: r5, 6: r6, 7: r7, 8: r8, 9: r9}
    bg_id = 0
    bg = include.renderer.BackgroundChanger()
    controller = include.controller.input_handling(bg_id)
    start, end = 0, 0.1
    SoundObj = pygame.mixer.music.load("assets/Christopher Larkin - Nightmare King.mp3")
    pygame.mixer.music.play(-1)

    #if 0 < bg_id <= 5:
        #monster_list = [include.Character.Monster(i) for i in include.rooms.Room.Monster_Dic[bg_id].keys()]


    while running:
        r = rs[bg_id]
        background = bg.background(bg_id)

        if blue_screen:
            background = pygame.image.load(f"./assets/backgrounds/blue_screen.png")
            background = pygame.transform.scale(background, (WIDTH, HEIGHT))
            time.sleep(3)
            surface.blit(background, (0, 0))
            pygame.display.flip()
            time.sleep(4)
            running = False
            pygame.quit()
        if wasted:
            background = pygame.image.load(f"./assets/backgrounds/wasted.jpeg")
            background = pygame.transform.scale(background, (WIDTH, HEIGHT))
            left, right, up, attack, leave, stop_move_left, stop_move_right, timer, reset, background_id = controller.check_event()
            if reset:
                wasted = False
            #time.sleep(2)
            #wasted = False

        # monster_list = [include.Character.Monster(i) for i in include.rooms.Room.Monster_Dic[bg_id].keys()]
        if bg_id == 0:
            bg_id, blue_screen, leave = controller.check_mouse(0, False)
            if leave:
                running = False
                pygame.quit()
            surface.blit(background, (0, 0))
            pygame.display.flip()
            end = time.time()
            
            receivedInputX, receivedInputY, attack, leave, timer, reset, background_id = controller.getInput()

            if leave:
                running = False
                pygame.quit()


        elif bg_id == 5 and 6 * 32 * (1000 / 576) <= c.x <= 13 * 32 * (1000 / 576) and c.y >= 9 * 32 * (667 / 384):

            receivedInputX, receivedInputY, attack, leave, timer, reset, background_id = controller.getInput()

            if leave:
                running = False
                pygame.quit()
            bg_id = 6
            surface.blit(background, (0, 0))
            pygame.display.flip()
            time.sleep(0.2)
            bg_id = 7
            surface.blit(background, (0, 0))
            pygame.display.flip()
            time.sleep(0.2)
            bg_id = 8
            time.sleep(0.2)
            surface.blit(background, (0, 0))
            pygame.display.flip()
            time.sleep(0.2)
            bg_id = 9
            surface.blit(background, (0, 0))
            pygame.display.flip()
            #time.sleep(1)
            #running = False
            #bg_id += 1

        elif bg_id > 9:
            running = False
            pygame.quit()
            exit()

        else:
            monster_list = [include.Character.Monster(i) for i in include.rooms.Room.Monster_Dic[bg_id].keys()]
            monster_render_list = {(mons.x/18*WIDTH, mons.y/12*HEIGHT): mons.status_avatar for mons in monster_list}

            last_latency = end - start
            start = time.time()

            receivedInputX, receivedInputY, attack, leave, timer, reset, background_id = controller.getInput()
            
            if reset == True:
                c.x, c.y = 0, HEIGHT - c.h - 53
            if leave:
                running = False
                pygame.quit()
            if c.x == WIDTH and 0 < bg_id < 5:
                bg_id += 1
                c.y = HEIGHT - c.h - 53
                c.x = 0

            c.velocityX, c.velocityY = p.recalculateVelocity(c.velocityX, c.velocityY, receivedInputX, receivedInputY)
            
            collides = []
            for i in monster_list:
                collides.append(math.sqrt((i.x / 18 * WIDTH - c.x) ** 2 + (i.y / 12 * HEIGHT - c.y) ** 2))
            if collides != []:
                if min(collides) < 60:
                    wasted = True
                    p.in_air_time += last_latency
                    c.y + 0.25 * 40 * (p.in_air_time ** 2)
                    bg_id = 1
                    c.y = HEIGHT - c.h - 53
                    c.x = 0

            surface.blit(background, (0, 0))
            if wasted == False:
                c.updateMovement()
                surface = include.renderer.render(surface=surface, n={(c.x, c.y): c.status_avatar})
                surface = include.renderer.render(surface=surface, n=monster_render_list)
            pygame.display.flip()
            end = time.time()

if __name__ == '__main__':
    main()
