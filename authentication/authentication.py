from flask import Flask, redirect, render_template, request, url_for, Blueprint, session
from werkzeug.security import generate_password_hash, check_password_hash

import pickle
import os

import re

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static', static_url_path='/authentication/static')

# Load users from pickle file
def load_users():
    if not os.path.exists('users.pkl'):
        with open('users.pkl', 'wb') as file:
            pickle.dump({}, file)
        return {}
    try:
        with open('users.pkl', 'rb') as file:
            users = pickle.load(file)
            if not users:
                return {}
            return users
    except EOFError:
        return {}

# Save users to pickle file
def save_users(users):
    with open('users.pkl', 'wb') as file:
        pickle.dump(users, file)

@auth.route('/signup', methods=['GET', 'POST'])
def signUpPage():
    message = ""
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        cnfrm_password = request.form.get('confirm_password')
        role = request.form.get('role')

        # Basic validation
        if not all([email, username, password, cnfrm_password, role]):
            message = 'All fields are required!'
            return render_template('signup.html', message=message)

        if password != cnfrm_password:
            message = 'Passwords do not match!'
            return render_template('signup.html', message=message)

        # Password validation
        if not validate_password(password):
            message = 'Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one number, and one special character.'
            return render_template('signup.html', message=message)

        # Load existing users
        users = load_users()

        if email in users:
            message = 'Email is already registered!'
            return render_template('signup.html', message=message)

        # Hash the password for security
        hashed_password = generate_password_hash(password)

        # Store user
        users[email] = {
            'username': username,
            'password': hashed_password,
            'role': role
        }
        print(users)
        # Save users
        save_users(users)

        message = 'Signup successful! Please log in.'
        return render_template('login.html', message=message)  # Redirect to login page or any other page

    return render_template('signup.html', message=message)

def validate_password(password):
    # Check password criteria
    if (len(password) < 8 or
        not re.search(r'[A-Z]', password) or  # At least one uppercase letter
        not re.search(r'[a-z]', password) or  # At least one lowercase letter
        not re.search(r'[0-9]', password) or  # At least one digit
        not re.search(r'[\W_]', password)):    # At least one special character
        return False
    return True

@auth.route('/login', methods=['GET', 'POST'])
def loginPage():
    message = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Load users
        users = load_users()

        # Check for user
        user = next((u for u in users.values() if u['username'] == username), None)
        if user and check_password_hash(user['password'], password):
            session['loggedin'] = True
            session['username'] = username
            message = 'Login successful!'
            return redirect(url_for('model_pred.predict'))  # Redirect to home or dashboard
        else:
            message = 'Invalid username or password.'

    return render_template('login.html', message=message)
