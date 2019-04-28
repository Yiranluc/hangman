import random
from enum import Enum


class GameState(Enum):
    IN_PROGRESS = 0
    WON = 1
    LOST = 2


class GuessResult(Enum):
    CORRECT = 0
    INCORRECT = 1

    FAIL_INVALID_INPUT = 2
    FAIL_ALREADY_GAME_OVER = 3
    FAIL_ALREADY_GUESSED = 4


class HangmanGame:
    def __init__(self, word, failedGuessesLimit):
        self.word = word

        self.state = GameState.IN_PROGRESS
        self.guesses = []
        self.failedGuessLimit = failedGuessesLimit
        self.numFailedGuessesRemaining = failedGuessesLimit
        self.revealedWord = ''.join(['_' for i in range(len(word))])
        self.numRevealedLetters = 0

    def guess(self, letter):
        # TODO uppercase/lowercase

        if not str.isalnum(letter) or len(letter) > 1:
            return GuessResult.FAIL_INVALID_INPUT

        if self.state != GameState.IN_PROGRESS:
            return GuessResult.FAIL_ALREADY_GAME_OVER

        if letter in self.guesses:
            return GuessResult.FAIL_ALREADY_GUESSED

        self.guesses.append(letter)

        letterInWord = False
        for i in range(len(self.word)):
            currLetter = self.word[i]

            if letter == currLetter:
                letterInWord = True
                self.numRevealedLetters += 1
                self.revealedWord = self.revealedWord[:i] + currLetter + self.revealedWord[i+1:]

        if letterInWord:
            if self.word == self.revealedWord:
                self.state = GameState.WON

            return GuessResult.CORRECT
        else:
            self.numFailedGuessesRemaining -= 1

            if self.numFailedGuessesRemaining <= 0:
                self.state = GameState.LOST

            return GuessResult.INCORRECT


class HangmanGameScorer:
    pointsPerLetter = 20
    bonusPointsPerRemainingGuess = 10

    @classmethod
    def score(self, game):
        points = game.numRevealedLetters * HangmanGameScorer.pointsPerLetter
        bonusPoints = game.numFailedGuessesRemaining * HangmanGameScorer.bonusPointsPerRemainingGuess
        return points + bonusPoints


def createHangmanGame():
    words = ["3dhubs", "marvin", "print", "filament", "order", "layer"]
    randWord = words[random.randint(0, len(words)-1)]
    return HangmanGame(randWord, 5)

