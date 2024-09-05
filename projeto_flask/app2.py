from flask import Flask

app2 = Flask(__name__)

@app2.route("/")
def index():
    return "Hello, World!"

@app2.route("/favicon.ico")
def favicon():
    return "Favicon"

if __name__ == "__main__":
    app2.run()