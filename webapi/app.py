from flask import Flask
import config

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>WEB API</p>"

if __name__ == '__main__':
    app.run(debug=True, host=config.HOST, port=config.PORT_API)