import pygame
import random, sys,time,os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 800
HEIGHT = 800
FPS = 30
BACKGROUND = (0, 0, 150)

n = 8
m = 8
matrix = [[0] * m for i in range(n)]

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")
# pygame.display.set_icon(pygame.image.load("b_king_2x_ns.png"))
clock = pygame.time.Clock()

class Figure(pygame.sprite.Sprite):
    xRelat = 0
    yRelat = 0
    xRelatLast = 0
    yRelatLast = 0
    xAbsol = 0
    yAbsol = 0
    Click = False
    Enabled = False
    name = ""
    coordListX = [99 ,99, 99, 99, 99, 99, 99, 99, 99, 99]
    coordListY = [99 ,99, 99, 99, 99, 99, 99, 99, 99, 99]
    global matrix

    def __init__(self, name, x, y):
        self.xRelat = x
        self.yRelat = y
        self.xAbsol = 60*x+179
        self.yAbsol = 60*y+179
        self.name = name
        matrix[self.yRelat][self.xRelat] = 1 
        pygame.sprite.Sprite.__init__(self)
        if (name == "b_king"): figure_img = pygame.image.load(os.path.join(img_folder, 'b_king.png')).convert()
        if (name == "b_queen"): figure_img = pygame.image.load(os.path.join(img_folder, 'b_queen.png')).convert()
        if (name == "b_bishop"): figure_img = pygame.image.load(os.path.join(img_folder, 'b_bishop.png')).convert()
        if (name == "b_knight"): figure_img = pygame.image.load(os.path.join(img_folder, 'b_knight.png')).convert()
        if (name == "b_rook"): figure_img = pygame.image.load(os.path.join(img_folder, 'b_rook.png')).convert()
        if (name == "b_pawn"): figure_img = pygame.image.load(os.path.join(img_folder, 'b_pawn.png')).convert()
        # 
        if (name == "w_king"): figure_img = pygame.image.load(os.path.join(img_folder, 'w_king.png')).convert()
        if (name == "w_queen"): figure_img = pygame.image.load(os.path.join(img_folder, 'w_queen.png')).convert()
        if (name == "w_bishop"): figure_img = pygame.image.load(os.path.join(img_folder, 'w_bishop.png')).convert()
        if (name == "w_knight"): figure_img = pygame.image.load(os.path.join(img_folder, 'w_knight.png')).convert()
        if (name == "w_rook"): figure_img = pygame.image.load(os.path.join(img_folder, 'w_rook.png')).convert()
        if (name == "w_pawn"): figure_img = pygame.image.load(os.path.join(img_folder, 'w_pawn.png')).convert()
        figure_img.convert()
        figure_img = pygame.transform.scale(figure_img, (figure_img.get_width()//15, figure_img.get_height()//15))
        self.image = figure_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.xAbsol, self.yAbsol)

    def setCoordinates(self, x, y):
        self.xRelatLast = self.xRelat
        self.xRelatLast = self.xRelat
        self.xRelat = x
        self.yRelat = y
        self.xAbsol = 60*x+179
        self.yAbsol = 60*y+179
        self.rect.center = (self.xAbsol, self.yAbsol)
        matrix[self.yRelatLast][self.xRelatLast] = 0 
        matrix[self.yRelat][self.xRelat] = 1

    # def click(self):
        # if event.type == pygame.MOUSEMOTION:
        #     x, y = event.pos
        #     if (x > self.xAbsol-30) and (x < self.xAbsol+30) and (y > self.yAbsol-30) and (y < self.yAbsol+30):
        #         self.Click = True
        #     else:
        #         self.Click = False
        # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.Click == True:
        #     self.Enabled = not self.Enabled

        # if self.Enabled == True:
        #     xCount = self.xRelat
        #     yCount = self.yRelat
        #     i = 0
            # if self.name == "b_rook" or self.name == "w_rook":      //Я ЭТО НЕ ДОПИСАЛ !! НЕ ТРОГАЙ !!
        #         while yCount < 7:
        #             yCount = yCount + 1 
        #             self.coordListX[i] = self.xRelat
        #             self.coordListY[i] = yCount
        #             i = i + 1
        #         while xCount < 7:
        #             xCount = xCount + 1 
        #             self.coordListX[i] = xCount
        #             self.coordListY[i] = self.yRelat
        #             i = i + 1
        #     print(self.coordListX)
        #     print(self.coordListY)


                


all_sprites = pygame.sprite.Group()
bRook = Figure("b_rook", 0, 0)
# bPawn = Figure("b_pawn", 0, 1)
# all_sprites.add(bPawn)
all_sprites.add(bRook)

def drawBoard(x, y):
    pygame.draw.rect(screen, (0, 0, 0), (x, y, 480, 480))
    for i in range(0, 4):
        pygame.draw.rect(screen, (255,255,255), (x*i/1.25+210 , y, 60, 60))
        pygame.draw.rect(screen, (255,255,255), (x*i/1.25+150 , y+60, 60, 60))
        pygame.draw.rect(screen, (255,255,255), (x*i/1.25+210 , y+120, 60, 60))
        pygame.draw.rect(screen, (255,255,255), (x*i/1.25+150 , y+180, 60, 60))
        pygame.draw.rect(screen, (255,255,255), (x*i/1.25+210 , y+240, 60, 60))
        pygame.draw.rect(screen, (255,255,255), (x*i/1.25+150 , y+300, 60, 60))
        pygame.draw.rect(screen, (255,255,255), (x*i/1.25+210 , y+360, 60, 60))
        pygame.draw.rect(screen, (255,255,255), (x*i/1.25+150 , y+420, 60, 60))

        pygame.draw.rect(screen, (0, 0, 0), (x*i/1.25+150 , y, 60, 60))
        pygame.draw.rect(screen, (0, 0, 0), (x*i/1.25+210 , y+60, 60, 60))
        pygame.draw.rect(screen, (0, 0, 0), (x*i/1.25+150 , y+120, 60, 60))
        pygame.draw.rect(screen, (0, 0, 0), (x*i/1.25+210 , y+180, 60, 60))
        pygame.draw.rect(screen, (0, 0, 0), (x*i/1.25+150 , y+240, 60, 60))
        pygame.draw.rect(screen, (0, 0, 0), (x*i/1.25+210 , y+300, 60, 60))
        pygame.draw.rect(screen, (0, 0, 0), (x*i/1.25+150 , y+360, 60, 60))
        pygame.draw.rect(screen, (0, 0, 0), (x*i/1.25+210 , y+420, 60, 60))

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        # bRook.click()
        # bPawn.click()
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    
    # Отрисовка
    screen.fill(BACKGROUND)
    drawBoard(WIDTH/2-250, HEIGHT/2-250)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()