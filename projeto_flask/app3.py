from flask import Flask, redirect, url_for

app3 = Flask(__name__)

app3.route('/admin')
def admin():
    return '<h1>Admin</h1>'

@app3.route('/guest/<name>')
def guest(name):
    return '<p>olá guest <b>%s</b></p>' % name

@app3.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', name = name))
    
@app3.route('/google')
def google():
    return redirect('http://google.com')

if __name__ == "__main__":
    app3.run(debug=True)

