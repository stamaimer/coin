# -*- coding: utf-8 -*-

"""

    coin.app.main
    ~~~~~~~~~~~~~

    stamaimer 08/14/16

"""

import sys
from datetime import datetime
from flask import Blueprint, abort, current_app, jsonify, make_response, redirect, render_template, request, url_for
from flask_security import login_required
from flask_sqlalchemy import get_debug_queries
from app.model import db
from app.model.student import Student


main = Blueprint("main", __name__)


@main.before_app_first_request
def before_app_first_request():

    pass


@main.before_app_request
def before_app_request():

    pass


@main.after_app_request
def after_app_request(response):

    # for query in get_debug_queries():
    #
    #     current_app.logger.debug(query)

    return response


@main.teardown_app_request
def teardown_app_request(response):

    return response


@main.route('/')
def index():

    return 'test'

    return render_template("index.html", current_time=datetime.utcnow())


# @main.app_errorhandler(404)
# def page_not_found(response):
#
#     pass


@main.route("/bind", methods=["PATCH"])
def bind():

    response = dict()

    try:

        request_body = request.get_json(force=True)

        student_id = request_body["student_id"]

        open_id = request_body["open_id"]

        name = request_body["name"]

        student = Student.query.filter(Student.student_id == student_id).first()

        if student:

            if student.name == name:

                if not student.open_id:

                    student.open_id = open_id

                    db.session.commit()

                    response["status"] = 1

                    response["description"] = u"绑定成功"

                else:

                    response["status"] = 0

                    response["description"] = u"该学生已绑定"

            else:

                response["status"] = 0

                response["description"] = u"学号和姓名不匹配"

        else:

            response["status"] = 0

            response["description"] = u"该学生不存在"

    except:

        current_app.logger.error(sys.exc_info())

    finally:

        return jsonify(response)


@main.route("/grade/<open_id>/<flag>", methods=["GET"])
def get_grade(open_id, flag):

    try:

        student = Student.query.filter(Student.open_id == open_id).first()

        if student:

            if flag == "current":

                score = student.scores[-1]

                return render_template("current_grade.html", score=score)

            elif flag == "history":

                scores = student.scores

                return render_template("history_grade.html", scores=scores)

            else:

                return "Flag Error"
        else:

            return "Student Not Exist"

    except:

        current_app.logger.error(sys.exc_info())

        return "Exception Occur"


@main.route("/input", methods=["GET"])
def _input():

    return render_template('input.html')


@main.route("/list", methods=["GET"])
def _list():

    exams = current_app.test_client().get(url_for('api.get_exam', _external=True))

    return render_template('list.html', exams=exams.data)


@main.route("/students", methods=["GET"])
def students():

    return render_template('students.html')

