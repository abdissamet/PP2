import pygame
import datetime
pygame.init()
w = 600
h = 500
angle1 = 0
angle2 = 0

screen=pygame.display.set_mode((w,h),pygame.RESIZABLE)

pygame.display.set_caption("simple clock")
pygame.display.set_icon(pygame.image.load(r"lab7/imagess/mickeyclock.bmp"))

white=(255,255,255)
screen.fill(white)

mickey=pygame.image.load(r"lab7/imagess/main-clock.png")
leftHand=pygame.image.load(r"lab7/imagess/left-hand.png")
rightHand=pygame.image.load(r"lab7/imagess/right-hand.png")

mickey = pygame.transform.scale( mickey ,(414 , 418))
clock = pygame.time.Clock()
x=0
while True:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            exit()
    t = datetime.datetime.now()
    angle1 = -t.second * 6
    angle2 = -t.minute * 6
    
    leftHand1 = pygame.transform.rotate(leftHand,x)
    rightHand1 = pygame.transform.rotate(rightHand,angle2)
    
    rightHand1=pygame.transform.scale(rightHand1,(rightHand1.get_width()//2 ,rightHand1.get_height()//2))
    leftHand1=pygame.transform.scale(leftHand1,(leftHand1.get_width()//2 , leftHand1.get_height()//2))
    
    mickeyrect = mickey.get_rect(center = (w//2,h//2))
    leftHandRect = leftHand1.get_rect(center = (w//2,h//2))
    rightHandRect = rightHand1.get_rect(center = (w//2,h//2))
    
    screen.blit(mickey,mickeyrect)
    screen.blit(leftHand1,leftHandRect)
    screen.blit(rightHand1,rightHandRect) 
    x-=0.6
    pygame.display.update()

    clock.tick(10)

run()