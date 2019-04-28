from hangman import GameState, GuessResult, createHangmanGame, HangmanGameScorer

game = createHangmanGame()

while game.state == GameState.IN_PROGRESS:

    displayWord = "".join([f"{l} " for l in game.revealedWord])

    print(displayWord)
    print(f"Guesses remaining: {game.numFailedGuessesRemaining}")

    guess = input(f"Choose a letter : ")

    guessResult = game.guess(guess)

    if guessResult == GuessResult.FAIL_INVALID_INPUT:
        print("Invalid input")
    elif guessResult == GuessResult.FAIL_ALREADY_GAME_OVER:
        print("Game is already over")
    elif guessResult == GuessResult.FAIL_ALREADY_GUESSED:
        print("Letter was already guessed")


if game.state == GameState.WON:
    print("You won!")
elif game.state == GameState.LOST:
    print("You lost!")

score = HangmanGameScorer.score(game)
print(f"Score: {score}")
