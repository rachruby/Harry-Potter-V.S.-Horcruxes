# Harry V.S. Horcruxes 
# Author: Rachel Zhang
# Description: This program is an adventurous game, where the user (roleplaying Harry Potter) has quick access to a menu page to choose to read the instructions and play the game to collect 6 horcruxes.

import pygame, sys, os 
from pygame import *

# Start up pygame
pygame.init()

# Setting up the window where we will draw our shapes and display animations
# The numbers represent the resolution of the screen
WIN = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Harry V.S. Horcruxes')

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
LIGHTBROWN = (199,167,93)
BLUE = (0,0,255)
DARKGREEN = (23,85,16)
LIGHTGRAY = (249,249,249)
# Creating font sizes
font = pygame.font.SysFont("Comic Sans MS",25)
menu_font = pygame.font.SysFont("Comic Sans MS",30)
instructions_font = pygame.font.SysFont("Comic Sans MS", 20)
ESC_font = pygame.font.SysFont("Comic Sans MS", 10)
textbox = pygame.font.SysFont("Comic Sans MS",18)
def drawText(text, font, color, surface, x, y):
    graphics = font.render(text,1,color)
    WIN.blit(graphics,(x,y))

click = False
# Menu Page main loop
def menu_page():
    
    # Background Picture for Menu Page
    loc = os.getcwd()
    img = 'forest.jpg'
    path = loc + "\\" + img
    imgForest = pygame.image.load(path)
    imgX = 0
    imgY = 0
    # Background music
    loc_music = os.getcwd()
    music = 'Harry Potter Theme Song.ogg'
    path_music = loc_music + "\\" + music
    theme = pygame.mixer.music.load('Harry Potter Theme Song.ogg')
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(loops = -1)
    
    while True:
        WIN.fill(BLACK)
        
        WIN.blit(imgForest,(imgX,imgY)) 
        
        drawText("Harry V.S. Horcruxes",menu_font, WHITE, WIN, 250, 100)
        # Get the mouse cursor position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Create Buttons on menu 
        button_instructions = pygame.Rect(200,270,400,50)
        button_game = pygame.Rect(200,350,400,50)
        # Create collide point to test if a point is in the button
        if button_instructions.collidepoint(mouse_x,mouse_y):
            if click:
                instructions()
        if button_game.collidepoint(mouse_x,mouse_y):
            if click:
                game()
        # Create buttons and text
        pygame.draw.rect(WIN,RED,button_instructions)
        drawText("Instructions", font, (WHITE),WIN,335,270)
        pygame.draw.rect(WIN,RED,button_game)
        drawText("Play Game", font, (WHITE), WIN, 345,350)        

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

# Instructions Page loop
def instructions():
    run = True
    # Hermione Picture for Instruction Page
    loc_instr = os.getcwd()
    img_hermione = 'hermione.png'
    path_instr = loc_instr + "\\" + img_hermione
    imgHermione = pygame.image.load(path_instr)
    hermioneX = 595
    hermioneY = 340

    while run:
        WIN.fill(LIGHTGRAY)

        drawText("Press ESC to exit to menu", ESC_font, (BLACK),WIN,20,10)
        drawText("Hermione's Telepathic Message:", font, (BLACK),WIN,20,20)
        # Instructions
        drawText("Harry! Wake Up! We have been teleported to the Forbidden Forest!", instructions_font, (BLACK),WIN,70,100)
        drawText("Bad News!", instructions_font, (BLACK),WIN,70,130)
        drawText("I lost our 6 Horcruxes, and I am injured!", instructions_font, (BLACK),WIN,70,160)
        drawText("Harry, FIND the 6 Horcruxes (mysterious red dots) in the forest.", instructions_font, (BLACK),WIN,70,190)
        drawText("Note, the trees are magical, you need to watch out for the trees", instructions_font, (BLACK),WIN,70,220)
        drawText("(there may be some horcruxes hidden in the trees!).", instructions_font, (BLACK),WIN,70,250)
        drawText("Harry, after finding the horcruxes, ", instructions_font, (BLACK),WIN,70,280)
        drawText("find a way to GET OUT OF THIS FOREST!", instructions_font, (BLACK),WIN,70,310)
        pygame.draw.rect(WIN,LIGHTBROWN,(60,80,700,320),4)
        pygame.draw.circle(WIN,LIGHTBROWN,(570,450),15,5)
        pygame.draw.circle(WIN,LIGHTBROWN,(530,430),15,5)        
        WIN.blit(imgHermione,(hermioneX,hermioneY))

        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        pygame.display.update()

# Game Page loop                     
def game():
    run = True
    # Tent Coordinates 
    tentX1 = 40
    tentY1 = 100
    
    tentX2 = 60
    tentY2 = 50
    
    tentX3 = 80
    tentY3 = 100
    # User's properties
    harryX = 40
    harryY = 325 
    harry_radius = 12
    speedX = 2
    speedY = 2
    # Tree Picture for Instruction Page
    loc_tree = os.getcwd()
    img_tree = 'rsz_tree.png'
    path_tree = loc_tree + "\\" + img_tree
    imgTree = pygame.image.load(path_tree)
    treeX = 125
    treeY = 0
    # Hogwarts (end point) (w=50,h=40) 
    loc_castle = os.getcwd()
    img_castle = 'rsz_castle.png'
    path_castle = loc_castle + "\\" + img_castle
    img_castle = pygame.image.load(path_castle)
    castleX = 720
    castleY = 50
    # Sound Effects
    loc_cheer = os.getcwd()
    sound_cheer = 'cheer.wav'
    path_cheer = loc_cheer + "\\" + sound_cheer
    cheer = pygame.mixer.Sound("cheer.wav")
    cheer.set_volume(0.7)
    
    loc_bonus = os.getcwd()
    sound_bonus = 'bonus.wav'
    path_bonus = loc_bonus + "\\" + sound_bonus
    bonus = pygame.mixer.Sound('bonus.wav')
    bonus.set_volume(0.8)
    # Scoring System 
    countX= 230
    countY = 20
    
    
    while run:
        WIN.fill(LIGHTBROWN)
        pygame.time.delay(10)
        # Tent (Starting Point) 
        pygame.draw.polygon(WIN,BLACK,((tentX1,tentY1),(tentX2,tentY2 ),(tentX3,tentY3 )))
        # Boundaries Coordinates(Forest Walls)
        wall_1 = pygame.Rect(125,0,100,450)    
        wall_2 = pygame.Rect(335,200,100,400)
        wall_3 = pygame.Rect(480,0,235,450)
        
        # Boundaries Drawings
        WIN.blit(imgTree,(treeX,treeY))        
        WIN.blit(imgTree,(335,200))
        WIN.blit(imgTree,(480,0))
        WIN.blit(imgTree,(580,0))

        # Horcruxes
        hor1 = pygame.draw.circle(WIN,RED,(100,400),10)
        hor2 = pygame.draw.circle(WIN,RED,(350,500),15)
        hor3 = pygame.draw.circle(WIN,RED,(400,100),10)
        hor4 = pygame.draw.circle(WIN,RED,(200,580),15)
        hor5 = pygame.draw.circle(WIN,RED,(585,320),10)
        hor6 = pygame.draw.circle(WIN,RED,(740,550),20)
        # Castle Drawings
        WIN.blit(img_castle,(castleX,castleY))

        # ESC instruction
        drawText("Press ESC to exit to menu", ESC_font,BLACK, WIN, 0,0 )
        
        # User (Harry Potter, Blue dot) 
        harry = pygame.draw.circle(WIN,BLUE,(harryX,harryY),harry_radius)
        
        

        # User moving keys      
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
 
        
        pygame.display.update()


        if 85<harryX<110 and 385< harryY < 410:
            hor1 = pygame.draw.circle(WIN,LIGHTGRAY,(100,400),10)
            countText = drawText("Horcrux number +1, Locket!",textbox, BLACK, WIN, countX, countY)
            pygame.display.update()
            bonus.play()
        if 335<harryX<360 and 485<harryY<500:
            hor2 = pygame.draw.circle(WIN,LIGHTGRAY,(350,500),15)
            countText = drawText("Horcrux number +1, Nagini!",textbox, BLACK, WIN, countX, countY)
            pygame.display.update()
            bonus.play()
        if 375<harryX<410 and 85<harryY<110:
            hor3 = pygame.draw.circle(WIN,LIGHTGRAY,(400,100),10)
            countText = drawText("Horcrux number +1, Diary!",textbox, BLACK, WIN, countX, countY)
            pygame.display.update()
            bonus.play()
        if 175<harryX<210 and 555<harryY<600:
            hor4 = pygame.draw.circle(WIN,LIGHTGRAY,(200,580),15)
            countText = drawText("Horcrux number +1, Diadem!",textbox, BLACK, WIN, countX, countY)
            pygame.display.update()
            bonus.play()
        if 560<harryX<595 and 295<harryY<330:
            hor5 = pygame.draw.circle(WIN,LIGHTGRAY,(585,320),10)
            countText = drawText("Horcrux number +1, Cup!",textbox, BLACK, WIN, countX, countY)
            pygame.display.update()
            bonus.play()
        if 715<harryX<750 and 515<harryY<570:
            hor6 = pygame.draw.circle(WIN,LIGHTGRAY,(740,550),20)
            countText = drawText("Horcrux number +1, Ring!",instructions_font, BLACK, WIN, countX, countY)
            pygame.display.update()
            bonus.play()
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if harryX > harry_radius:
                if harryX <125 or harryY > 450: 
                    harryX = harryX - speedX
                if harryX > 237:
                    harryX = harryX - speedX
                if 720<harryX<750 and harryY<90:
                    cheer.play()
                    break
                
        if keys[pygame.K_RIGHT]:
            if harryX + harry_radius < 800:
                if harryX < 113 or harryY >450 or harryX>213:
                    harryX = harryX + speedX
                if 720<harryX<750 and harryY< 90:
                    cheer.play()
                    break

        if keys[pygame.K_UP]:
            if harryY > harry_radius:
                if harryY > 462 or harryX < 125 or harryX >225:
                    harryY = harryY - speedY
                if 720<harryX<750 and harryY < 90:
                    cheer.play()
                    break

        if keys[pygame.K_DOWN]:
            if harryY + harry_radius < 600: 
                harryY = harryY + speedY
            if 720<harryX<750 and harryY < 90:
                cheer.play()
                break

        pygame.display.update()
        
menu_page()
    


















