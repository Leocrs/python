from flask import Flask

app = Flask(__name__)

# Import routes
from app import routes

if __name__ == '__main__':
    app.run(debug=True)


    # http://localhost:5000/

    