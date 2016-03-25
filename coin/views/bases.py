# -*- coding: utf-8 -*-
from . import *


@coin.route('/')
@coin.route("/index/")
@login_required
def index():

    return render_template("index.html")


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


@coin.route("/test", methods=["GET", "POST"])
@auth_token_required
def test():

    return "Test"


@coin.errorhandler(404)
def four04(error):

    return render_template("404.html"), 404


@coin.before_request
def before_request():

    pass


@coin.teardown_request
def teardown_request(exception):

    pass