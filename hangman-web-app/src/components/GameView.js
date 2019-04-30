import React, { useState, useEffect } from 'react';

function Word({revealedWord}) {
    const wordWithSpaces = revealedWord.split('').join(' ');
    return <p>{wordWithSpaces}</p>;
}

function GuessInput({onLetterUpdated, onGuess}) {
    const [letter, setLetter] = useState('');

    useEffect(() => {
     if(typeof onLetterUpdated === 'function') {
         onLetterUpdated();
     }
    }, [letter]);

    function submitGuess() {
        setLetter('');
        if(typeof onGuess === 'function') {
            onGuess(letter)
        }
    }

    function onKeyPress(ev) {
        if(ev.key === 'Enter') {
            submitGuess();
        }
    }

    return (
        <div>
            <input
                type="text"
                value={letter}
                autofocus
                onChange={e => setLetter(e.target.value)}
                onKeyPress={e => onKeyPress(e)}
            />
            <button
                type="button"
                onClick={() => submitGuess()}
            >
                Guess
            </button>
        </div>
    )

}

export default function GameView({game, onLetterUpdated, onGuess}) {
    return (
        <div>
            <Word revealedWord={game.revealedWord} />
            <p>Guesses Remaining: {game.numFailedGuessesRemaining}</p>
            <GuessInput onLetterUpdated={onLetterUpdated} onGuess={onGuess} />
        </div>
    );
}
