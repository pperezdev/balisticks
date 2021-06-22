from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>WEB API</p>"

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5001)