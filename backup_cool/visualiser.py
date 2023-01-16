import pygame
from pygame import Surface, Vector2
from typing import Any, Callable, Generator, Tuple

class Visualiser:
    def __init__(self, screen: Surface, color: Tuple[int, int, int]):
        self.screen = screen
        self.column_color = color
        self.__line_thickness = 3


    def run(self, algorithm: Generator, dataset: list[int]):
        dataset_len = len(dataset)
        biggest_val = max(dataset)

        sw, sh = [float(i) for i in self.screen.get_size()]
        bar_color = (255 - self.column_color[0], 255 - self.column_color[1], 255 - self.column_color[2])
        col_size = sw / dataset_len

        col_top = Vector2(0.0, 0.0)
        col_bottom = Vector2(0.0, sh)

        for i, v in enumerate(dataset):
            col_top.x += col_size
            col_bottom.x += col_size

            col_top.y = ((1 - (v / biggest_val)) * sh)

            pygame.draw.line(self.screen,
                             self.column_color,
                             col_bottom - ((col_size / 2), 0),
                             col_top - ((col_size / 2), 0),
                             int(col_size) + 1)

        if dataset_len <= 80:
            col_top = Vector2(0.0, 0.0)
            col_bottom = Vector2(0.0, sh)
            for _ in range(dataset_len - 1):
                col_top.x += col_size
                col_bottom.x += col_size
                pygame.draw.line(self.screen,
                                bar_color,
                                col_bottom,
                                col_top,
                                3)
        
        




