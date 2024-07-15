import pygame
import time
import random
from monster import Monster

# Function to get a valid game duration from the user
def get_game_duration():
    while True:
        try:
            game_duration = int(input("How many seconds do you want the game to last? "))
            if game_duration > 0 and game_duration < 10000:
                return game_duration
            else:
                print("Please enter a number less than 10,000.")
        except ValueError:
            print("Please enter a valid number.")

# Get the game duration from the user
game_duration = get_game_duration()

print("Your score is based on the number of hits minus shots taken, so make sure to be accurate! ")

pygame.init()
pygame.display.set_caption("Dragon Popper")
screen = pygame.display.set_mode((800, 800))

WHITE = [255, 255, 255]
GREEN = [0, 255, 0]

FPS = 30
fpsClock = pygame.time.Clock()

quitVar = False
myMonsters = []

font = pygame.font.Font('PlayfairDisplay-VariableFont_wght.ttf', 50)
font2 = pygame.font.Font('PlayfairDisplay-VariableFont_wght.ttf', 40)

shots = 0
hits = 0

image = pygame.image.load("Pixel-Image_07.png")
image = pygame.transform.scale(image, (800, 800))

start_time = time.time()
game_over = False
score_screen = False
score_displayed = False

def spawn_monster_clump():
    """Spawns a clump of monsters."""
    clump_size = random.randint(2, 5)  # Number of monsters in a clump
    base_x = random.randint(0, 700)
    base_y = random.randint(0, 600)
    for _ in range(clump_size):
        x_offset = random.randint(-20, 20)
        y_offset = random.randint(-20, 20)
        direction = "left" if random.random() < 0.5 else "right"
        myNewMonster = Monster(base_x + x_offset, base_y + y_offset, direction)
        myMonsters.append(myNewMonster)

while not quitVar:
    elapsed_time = time.time() - start_time
    remaining_time = game_duration - elapsed_time

    if remaining_time <= 0:
        pygame.time.wait(2000)
        game_over = True
        remaining_time = 0

    screen.fill(WHITE)
    screen.blit(image, (0, 0))

    if not game_over and not score_screen:
        text = font.render("Shots: ", True, GREEN)
        textRect = text.get_rect(center=(100, 750))
        screen.blit(text, textRect)

        text3 = font.render(str(shots), True, GREEN)
        textRect = text3.get_rect(center=(200, 750))
        screen.blit(text3, textRect)

        text2 = font.render("Hits: ", True, GREEN)
        textRect = text2.get_rect(center=(300, 750))
        screen.blit(text2, textRect)

        text4 = font.render(str(hits), True, GREEN)
        textRect = text4.get_rect(center=(400, 750))
        screen.blit(text4, textRect)

        time_text = font.render("Time (s): " + str(int(remaining_time)), True, GREEN)
        time_rect = time_text.get_rect(center=(650, 750))
        screen.blit(time_text, time_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = True

        if event.type == pygame.MOUSEBUTTONUP:
            shots += 1
            for monStar in myMonsters:
                if monStar.rect.collidepoint(event.pos):
                    hits += 1
                    myMonsters.remove(monStar)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_over or score_screen:
                score_screen = False
                game_over = False
                myMonsters.clear()
                shots = 0
                hits = 0
                start_time = time.time()
                score_displayed = False

    if not game_over and not score_screen:
        if random.random() < 0.05:  # Adjust probability to control spawn frequency
            spawn_monster_clump()

        for monStar in myMonsters:
            monStar.fly(screen)

    if game_over and not score_screen and not score_displayed:
        score_screen = True
        score = hits - shots
        score_displayed = True

    if score_displayed:
        score_text = font.render("Score: " + str(score), True, GREEN)
        score_rect = score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(score_text, score_rect)

        restart_text = font2.render("Press SPACE to restart", True, GREEN)
        restart_rect = restart_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))
        screen.blit(restart_text, restart_rect)
        
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
