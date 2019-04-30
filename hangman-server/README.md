# hangman-server
Hangman REST API written in python using flask

## Getting started
Make sure you're using python 3

Install requirements
```
./venv/bin/activate
pip install -r requirements.txt
```

Start server
```
python server.py
```

Hit the API
```
POST http://localhost:5000/api/hangman
GET http://localhost:5000/api/hangman/{game_id}
POST http://localhost:5000/api/hangman/{game_id}/guess
```

## Missing features
- User session support
- Multiprocess support
- Server-side high score persistence

