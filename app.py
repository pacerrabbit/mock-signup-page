#!python2.7

# Standard libs
import hashlib

# Third party libs
from flask import Flask
from flask import abort
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

# Our libs
from models import User

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('signup'))

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/do-signup', methods=['POST'])
def do_signup():
    # Retrieve form parameters
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    password_confirm = request.form['password_confirm']

    if not username:
        abort(400, "Please enter a username")
    if not email:
        abort(400, "Please enter your email address")
    if not password:
        abort(400, "Please enter a password")
    if not password_confirm:
        abort(400, "Please confirm your password")

    # TODO: Finish validating the inputs

    # Hash password for storage
    # Note: SHA is not secure as a password hashing algorithm. Don't actually
    # use it for password hashing in real life.
    password_hash = hashlib.sha512(password).hexdigest()

    # Create user record
    user = User.create(username, email, password_hash)

    return redirect(url_for('users'))

@app.route('/users')
def users():
    # Retrieve all the users so we can display them in a table
    all_users = User.get_all()
    return render_template('users.html', all_users=all_users)

if __name__ == '__main__':
    app.run(debug=True)

