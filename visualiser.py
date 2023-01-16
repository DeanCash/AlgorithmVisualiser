import pygame
from pygame import Surface, Vector2
from pygame.font import Font
from pygame.time import Clock
from typing import Any, Callable, Generator, Tuple

class Visualiser:
    def __init__(self, screen: Surface, algorithm: Callable, clock: Clock, color: Tuple[int, int, int]):
        self.screen = screen
        self.algorithm = algorithm
        self.clock = clock
        self.column_color = color
        self.__line_thickness = 3
        self.__iterations = 0
        self.__sorted = False


    def run(self, dataset: list[int], start_sort: bool):
        dataset_len = len(dataset)
        biggest_val = max(dataset)

        sw, sh = [float(i) for i in self.screen.get_size()]
        bar_color = (255 - self.column_color[0], 255 - self.column_color[1], 255 - self.column_color[2])
        col_size = sw / dataset_len

        col_top = Vector2(0.0, 0.0)
        col_bottom = Vector2(0.0, sh)

        if start_sort:
            try:
                dataset = next(self.algorithm(dataset))
                self.__sorted = False
                self.__iterations += 1
            except:
                self.__sorted = True

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
                                self.__line_thickness)
        return dataset

    def show_stats(self, font: Font):
        text_color = (255, 255, 255)
        fps = self.clock.get_fps()

        fps_text = font.render(f"FPS: {round(fps, 1)}", True, text_color)
        fps_text_size = fps_text.get_size()
        fps_text_pos = (self.screen.get_width() - 100, fps_text_size[1])
        self.screen.blit(fps_text, fps_text_pos)

        iteration_text = font.render(f"ITERATIONS: {self.__iterations}", True, text_color)
        iteration_text_size = iteration_text.get_size()
        iteration_text_pos = (self.screen.get_width() - 270, iteration_text_size[1])
        self.screen.blit(iteration_text, iteration_text_pos)
        
        algorithm_kind_text = font.render(f"{self.algorithm.__name__}".upper(), True, text_color)
        algorithm_kind_text_size = algorithm_kind_text.get_size()
        algorithm_kind_text_pos = (10, algorithm_kind_text_size[1])
        self.screen.blit(algorithm_kind_text, algorithm_kind_text_pos)

    def set_column_color(self, color: Tuple[int, int, int]):
        self.column_color = color







