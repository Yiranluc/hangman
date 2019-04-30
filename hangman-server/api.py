from flask import Blueprint, request, jsonify
import hangman
from gamemanager import GameManager

api = Blueprint('api', __name__)

game_manager = GameManager()


@api.route('/api/hangman', methods=['POST'])
def post_hangman():
    game_id, game = game_manager.create_game()
    data = {'gameId': game_id}
    return jsonify(data), 200


@api.route('/api/hangman/<int:game_id>', methods=['GET'])
def get_hangman(game_id):
    game = game_manager.get_game(game_id)

    if game is None:
        return jsonify({'error': 'Game not found'}), 404

    data = {
        'gameId': game_id,
        'revealedWord': game.revealed_word,
        'numFailedGuessesRemaining': game.num_failed_guesses_remaining,
        'score': hangman.HangmanGameScorer.score(game)
    }

    return jsonify(data), 200


@api.route('/api/hangman/<int:game_id>/guess', methods=['POST'])
def post_hangman_guess(game_id):
    game = game_manager.getGame(game_id)

    if game is None:
        return jsonify({'error': 'Game not found'}), 404

    if 'letter' not in request.json:
        return jsonify({'error': '\'letter\' is required input'}), 400

    letter = request.json['letter']

    result = game.guess(letter)

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
