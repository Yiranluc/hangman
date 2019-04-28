from flask import Blueprint, request, jsonify
import hangman

api = Blueprint('api', __name__)
games = {}
lastGameId = 0


@api.route('/api/hangman', methods=['POST'])
def postHangman():
    global lastGameId
    global games

    # TODO Do I need a lock for this?
    lastGameId += 1
    game = hangman.createHangmanGame()
    games[lastGameId] = game

    data = {'gameId': lastGameId}

    return jsonify(data), 200


@api.route('/api/hangman/<int:gameId>', methods=['GET'])
def getHangman(gameId):
    global games

    if gameId not in games:
        return jsonify({'error': 'Game not found'}), 404

    game = games[gameId]

    data = {
        'gameId': gameId,
        'revealedWord': game.revealedWord,
        'numFailedGuessesRemaining': game.numFailedGuessesRemaining,
        'score': hangman.HangmanGameScorer.score(game)
    }

    return jsonify(data), 200


@api.route('/api/hangman/<int:gameId>/guess', methods=['POST'])
def postHangmanGuess(gameId):
    global games

    if gameId not in games:
        return jsonify({'error': 'Game not found'}), 404

    if 'letter' not in request.json:
        return jsonify({'error': '\'letter\' is required input'}), 400

    letter = request.json['letter']

    result = games[gameId].guess(letter)

    if result == hangman.GuessResult.FAIL_INVALID_INPUT:
        return jsonify({'error': 'Invalid input'}), 400
    elif result == hangman.GuessResult.FAIL_ALREADY_GAME_OVER:
        return jsonify({'error': 'Game already over'}), 500
    elif result == hangman.GuessResult.FAIL_ALREADY_GUESSED:
        return jsonify({'error': 'Letter already guessed'}), 500

    if result == hangman.GuessResult.INCORRECT:
        return jsonify({'result': 'Incorrect'}), 200
    else:
        return jsonify({'result': 'Success'}), 200

if __name__ == '__main__':
    api.run()
