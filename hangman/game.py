import random
from collections.abc import Iterable

from GameStatus import GameStatus
from graphics import stages
from invalid_operation_exception import IvalidOperationException
from words import word_list


class Game:

    def __init__(self):
        self.__guesses_remaining = 6
        self.__tried_letters = []
        self.__display_word = []
        self.__display_hangman = stages[self.__guesses_remaining]
        self.__game_status = GameStatus.NOT_STARTED
        self.__word = ''

    def generate_word(self):
        self.__word = random.choice(word_list)
        self.__display_word = ['_' for _ in range(len(self.__word))]
        self.__game_status = GameStatus.IN_PROGRESS
        print('The word has been generated')
        print(*self.__display_word)
        return self.__word

    def __is_winning(self):
        return '_' not in self.__display_word

    def guess_letter(self, letter: str):
        if self.__guesses_remaining == 0:
            raise IvalidOperationException('You have exceeded the amount of allowed guesses.')

        if self.__game_status != GameStatus.IN_PROGRESS:
            raise IvalidOperationException(f'Inappropriate status of game. Current game status: {self.__game_status}')

        if letter in self.__tried_letters:
            print('You have already tried that letter')
            return
        elif len(letter) != 1:
            print('You must enter only one letter')
            return

        self.__tried_letters.append(letter.lower())
        if letter.lower() in self.__word.lower():
            for index, char in enumerate(self.__word):
                if char.lower() == letter.lower():
                    self.__display_word[index] = char
            print('You have guessed correctly')
        else:
            self.__guesses_remaining -= 1
            print(
                f"Your guess was wrong. You have {self.__guesses_remaining} guess{'' if self.__guesses_remaining == 1 else 'es'} remaining")

        if self.__is_winning():
            self.__game_status = GameStatus.WON
            print(f'Congratulations! You have guessed the word. The word was {self.__word}')
            return
        elif self.__guesses_remaining == 0:
            self.__game_status = GameStatus.LOST
            print('You have lost the game')
            return

    def guess_word(self, word: str) -> Iterable[str]:
        if word == self.__word:
            self.__game_status = GameStatus.WON
            return f'Congratulations! You have guessed the word. The word was {self.__word}'
        else:
            self.__guesses_remaining -= 1
            print(self.__display_hangman)
            return f'You have guessed incorrectly. You have {self.__guesses_remaining} guess{"" if self.__guesses_remaining == 1 else "es"} remaining'

    @property
    def game_status(self) -> GameStatus:
        return self.__game_status

    @property
    def guesses_remaining(self) -> int:
        return self.__guesses_remaining

    @property
    def tried_letters(self) -> Iterable[str]:
        return sorted(self.__tried_letters)

    @property
    def display_hangman(self) -> str:
        return self.__display_hangman

    @property
    def display_word(self) -> Iterable[str]:
        return self.__display_word

    @property
    def show_word(self) -> str:
        return self.__word