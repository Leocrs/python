from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/favicon.ico")
def favicon():
    return "Favicon"

if __name__ == "__main__":
    app.run()