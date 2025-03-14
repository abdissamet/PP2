import pygame
from pygame import mixer

mixer.init()
screen=pygame.display.set_mode((800, 600))

player=pygame.image.load(r"lab7/music/musicplayer.jpg")
mic = pygame.transform.scale( player ,(800 , 600))
music=mixer.music.load(r"lab7/music/musicc.mp3")
pause= False

while True:
    screen.blit(mic,(0,0))
    pygame.display.update()
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                pygame.mixer.music.play(-1)     
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                pause=not pause
                if pause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()