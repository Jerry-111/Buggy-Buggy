import pygame
import time

class input_handling:
    def __init__(self,bd_id):
        self.left, self.right, self.up, self.attack, self.leave, self.timer = [False] * 6
        self.stop_move_left = False
        self.stop_move_right = False
        self.reset = False
        self.bd_id = bd_id

    def check_event(self):
        # we don't need these two lines
        # self.attack = False
        # self.stop_move_right,self.stop_move_right = [False] * 2

        for event in pygame.event.get():
            self.stop_move_right, self.stop_move_left = [False] * 2
            if event.type == pygame.QUIT:
                self.leave = True
                #pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.leave = True
                if event.key == pygame.K_a:
                    self.left = True
                if event.key == pygame.K_d:
                    self.right = True
                if event.key == pygame.K_w:
                    self.up = True
                if event.key == pygame.K_j:
                    self.attack = True
                if event.key == pygame.K_t:
                    self.timer = True
                if event.key == pygame.K_SPACE:
                    self.reset = True
                if event.key == pygame.K_1 and event.key == pygame.K_TAB:
                    bg_id = 1
                if event.key == pygame.K_5 and event.key == pygame.K_TAB:
                    bg_id = 5
            if event.type == pygame.KEYUP:
                # You don't need this
                # if event.key == pygame.K_ESCAPE:
                #     self.leave = False
                if event.key == pygame.K_a:
                    self.left = False
                    self.stop_move_left = True
                if event.key == pygame.K_d:
                    self.right = False
                    self.stop_move_right = True
                if event.key == pygame.K_w:
                    self.up = False
                if event.key == pygame.K_SPACE:
                    self.reset = False

                    # self.stop_move = True


        return [self.left, self.right, self.up, self.attack, self.leave, self.stop_move_left, self.stop_move_right, self.timer, self.reset, self.bd_id]


    def check_mouse(self, bg_id, blue_screen):
        # we don't need these two lines
        # self.attack = False
        # self.stop_move_right,self.stop_move_right = [False] * 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.leave = True
                #pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('yes button')
                x1, y1 = pygame.mouse.get_pos()
                print(x1, y1)
                if 176 <= x1 * (576 / 1000) <= 385 and 153 <= y1 * (384 / 667) <= 187:  # start
                    print('start')
                    bg_id += 1
                    time_start1 = time.time()
                    return 1, blue_screen, False
                if 49 <= x1 * (576 / 1000) <= 104 and 299 <= y1 * (384 / 667)  <= 324:
                    print('quit')
                    # quit
                    self.leave = True
                    pygame.quit()
                    exit()
                if 176 <= x1 * (576 / 1000) <= 385 and 197 <= y1 * (384 / 667)  <= 230:  # continue
                    print('continue')
                    blue_screen = True
                if 176 <= x1 * (576 / 1000) <= 385 and 240 <= y1 * (384 / 667)  <= 275:  # option
                    print('option')
                    blue_screen = True

        return bg_id, blue_screen, self.leave
