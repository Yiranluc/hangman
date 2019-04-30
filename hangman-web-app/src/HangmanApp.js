import React, { useState, useEffect } from 'react';
import hangman from './client/hangman';
import GameView from './components/GameView';
import GameOverView from './components/GameOverView';
import './HangmanApp.css';

const HIGHSCORE_KEY = 'hangman_highscore';

function HangmanApp() {
    const [game, setGame] = useState({});
    const [highscore, setHighscore] = useState(0);

    async function startGame() {
        const savedHighscore = localStorage.getItem(HIGHSCORE_KEY);
        setHighscore(savedHighscore);

        const game = await hangman.createGame();
        setGame(game);
    }

    async function makeGuess(letter) {
        const result = await hangman.makeGuess(game.gameId, letter);
        const updatedGame = await hangman.getGame(game.gameId);

        // TODO display show the result of the guessse

        setGame(updatedGame);
    }

    useEffect(() => {
        startGame();
    }, []);

    useEffect(() => {
        if (game && game.score && game.state != 'IN_PROGESS') {
            // Just saving the high score on client side for now
            const savedHighscore = localStorage.getItem(HIGHSCORE_KEY);
            const currHighscore = parseInt(game.score);

            if (savedHighscore === null || currHighscore > savedHighscore) {
                localStorage.setItem(HIGHSCORE_KEY, currHighscore);
                setHighscore(currHighscore);
            }
        }
    }, [game]);

    let view;

    if (game.state == 'IN_PROGESS') {
        view =
            <GameView
                game={game}
                onGuess={(letter) => makeGuess(letter)}
            />;
    } else if (game.state) {
        view =
            <GameOverView
                game={game}
                highscore={highscore}
                onRestartGame={() => startGame()}
            />;
    }

    return (
        <div className="HangmanApp">
            <h1>Hangman</h1>
            {view}
        </div>
    );
}

export default HangmanApp;
