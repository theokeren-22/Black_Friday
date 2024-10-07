from flask import Flask, redirect, render_template, request, url_for, Blueprint, session

graphs_display = Blueprint('graphs_display', __name__, template_folder='templates', static_folder='static', static_url_path='/graphs/static')

@graphs_display.route('/graphs', methods = ['GET', 'POST'])
def display_graphs():
    if 'username' not in session:
        return redirect(url_for('logout'))

    username = session.get('username')
    return render_template('graphs.html',
                            username = username)

@graphs_display.route('/about', methods = ['GET','POST'])
def about_page():
    if 'username' not in session:
        return redirect(url_for('logout'))

    username = session.get('username')
    return render_template('about.html',
                            username = username)