import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from logging import DEBUG
from flask_sqlalchemy import SQLAlchemy
from thermos.forms import BookMarkForm, LoginForm
from thermos.models import User, Bookmark

from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)
from flask_login import login_manager, login_required

bookmarks = []


def store_bookmark(url, description):
    bookmarks.append(dict(
        url=url,
        description=description,
        user="sudeep",
        date=datetime.utcnow
    ))


def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", new_bookmarks=models.Bookmark.newest(5))


@app.route('/addold', methods=["GET", "POST"])
def add1():
    if request.method == "POST":
        url = request.form['url']
        print(url)
        app.logger.debug('stored url: ' + url)
        flash("Stored url books is: {}".format(url))
        flash("Stored url books is: {}".format(url))

        return redirect(url_for('index'))
    return render_template("add.html")


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookMarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        # bm = Bookmark(url=url, description=description)
        bm = models.Bookmark(url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        print(url, description)
        flash("Stored url books is: {} ,{}".format(url, description))
        flash("Stored url books is: {} ,{}".format(url, description))

        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.errorhandler(404)
def server_error(e):
    return render_template('404.html'), 404


@app.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404
    return render_template('user.html', user=user)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            login_user(user, form.remember_me.data)
            flash("Logged in sucessfully as {}.".format(user.username))
            return redirect(request.args.get('next') or url_for('index'))
        flash("Incorrect usename or password")
    return render_template("login.html", form=form)
