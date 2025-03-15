import pygame

pygame.init()

# Терезенің параметрлері
WINDOW_WIDTH, WINDOW_HEIGHT = 700, 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Доп")

# Шардың бастапқы орны мен түсі
ball_position = [50, 50]
ball_radius = 25
colors = [(255, 0, 0), (0, 0, 255)]
color_index = 0

# Қозғалыс жылдамдығы
speed = 20

# Ойын циклін басқару
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            color_index = 1 - color_index  # Түсті ауыстыру индекс 0 мен 1 арасында 
    
    # Басылған пернелерді тексеру
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_position[1] = max(ball_position[1] - speed, ball_radius)
    if keys[pygame.K_DOWN]:
        ball_position[1] = min(ball_position[1] + speed, WINDOW_HEIGHT - ball_radius)
    if keys[pygame.K_LEFT]:
        ball_position[0] = max(ball_position[0] - speed, ball_radius)
    if keys[pygame.K_RIGHT]:
        ball_position[0] = min(ball_position[0] + speed, WINDOW_WIDTH - ball_radius)

    # Терезені жаңарту
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, colors[color_index], ball_position, ball_radius)
    pygame.display.flip()
    
    # Кадр жиілігін басқару
    clock.tick(60)

pygame.quit()