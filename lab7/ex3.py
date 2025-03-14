import pygame

pygame.init()

w, h = 800, 600
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

x, y = w // 2, h // 2

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - 30 > 0:
        x -= 20
    if keys[pygame.K_RIGHT] and x + 30 < w:
        x += 20
    if keys[pygame.K_DOWN] and y + 30 < h:
        y += 20
    if keys[pygame.K_UP] and y - 30 > 0:
        y -= 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    pygame.display.update()