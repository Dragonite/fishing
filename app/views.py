from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Haolin'}  # fake user
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