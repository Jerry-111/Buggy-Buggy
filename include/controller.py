import pygame
import time

class input_handling:
    def __init__(self,bd_id):
        self.attack, self.leave, self.timer = [False] * 3
        self.reset = False
        self.bd_id = bd_id
        self.leftPressed = False
        self.rightPressed = False
        self.downPressed = False
        self.upPressed = False

    def getInput(self):
        xInput, yInput = 0, 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.leave = True
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.leave = True
                
                if event.key == pygame.K_a:
                    self.leftPressed = True
                if event.key == pygame.K_d:
                    self.rightPressed = True
                if event.key == pygame.K_s:
                    self.downPressed = True
                if event.key == pygame.K_w:
                    self.upPressed = True

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
                if event.key == pygame.K_SPACE:
                    self.reset = False
                if event.key == pygame.K_a:
                    self.leftPressed = False
                if event.key == pygame.K_d:
                    self.rightPressed = False
                if event.key == pygame.K_s:
                    self.downPressed = False
                if event.key == pygame.K_w:
                    self.upPressed = False
 

        if self.leftPressed and self.rightPressed:
            xInput = 0
        if self.leftPressed and not self.rightPressed:
            xInput = -1
        if self.rightPressed and not self.leftPressed:
            xInput = 1
        if not self.leftPressed and not self.rightPressed:
            xInput = 0

        if self.upPressed and self.downPressed:
            yInput = 0
        if self.upPressed and not self.downPressed:
            yInput = 1
        if self.downPressed and not self.upPressed:
            yInput = -1
        if not self.upPressed and not self.downPressed:
            yInput = 0 

        return [xInput, yInput, self.attack, self.leave, self.timer, self.reset, self.bd_id]

    def check_mouse(self, bg_id, blue_screen):
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
