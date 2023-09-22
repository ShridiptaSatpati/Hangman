import pygame
import time
from default import Hangman


class Screen_1(Hangman):
    def non_duplicater(self, string):
        non_duplicate_list = []
        new_string = ""
        for element in string:
            if element not in non_duplicate_list:
                non_duplicate_list.append(element)
        return new_string.join(non_duplicate_list)

    def show_text(self, text, font_size, x, y):
        font = pygame.font.Font("freesansbold.ttf", int(font_size))
        font_render_text = font.render(str(text), True, (255, 255, 255))
        font_display_screen = Hangman.screen.blit(font_render_text, (int(x), int(y)))

    def join(self, iterable):  # with space
        join_str = ""
        for elements in iterable:
            join_str += " " + elements
        return join_str

    def draw_button_modes(self):
        if Hangman.selection_dict["MODE"] == "NORMAL":
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (275, 112, 100, 30), 0)
            self.show_text("NORMAL", 20, 280, 118)
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (390, 112, 110, 30), 3)
            self.show_text("SURVIVAL", 20, 395, 118)
        else:
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (275, 112, 100, 30), 3)
            self.show_text("NORMAL", 20, 280, 118)
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (390, 112, 110, 30), 0)
            self.show_text("SURVIVAL", 20, 395, 118)

    def draw_button_difficulty(self):
        self.show_text("DIFFICULTY?", 21, 278, 243)

        if Hangman.selection_dict["DIFFICULTY"] != "EASY":
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (272, 268, 68, 28), 3)
            self.show_text("EASY", 18, 280, 274)
        else:
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (272, 268, 68, 28), 0)
            self.show_text("EASY", 18, 280, 274)

        if Hangman.selection_dict["DIFFICULTY"] != "MODERATE":
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (353, 268, 118, 28), 3)
            self.show_text("MODERATE", 18, 360, 274)
        else:
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (353, 268, 118, 28), 0)
            self.show_text("MODERATE", 18, 360, 274)

        if Hangman.selection_dict["DIFFICULTY"] != "HARD":
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (486, 268, 68, 28), 3)
            self.show_text("HARD", 18, 493, 274)
        else:
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (486, 268, 68, 28), 0)
            self.show_text("HARD", 18, 493, 274)

    def draw_button_timed(self):
        self.show_text("TIMED?", 21, 278, 155)

        if Hangman.selection_dict["TIMED"] != "30 S":
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (275, 184, 40, 20), 3)
            self.show_text("30 S", 15, 280, 188)

        else:
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (275, 184, 40, 20), 0)
            self.show_text("30 S", 15, 280, 188)

        if Hangman.selection_dict["TIMED"] != "1 M":
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (325, 184, 40, 20), 3)
            self.show_text("1 M", 15, 332, 188)

        else:
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (325, 184, 40, 20), 0)
            self.show_text("1 M", 15, 332, 188)

        if Hangman.selection_dict["TIMED"] != "2 M":
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (275, 212, 40, 20), 3)
            self.show_text("2 M", 15, 282, 216)
        else:
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (275, 212, 40, 20), 0)
            self.show_text("2 M", 15, 282, 216)

        if Hangman.selection_dict["TIMED"] != "4 M":
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (325, 212, 40, 20), 3)
            self.show_text("4 M", 15, 332, 216)
        else:
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (325, 212, 40, 20), 0)
            self.show_text("4 M", 15, 332, 216)

        if Hangman.selection_dict["TIMED"] != "UNTIMED":
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (390, 198, 111, 30), 3)
            self.show_text("UNTIMED", 20, 398, 205)
        else:
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (390, 198, 111, 30), 0)
            self.show_text("UNTIMED", 20, 398, 205)

    def set_config(self, mouse_pos):
        # survival mode - more hint but 1 lives and 9 games
        # normal mode - fewer hint but 3 lives and 1 game
        # more difficult less hint
        # more time more number of games

        # set mode
        if Hangman.selection_dict["MODE"] == "NORMAL":
            self.die_count = 3
        else:
            self.die_count = 1  # survival mode

        if 275 <= mouse_pos[0] <= 375 and 112 <= mouse_pos[1] <= 142:
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (275, 112, 100, 30), 0)
            Hangman.selection_dict["MODE"] = "NORMAL"
            self.die_count = 3

        if 390 <= mouse_pos[0] <= 500 and 112 <= mouse_pos[1] <= 142:
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (390, 112, 110, 30), 0)
            Hangman.selection_dict["MODE"] = "SURVIVAL"
            self.die_count = 0

        # set timer
        if 390 <= mouse_pos[0] <= 501 and 198 <= mouse_pos[1] <= 220:
            pygame.draw.rect(Hangman.screen, (225, 0, 0), (390, 198, 111, 30), 0)
            Hangman.selection_dict["TIMED"] = "UNTIMED"
            Hangman.timer = 1e10
            Hangman.numberOfGames = 9

        if 275 <= mouse_pos[0] <= 310 and 184 <= mouse_pos[1] <= 204:
            Hangman.selection_dict["TIMED"] = "30 S"
            Hangman.timer = 30
            Hangman.numberOfGames = 1

        if 325 <= mouse_pos[0] <= 360 and 184 <= mouse_pos[1] <= 204:
            Hangman.selection_dict["TIMED"] = "1 M"
            Hangman.timer = 60
            Hangman.numberOfGames = 2

        if 275 <= mouse_pos[0] <= 315 and 212 <= mouse_pos[1] <= 232:
            Hangman.selection_dict["TIMED"] = "2 M"
            Hangman.timer = 120
            Hangman.numberOfGames = 4

        if 325 <= mouse_pos[0] <= 365 and 212 <= mouse_pos[1] <= 232:
            Hangman.selection_dict["TIMED"] = "4 M"
            Hangman.timer = 240
            Hangman.numberOfGames = 6

        # set difficulty
        if 272 <= mouse_pos[0] <= 272 + 68 and 268 <= mouse_pos[1] <= 268 + 28:
            Hangman.selection_dict["DIFFICULTY"] = "EASY"
            Hangman.hint = len(self.non_duplicater(Hangman.random_word)) - 3

        if 353 <= mouse_pos[0] <= 353 + 118 and 268 <= mouse_pos[1] <= 268 + 28:
            Hangman.selection_dict["DIFFICULTY"] = "MODERATE"
            Hangman.hint = len(self.non_duplicater(Hangman.random_word)) - 4

        if 486 <= mouse_pos[0] <= 486 + 68 and 268 <= mouse_pos[1] <= 268 + 28:
            Hangman.selection_dict["DIFFICULTY"] = "HARD"
            Hangman.hint = len(self.non_duplicater(Hangman.random_word)) - 5

        if Hangman.selection_dict["MODE"] == "SURVIVAL":
            if Hangman.selection_dict["DIFFICULTY"] == "EASY":
                Hangman.hint = 14
            if Hangman.selection_dict["DIFFICULTY"] == "MODERATE":
                Hangman.hint = 8
            if Hangman.selection_dict["DIFFICULTY"] == "HARD":
                Hangman.hint = 4

    def show(self):
        Hangman.screen.fill((0, 0, 0))
        backgroundImg1 = pygame.image.load(f"images/hangmanImg9.png")
        Hangman.screen.blit(backgroundImg1, (0, 0))

        # draw buttons
        self.show_text("HANGMAN", 30, 220, 20)
        self.show_text("WELCOME BACK!", 18, 273, 82)
        self.draw_button_modes()
        self.draw_button_timed()
        self.draw_button_difficulty()
        pygame.draw.rect(Hangman.screen, (225, 0, 0), (248, 330, 120, 50), 3)
        self.show_text("START", 21, 272, 345)
