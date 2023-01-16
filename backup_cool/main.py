import sys, os
import time
import pygame
import csv
import itertools
import random

from algorithms import *
from visualiser import Visualiser

pygame.init()

size = width, height = 1200, 700
bg_color = (34, 40, 54)
column_color = (47, 224, 38)

screen = pygame.display.set_mode(size, vsync=True)
visualiser = Visualiser(screen, column_color)

file = 'data.csv'
with open(file, "r", newline='') as f:
    dataset = list(itertools.chain.from_iterable(csv.reader(f)))
    dataset = [int(x) for x in dataset if x != '' and (not x.isspace())]
    print("SET :", dataset)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    dataset.append(random.randint(1, max(dataset)))
    print("APPENDED")
    
    screen.fill(bg_color)
    # game loop
    visualiser.run(bubble_sort, dataset)

    pygame.display.flip()





