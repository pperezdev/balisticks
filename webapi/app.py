from flask import Flask
from config import Config

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>WEB API</p>"

@app.route("/api/")
def api():
    return "api"

if __name__ == '__main__':
    app.run(debug=True, host=Config.HOST, port=Config.PORT_API)