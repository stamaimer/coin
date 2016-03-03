from flask import flash, redirect, render_template, request, url_for

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