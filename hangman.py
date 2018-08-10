
class HMan:

    guesses = []

    noStrikes = ["\n\n _________     ", "|         |    ", "|            ", "|          ",
                 "|         ", "|              ", "|              \n\n"]

    strike_one = ["\n\n _________     ", "|         |    ", "|         0    ", "|          ",
                  "|          ", "|              ", "|              \n\n"]

    strike_two = ["\n\n _________     ", "|         |    ", "|         0    ", "|         |  ",
                  "|          ", "|              ", "|              \n\n"]

    strike_three = ["\n\n _________     ", "|         |    ", "|         0    ", "|        /|  ",
                  "|          ", "|              ", "|              \n\n"]

    strike_four = ["\n\n _________     ", "|         |    ", "|         0    ", "|        /|\  ",
                    "|          ", "|              ", "|              \n\n"]

    strike_five = ["\n\n _________     ", "|         |    ", "|         0    ", "|        /|\  ",
                   "|        /   ", "|              ", "|              \n\n"]

    strike_six = ["\n\n _________     ", "|         |    ", "|         0    ", "|        /|\  ",
                   "|        / \  ", "|              ", "|              \n\n"]

    def __init__(self):
        self.title()
        self.word = self.get_word()
        self.letters_left = self.word.__len__()
        self.guessed_string = list('_' * self.word.__len__())
        self.strikes = 0



    def title(self):
        print("    __  __      __  ___          ")
        print("   / / / /     /  |/  /___ _____ ")
        print("  / /_/ /_____/ /|_/ / __ `/ __ \\")
        print(" / __  /_____/ /  / / /_/ / / / /")
        print('/_/ /_/     /_/  /_/\__,_/_/ /_/\n\n\n')
        print('Directions: \t\tEnter word for other player to guess\n\t\t\tWord cannot contain numbers')

    def win_text(self):
        print(" _    ___      __                  ")
        print("| |  / (_)____/ /_____  _______  __")
        print("| | / / / ___/ __/ __ \/ ___/ / / /")
        print("| |/ / / /__/ /_/ /_/ / /  / /_/ / ")
        print("|___/_/\___/\__/\____/_/   \__, /  ")
        print("                          /____/   ")

    def get_word(self):
        while True:
            wrd = list(input("\nEnter your word    "))
            if self.hasDigit(wrd) is True:
                print("\t\t\tWord cannot contain any numbers")
            else:
                print("\n\n\n\n\n\n\n\n\n\n")
                return wrd

    def hasDigit(self, wrd):
        return any(char.isdigit() for char in wrd)

    def print_guessed(self):
        for i in self.guessed_string:
            print(i, end=' ')

    def print_attempts(self):
        for i in self.guesses:
            print(i, end=', ')

    def print_word(self):
        for i in self.word:
            print(i, end='')

    def print_board(self):
        print("Word: ", end='')
        self.print_guessed()
        print("\t\tGuesses: ", end='')
        self.print_attempts()

        if self.strikes == 0:
            for i in self.noStrikes:
                print(i)

        if self.strikes == 1:
            for i in self.strike_one:
                print(i)

        if self.strikes == 2:
            for i in self.strike_two:
                print(i)

        if self.strikes == 3:
            for i in self.strike_three:
                print(i)

        if self.strikes == 4:
            for i in self.strike_four:
                print(i)

        if self.strikes == 5:
            for i in self.strike_five:
                print(i)

        if self.strikes == 6:
            for i in self.strike_six:
                print(i)

    def guess(self):
        g = input('Guess a letter\t\t')

        while g.__len__() > 1 or self.hasDigit(g) is True or g in self.guesses:
            g = input('Guess cannot be number, multiple characters or already guessed')

        if g in self.word and g not in self.guesses:
            self.guesses.append(g)

            for i in range(0, self.guessed_string.__len__()):
                if self.word[i] == g:
                    self.guessed_string[i] = g
                    self.letters_left -= 1

            print(u'\u2713 Correct!\n\n')
            return g
        else:
            print('Nope!\n\n')
            self.strikes += 1
            self.guesses.append(g)
            return False

    def play(self):

        while self.strikes < 6 and self.letters_left != 0:

            self.print_board()

            self.guess()

        if self.strikes == 6:
            self.print_board()
            print("\n\n\nGAME OVER\nWord: ", end='')
            self.print_word()
        if self.letters_left == 0:
            print("\n\n\n\n\n\n\n")
            self.win_text()
            print("You Guessed Right!")


class main:

    game = HMan()
    game.play()