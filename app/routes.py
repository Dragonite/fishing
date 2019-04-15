from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

user = {'nickname': 'Haolin', 'admin': 'true', 'id': 1}

@app.route('/')
@app.route('/index')
def index():
      # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'Haolin'}, 
            'body': 'I caught a herring!' 
        },
        { 
            'author': {'nickname': 'Luna'}, 
            'body': 'I caught a snapper!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form, user=user)