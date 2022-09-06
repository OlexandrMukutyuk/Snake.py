import random
from Snake_Settings import *

import pygame


class Snake:
    def __init__(self, window, apple, text, best_score, size_player=3, size_body_player=50, cords=spawn_cords,
                 color=Light_Green,
                 x=Size_window_x / 2, y=Size_window_y / 2):
        self.window = window
        self.Apple = apple
        self.Score = text
        self.Best_Score = best_score
        self.size_player = size_player
        self.size_body_player = size_body_player
        self.color = color
        self.head_collision = None
        self.cords = cords
        self.x = x
        self.y = y
        self.available_size = {'Right': True, 'Left': False, 'Up': False, 'Down': False}
        self.rend()

    def start_poz(self):
        self.size_player = 3
        self.cords = [(Size_window_x / 2, Size_window_y / 2, 50, 50),
                      (Size_window_x / 2 - 50, Size_window_y / 2, 50, 50),
                      (Size_window_x / 2 - 100, Size_window_y / 2, 50, 50)]
        self.x, self.y = Size_window_x / 2, Size_window_y / 2
        self.available_size = {'Right': True, 'Left': False, 'Up': False, 'Down': False}
        self.Apple.gen_cord((0, 0, 0, 0))
        if self.Score.tex > self.Best_Score.tex:
            self.Best_Score.tex = self.Score.tex
        self.Score.tex = 0

    def rend(self):
        self.Apple.rend()
        for snake in range(len(self.cords)):
            pygame.draw.rect(self.window, self.color, self.cords[snake])
            pygame.draw.rect(self.window, Dark, self.cords[snake], 1)
        self.Score.rend()
        self.Best_Score.rend()

    def moving(self):
        for num in range(self.size_player - 1):
            self.cords[-num - 1] = self.cords[-num - 2]
        if self.available_size['Right']:
            self.cords[0] = (self.x + 50, self.y, self.size_body_player, self.size_body_player)
            self.x += 50
            self.end_game()
            self.apple_eating()
        elif self.available_size['Left']:
            self.cords[0] = (self.x - 50, self.y, self.size_body_player, self.size_body_player)
            self.x -= 50
            self.end_game()
            self.apple_eating()
        elif self.available_size['Up']:
            self.cords[0] = (self.x, self.y - 50, self.size_body_player, self.size_body_player)
            self.y -= 50
            self.end_game()
            self.apple_eating()
        elif self.available_size['Down']:
            self.cords[0] = (self.x, self.y + 50, self.size_body_player, self.size_body_player)
            self.y += 50
            self.end_game()
            self.apple_eating()
        self.rend()

    def end_game(self):
        if self.x > Size_window_x - 50 or self.x < 0:
            self.start_poz()
        elif self.y > Size_window_y - 50 or self.y < 0:
            self.start_poz()
        for num in range(self.size_player - 1):
            if self.cords[0] == self.cords[num + 1]:
                self.start_poz()
                break

    def apple_eating(self):
        if self.cords[0] == self.Apple.cord:
            self.cords.append((0, 0, 0, 0))
            self.size_player += 1
            self.Apple.gen_cord(self.cords)
            self.Score.tex += 1



class Apple:
    def __init__(self, window, size=50, color=Red, cord=spawn_cords_apple):
        self.window = window
        self.size = size
        self.color = color
        self.cord = cord
        self.temp = cord
        self.gen_cord((0, 0, 0, 0))

    def rend(self):
        pygame.draw.rect(self.window, self.color, self.cord)
        pygame.draw.rect(self.window, Light_Red, self.cord, 2)

    def gen_cord(self, cords):
        while True:
            self.temp = (random.randint(0, 23) * 50, random.randint(0, 11) * 50, self.size, self.size)
            for num in cords:
                if self.temp == num:
                    break
                elif num == cords[-1]:
                    self.cord = self.temp
            if self.cord == self.temp:
                break


class Text:

    def rend(self):
        pygame.draw.rect(self.window, (224, 224, 224), (self.x - 10, self.y - self.size / 4, 100, self.size))
        pygame.draw.rect(self.window, (192, 192, 192), (self.x - 10, self.y - self.size / 4, 100, self.size), 2)
        self.window.blit(self.fonts.render(str(self.tex), True, self.color), (self.x, self.y))

    def __init__(self, x, y, tex, color, size, window):
        self.x = x
        self.y = y
        self.window = window
        self.tex = tex
        self.color = color
        self.size = size
        self.fonts = pygame.font.Font(None, size)
