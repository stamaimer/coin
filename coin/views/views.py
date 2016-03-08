# -*- coding: utf-8 -*-

from flask import abort, escape, flash, g, redirect, render_template, request, send_from_directory, session, url_for
from werkzeug import secure_filename
import os
from coin import coin

@coin.route('/')
@coin.route("/index/")
def index():

    return render_template("index.html")

@coin.route("/signup/", methods=["POST"])
def signup():

    pass


@coin.route("/signin/", methods=["GET", "POST"])
def signin():

    error = None

    if request.method == "POST":

        if request.form["username"] != "admin" or \
           request.form["password"] != "secret":

            error = "Invalid credentials"

        else:

            flash("You were successfully signin.")

            return redirect(url_for("index"))

    return render_template("signin.html", error=error)


@coin.route("/upload/", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        file = request.files["file"]

        if file:

            filename = secure_filename(file.filename)

            file.save(os.path.join(coin.config["UPLOAD_DIR"], filename))

            return redirect(url_for("show", filename=filename))

    return render_template("upload.html")


@coin.route("/upload/<filename>")
def show(filename):

    return send_from_directory(coin.config["UPLOAD_DIR"], filename)


@coin.errorhandler(404)
def four04(error):

    return render_template("404.html"), 404


@coin.before_request
def before_request():

    pass


@coin.teardown_request
def teardown_request(exception):

    pass