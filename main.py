import random
import pygame
from pygame import time
import time
from screen_1 import Screen_1
from screen_2 import Screen_2
from default import Hangman


pygame.init()
pygame.display.set_caption("Hangman")
icon = pygame.image.load("images/hangmanIco.png")
pygame.display.set_icon(icon)

pygame.mixer.music.set_volume(0.45)  # initializing the music system
pygame.mixer.music.load("sounds/videoplayback.wav")
pygame.mixer.music.play(-1)
Hangman.screen = pygame.display.set_mode((600, 400))


sc1 = Screen_1()
sc2 = Screen_2()

running = True
pressed_start = False

while running:
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(sc1.selection_dict, Hangman.hint)
            if (
                248 <= mouse_pos[0] <= 368
                and 330 <= mouse_pos[1] <= 380
                and pressed_start == False
            ):
                Hangman.screen_number = 2
                pressed_start = True
                sc2.start_time = time.time()

            elif (
                224 <= mouse_pos[0] <= 374
                and 332 <= mouse_pos[1] <= 382
                and pressed_start == True
            ):
                Hangman.screen_number = 1
                pressed_start = False

            if Hangman.screen_number == 1:
                sc1.set_config(mouse_pos)

            elif Hangman.screen_number == 2:
                sc2.update_button(mouse_pos)

        if Hangman.screen_number == 1:
            Hangman.screen.fill((0, 0, 0))
            sc1.show()

        elif Hangman.screen_number == 2:  # for keyboard press
            sc2.show()
            sc2.play_breakpoints()
            sc2.keypress(event)

    if Hangman.screen_number == 2:  # for time
        sc2.show()
        sc2.play_breakpoints()

    pygame.display.update()
