# Templates 

from flask import Flask, render_template

app6 = Flask(__name__, template_folder='templates')

@app6.route('/')
def index():
    return 'render_template("modelo.html")'


if __name__ == "__main__":
    app6.run(debug=True)
