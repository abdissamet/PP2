import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

playlist = [
    "ilhan-insanov-nege-magan-arman.mp3",
    "alisher-qonysbaev-bөleksiң.mp3",
    "kazybek-kuraiysh-ana.mp3"
]

current_track = 0

def play_music():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()
    print(f"Now playing: {playlist[current_track]}")

def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped.")

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()
    print("Next track.")

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()
    print("Previous track.")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_p:
                previous_track()

pygame.quit()