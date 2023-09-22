import pygame
import random
from words import words_list
import math

pygame.init()


class Hangman:
    click_sound = pygame.mixer.Sound("sounds/CLICKS.wav")
    slide_down_sound = pygame.mixer.Sound("sounds/SLIDE_DOWN.wav")

    correct_sound = pygame.mixer.Sound("sounds/CORRECT.wav")
    wrong_sound = pygame.mixer.Sound("sounds/INCORRECT.wav")
    time_up_sound = pygame.mixer.Sound("sounds/TIME-UP.wav")

    # list of letters in the random word
    start_ticks = pygame.time.get_ticks()
    clock = pygame.time.Clock()

    # screen
    screen_number = 1
    screen = ""

    # level = 1
    die_count = 0
    numberOfGames = 4
    die = False
    time_up = False
    hint = 0
    random_word = ""

    timer = 0  # untimed
    selection_dict = {"MODE": "NORMAL", "TIMED": "UNTIMED", "DIFFICULTY": "EASY"}
