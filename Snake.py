from Snake_Objekt import *
import pygame

window = pygame.display.set_mode(Size_window)
clock = pygame.time.Clock()
pygame.font.init()
pygame.display.set_caption('Snake')
apple = Apple(window)
Score = Text(1080, 20, 0, (0, 0, 0), 36, window)
Best_score = Text(20, 20, 0, (0, 0, 0), 36, window)
Sk = Snake(window, apple, Score, Best_score)


def start_poz():
    Sk.start_poz()


def rend():
    window.fill(White)
    Sk.moving()
    pygame.display.flip()


def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not Sk.available_size['Right']:
                        Sk.available_size = {'Right': False, 'Left': True, 'Up': False, 'Down': False}
                        # break
                elif event.key == pygame.K_RIGHT:
                    if not Sk.available_size['Left']:
                        Sk.available_size = {'Right': True, 'Left': False, 'Up': False, 'Down': False}
                        # break
                elif event.key == pygame.K_DOWN:
                    if not Sk.available_size['Up']:
                        Sk.available_size = {'Right': False, 'Left': False, 'Up': False, 'Down': True}
                        # break
                elif event.key == pygame.K_UP:
                    if not Sk.available_size['Down']:
                        Sk.available_size = {'Right': False, 'Left': False, 'Up': True, 'Down': False}
                        # break
                elif event.key == pygame.K_SPACE:
                    start_poz()
                break

        rend()
        clock.tick(FPS)


if __name__ == '__main__':
    game()
