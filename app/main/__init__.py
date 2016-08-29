# -*- coding: utf-8 -*-

"""

    coin.app.main
    ~~~~~~~~~~~~~

    stamaimer 08/14/16

"""

import sys
from datetime import datetime
from flask import Blueprint, current_app
from flask import abort, make_response, redirect, render_template, request, url_for
from flask_security import login_required
from flask_sqlalchemy import get_debug_queries
from app.security import security
from app.form.registration_form import RegistrationForm
from app.model import db
from app.model.registration import Registration


main = Blueprint("main", __name__)


@main.before_app_first_request
def before_app_first_request():

    pass


@main.before_app_request
def before_app_request():

    pass


@main.after_app_request
def after_app_request(response):

    for query in get_debug_queries():

        current_app.logger.debug(query)

    return response


@main.teardown_app_request
def teardown_app_request(response):

    return response


@main.route('/')
def index():

    return render_template("index.html", current_time=datetime.utcnow())


# @main.app_errorhandler(404)
# def page_not_found():
#
#     pass


@main.route("/registration", methods=["GET"])
def show_registration():

    return render_template("registration.html", registration_form=RegistrationForm())


@main.route("/registration", methods=["POST"])
def post_registration():

    form = RegistrationForm()

    current_app.logger.debug(form)

    if form.validate_on_submit():

        registration = Registration(form.first_name.data,
                                    form.last_name.data,
                                    ','.join(form.degrees.data),
                                    form.other_degrees.data,
                                    form.position.data,
                                    form.mailing_address.data["organization"],
                                    form.mailing_address.data["address1"],
                                    form.mailing_address.data["address2"],
                                    form.mailing_address.data["city"],
                                    form.mailing_address.data["state"],
                                    form.mailing_address.data["zip_code"],
                                    form.mailing_address.data["country"],
                                    form.work_phone.data,
                                    form.fax.data,
                                    form.email.data,
                                    form.alternate_email.data,
                                    form.work_environment.data,
                                    ','.join(form.primary_interests.data["health_research_topic"]),
                                    ','.join(form.primary_interests.data["health_research_method"]))

        db.session.add(registration)

        db.session.commit()

        return redirect(url_for("main.show_registrations"))
    else:

        return redirect(url_for("main.show_registration"))


@main.route("/registrations", methods=["GET"])
def show_registrations():

    try:

        resgistations = Registration.query.all()

    except:

        current_app.logger.error(sys.exc_info())

    finally:

        return render_template("registrations.html", registrations=resgistations)


@main.route("/registrations/<id>", methods=["GET"])
def show_registration_detail(id):

    try:

        registration = Registration.query.filter(Registration.id == id).first()

    except:

        current_app.logger.error(sys.exc_info())

    finally:

        return render_template("registration_detail.html", registration=registration)


# @main.app_context_processor
# def app_context_processor():
#
#     pass