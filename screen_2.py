import pygame
from default import Hangman
import random
import time
from words import words_list


class Screen_2(Hangman):
    def __init__(self):
        self.level = 1
        self.reset()

    def join(self, iterable, char):  # with space
        join_str = ""
        for elements in iterable:
            join_str += char + elements
        return join_str

    def show_text(self, text, font_size, x, y):
        font = pygame.font.Font("freesansbold.ttf", int(font_size))
        font_render_text = font.render(str(text), True, (255, 255, 255))
        Hangman.screen.blit(font_render_text, (int(x), int(y)))

    def show_stopwatch(self, total_time):  # for timed ones
        # second = (total_time - (int(time.perf_counter()))) + current_time
        second = int(time.time() - self.start_time)

        if self.selection_dict["TIMED"] == "UNTIMED":
            self.show_text(f"TIME: 00", 23, 280, 35)
        else:
            if second <= total_time:
                min = second // 60
                second = second % 60
                self.show_text(f"TIME: {min} mins, {second} secs", 23, 215, 35)

                # return f"{min} mins, {second} secs"
            else:
                self.time_up = True
                self.show_text(f"TIME: 0 mins, 0 secs", 23, 215, 35)

    def reset(self):
        self.text = ""
        self.coor = 0, 0, 0
        self.random_word = random.choice(words_list)
        words_list.remove(self.random_word)

        self.correct_guesses = ["_" for item in self.random_word]
        self.already_guessed = []
        self.wrong_guesses = []

        self.time_up = False
        self.die = False
        self.die_count = 0
        self.start_time = time.time()
        print(self.random_word)

        if Hangman.selection_dict["MODE"] == "NORMAL":
            if Hangman.selection_dict["DIFFICULTY"] == "EASY":
                Hangman.hint = len(self.random_word) - 3

            if Hangman.selection_dict["DIFFICULTY"] == "MODERATE":
                Hangman.hint = len(self.random_word) - 4

            if Hangman.selection_dict["DIFFICULTY"] == "HARD":
                Hangman.hint = len(self.random_word) - 5

        # if Hangman.selection_dict["MODE"] == "SURVIVAL":
        #     if Hangman.selection_dict["DIFFICULTY"] == "EASY":
        #         Hangman.hint = 14
        #     if Hangman.selection_dict["DIFFICULTY"] == "MODERATE":
        #         Hangman.hint = 8
        #     if Hangman.selection_dict["DIFFICULTY"] == "HARD":
        #         Hangman.hint = 4

    def draw_button(self):  # replay, surrender, hint
        pygame.draw.rect(Hangman.screen, (225, 0, 0), (100, 330, 100, 50), 3)
        self.show_text("REPLAY", 21, 107, 346)

        pygame.draw.rect(Hangman.screen, (225, 0, 0), (224, 330, 150, 50), 3)
        self.show_text("SURRENDER", 21, 232, 346)

        pygame.draw.rect(Hangman.screen, (225, 0, 0), (400, 330, 100, 50), 3)
        self.show_text("HINT", 21, 425, 346)

    def draw_header(self):
        # display current selected mode
        self.show_text("MODE~ " + str(self.selection_dict["MODE"]), 19, 10, 15)

        if self.selection_dict["TIMED"] == "UNTIMED":  # show time remaining
            self.show_text(self.selection_dict["TIMED"], 15, 45, 40)
            self.show_text(self.selection_dict["DIFFICULTY"], 15, 130, 40)
        else:
            if self.selection_dict["DIFFICULTY"] == "MODERATE":
                self.show_text(self.selection_dict["TIMED"], 15, 60, 40)
                self.show_text(self.selection_dict["DIFFICULTY"], 15, 100, 40)
            else:
                self.show_text(self.selection_dict["TIMED"], 15, 85, 40)
                self.show_text(self.selection_dict["DIFFICULTY"], 15, 125, 40)

        self.show_text(f"LEVEL {self.level}/{Hangman.numberOfGames}", 25, 270, 10)

        # display hints left
        if Hangman.hint > 0:
            self.show_text(f"HINT {str(Hangman.hint)}", 25, 490, 10)  # hint counter
        elif Hangman.hint <= 0:
            self.show_text(f"HINT 0", 25, 490, 10)  # hint counter

        # stopwatch
        self.show_stopwatch(Hangman.timer)

        self.show_text(self.join(self.correct_guesses, " "), 32, 265, 100)
        self.show_text("WRONG GUESSES: ", 15, 270, 220)
        self.show_text(self.join(self.wrong_guesses, " "), 32, 265, 250)

    def update_button(self, mouse_pos):
        if 100 <= mouse_pos[0] <= 200:  # pressed replay button
            if 330 <= mouse_pos[1] <= 380:
                self.reset()

        if (
            400 <= mouse_pos[0] <= 500 and 332 <= mouse_pos[1] <= 382
        ):  # pressed hint button
            if Hangman.hint > 0:
                Hangman.hint -= 1
                res = []
                res[:] = self.random_word.upper()

                not_guessed = set(res) - set(self.already_guessed)

                self.rand_choice_hint = random.choice(tuple(not_guessed))
                for index, char in enumerate(self.random_word.upper()):
                    if char == self.rand_choice_hint:
                        self.correct_guesses[index] = self.rand_choice_hint
                self.already_guessed.append(self.rand_choice_hint)

    def home_screen(self):
        pygame.display.update()
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        time.sleep(2)
        Hangman.screen_number = 1
        pygame.event.set_allowed(pygame.MOUSEMOTION)

    def play_breakpoints(self):
        if self.die:
            backgroundImg9 = pygame.image.load(f"images/hangmanImg9.png")
            Hangman.screen.blit(backgroundImg9, (0, 0))

            self.show_text("OH NO! YOU DIED", 32, 260, 120)
            self.show_text("THE WORD WAS:", 20, 290, 195)
            self.show_text(self.random_word.upper(), 30, 290, 235)
            self.reset()
            self.home_screen()

        elif self.join(self.correct_guesses, "") == self.random_word.upper():
            print("correctly done")
            backgroundImg9 = pygame.image.load(f"images/hangmanImg9.png")
            Hangman.screen.blit(backgroundImg9, (0, 0))

            self.show_text("LEVEL COMPLETED", 32, 250, 120)
            self.show_text("CORRECT THE WORD IS:", 20, 250, 210)
            self.show_text(self.random_word.upper(), 28, 300, 250)
            self.reset()
            pygame.display.update()
            pygame.event.set_blocked(pygame.MOUSEMOTION)
            time.sleep(2)
            pygame.event.set_allowed(pygame.MOUSEMOTION)
            self.level += 1

        elif self.level > Hangman.numberOfGames:
            backgroundImg9 = pygame.image.load(f"images/hangmanImg9.png")
            Hangman.screen.blit(backgroundImg9, (0, 0))

            self.show_text("BRAVO!", 28, 345, 100)
            self.show_text("YOU ESCAPED", 28, 295, 140)
            self.show_text("ALL LEVELS COMPLETE", 24, 253, 230)

            self.reset()
            self.level = 1
            self.home_screen()

        elif self.time_up:
            backgroundImg9 = pygame.image.load(f"images/hangmanImg9.png")
            Hangman.screen.blit(backgroundImg9, (0, 0))

            self.show_text("TIME UP! YOU DIED", 32, 260, 120)
            self.show_text("THE WORD WAS:", 20, 290, 195)
            self.show_text(self.random_word.upper(), 30, 290, 235)

            self.reset()
            self.home_screen()

    def keypress(self, event):
        if self.die_count >= 9:
            self.die = True
            self.die_count = 0

        if event.type == pygame.KEYDOWN:
            event_chr = ""
            event_ord = event.key  # getting A, B, C...

            if 97 <= int(event_ord) <= 122 or 65 <= int(event_ord) <= 90:
                event_chr = chr(event_ord).upper()

            if event_chr in self.already_guessed:
                # already_guessed containes correct aswell as
                # self.show_text("ALREADY GUESSED THAT LETTER", 18, 270, 160)
                self.text = "ALREADY GUESSED THAT LETTER"
                self.coor = 18, 270, 160

            elif (
                event_chr in self.random_word.upper()
                and event_chr not in self.already_guessed
            ):
                # self.show_text("CORRECT!", 20, 330, 155)

                self.text = "CORRECT!"
                self.coor = 20, 330, 155

                self.already_guessed.append(event_chr)

                self.correct_sound.play()

                for index, char in enumerate(
                    self.random_word.upper()
                ):  # changing the underscores with letters
                    if char == event_chr:
                        self.correct_guesses[index] = event_chr

            elif (
                event_chr not in self.random_word.upper()
                and event_chr not in self.already_guessed
            ):
                # self.show_text("WORNG LETTER", 20, 330, 155)
                self.text = "WORNG LETTER"
                self.coor = 20, 330, 155

                self.already_guessed.append(event_chr)

                self.wrong_sound.play()

                self.wrong_guesses.append(event_chr)
                self.die_count += 1

        if event.type == pygame.KEYUP:
            self.text = ""
            self.coor = 0, 0, 0

    def show(self):
        backgroundImg = pygame.image.load(f"images/hangmanImg{self.die_count}.png")
        Hangman.screen.blit(backgroundImg, (0, 0))

        self.draw_header()
        self.draw_button()
        self.show_text(self.text, self.coor[0], self.coor[1], self.coor[2])
