from GameStatus import GameStatus
from game import Game

game = Game()
word = game.generate_word()

print(f'The word consists of {len(word)} letters')
print('Try to guess the word letter by letter')
print('You can also try to guess the word by typing it. To do that type "guess_word" instead of a letter')

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input('Pick a letter: \n')
    if letter.lower() == 'guess_word':
        game.guess_word(input('Enter the word: \n'))
    else:

        state = game.guess_letter(letter)
        print(*game.display_word)

    print(f'Tries remaining: {game.guesses_remaining}')
    print(f"You have already tried these letters: {', '.join(game.tried_letters)}")



if game.game_status == GameStatus.LOST:
    print('You are hanged')
    print(f'The word was {game.show_word}')

if game.game_status == GameStatus.WON:
    print('You won')
    print(f'The word was {game.show_word}')