from flask import Flask
from api.api import api

app = Flask(__name__)
app.register_blueprint(api)

@app.route('/')
def hello():
    return "Hello world!"

if __name__ == '__main__':
    app.run()
