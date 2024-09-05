from flask import Flask

# Create a Flask web server from the current module
app = Flask(__name__)

@app.route('/')
def home():
    """Display a welcome message on the home page."""
    return 'Bem-vindo à página inicial!'

if __name__ == '__main__':
    # Run the Flask development server with debugging enabled
    app.run(debug=True)