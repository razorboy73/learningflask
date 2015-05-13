__author__ = 'workhorse'
from flask import render_template

from app import app


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