import sys, os
import csv
import time
import random
import itertools
import pygame

from algorithms import *
from visualiser import Visualiser

pygame.init()
os.system("cls")

size = width, height = 1200, 700
bg_color = (34, 40, 54)
text_color = (255, 255, 255)
column_color = (47, 224, 38) # GREEN
# column_color = (147, 124, 88) # BEIGE
# column_color = (234, 20, 20) # RED
# column_color = (230, 230, 230) # WHITE

screen = pygame.display.set_mode(size, pygame.RESIZABLE, vsync=True)
clock = pygame.time.Clock()
main_font_normal = pygame.font.Font("./fonts/SF Atarian System Bold.ttf", 24)
main_font_big = pygame.font.Font("./fonts/SF Atarian System Bold.ttf", 36)

visualiser = Visualiser(screen, bubble_sort, clock, column_color)

file = 'data.csv'
with open(file, "r", newline='') as f:
    dataset = list(itertools.chain.from_iterable(csv.reader(f)))
    dataset = [int(x) for x in dataset if x != '' and (not x.isspace())]
print(f"Successfully loaded '{file}' {round(os.path.getsize(file) / 1024, 2)}KB")
print(f"Dataset size : {len(dataset)}")
print(f"Biggest value in set : {max(dataset)}")
print(f"Smallest value in set : {min(dataset)}")

icon_file = "icon.png"
pygame.display.set_caption("Dean's Algorithm Visualiser")
pygame.display.set_icon(pygame.image.load(icon_file))
print(f"Successfully loaded '{icon_file}' {round(os.path.getsize(icon_file) / 1024, 2)}KB")

pressed = True
milliseconds = 0
second_counter = 0
click_delay = 200

fps = 10 if len(dataset) <= 80 else 60

show_text = True
start_sorting = False

start_pause = main_font_big.render(f"Press SPACE to Start/Pause", True, text_color)

print("Entering program loop")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE) and pressed:
                start_sorting = not start_sorting
                pressed = False
                second_counter = 0

            if (event.key == pygame.K_q):
                for _ in range(10):
                    dataset.append(random.randint(1, max(dataset)))

            if (event.key == pygame.K_t):
                show_text = not show_text

    if second_counter >= click_delay:
        pressed = True

    screen.fill(bg_color)

    #* Game functionality under here


    # visualiser loop
    dataset = visualiser.run(dataset, start_sorting)
    visualiser.show_stats(main_font_normal)

    # ? Give bars random colors
    # visualiser.set_column_color(
    #     (random.randint(1, 255),
    #      random.randint(1, 255),
    #      random.randint(1, 255))
    # )

    if (not start_sorting) and show_text:
        start_pause_size = start_pause.get_size()
        start_pause_pos = ((screen.get_width() / 2) - (start_pause_size[0] / 2), screen.get_height() * 0.75)
        screen.blit(start_pause, start_pause_pos)

    # tick the game
    ticks = clock.tick(fps)    
    milliseconds += ticks
    second_counter += ticks

    # make changes visible
    pygame.display.flip()




