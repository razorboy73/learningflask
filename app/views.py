__author__ = 'workhorse'


from flask import render_template, flash, redirect
from app import app

from .forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    user = {"nickname": "Josh"}

    posts = [#array of posts
        {
            "author":{"nickname":"john"},
            "body":"Beautiful day in Portland"
        },
        {
            "author":{"nickname":"josh"},
            "body":"Hello from NYC"
        },
        {
            "author":{"nickname":"Leah"},
            "body":"I like shoes"
        }



     ]
    return render_template("index.html",
                           title = "Home",
                           user = user,
                            posts = posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for OpenID={}, remember_me {}".format(form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template("login.html",
                           title="Sign In",
                           form=form,
                           providers = app.config['OPENID_PROVIDERS'])