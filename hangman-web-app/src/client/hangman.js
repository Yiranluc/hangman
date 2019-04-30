
async function createGame() {
	const url = "http://localhost:5000/api/hangman";
	const response = await fetch(url, {
		method: "POST",
		headers: { "Content-Type": "application/json" },
	});
	const json = await response.json();
	return json;
}

async function getGame(gameId) {
	const url = `http://localhost:5000/api/hangman/${gameId}`;
	const response = await fetch(url, {
		method: "GET",
		headers: { "Content-Type": "application/json" },
	});
	const json = await response.json();
	return json;
}

async function makeGuess(gameId, letter) {
	const url = `http://localhost:5000/api/hangman/${gameId}/guess`;
	const response = await fetch(url, {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify({ "letter": letter })
	});
	const json = await response.json();
	return json;
}

export default {
	createGame,
	getGame,
	makeGuess
}
