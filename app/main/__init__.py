# -*- coding: utf-8 -*-

"""

    coin.app.main
    ~~~~~~~~~~~~~

    stamaimer 08/14/16

"""

import sys, json
from datetime import datetime
from flask import Blueprint, abort, current_app, jsonify, make_response, redirect, render_template, request, url_for
from flask_security import login_required
from flask_sqlalchemy import get_debug_queries
from app.model import db
from app.model.student import Student
from app.model.score import Score

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


@main.route("/unbind", methods=["PATCH"])
def unbind():
	response = dict()

	try:

		open_id = request.get_json(force=True)["open_id"]

		student = Student.query.filter(Student.open_id == open_id).first()

		if student:

			if student.open_id == open_id:

				student.open_id = None

				db.session.commit()

				response["status"] = 1

				response["description"] = u"解绑成功"

			else:

				response["status"] = 0

				response["description"] = u"解绑失败"

		else:

			response["status"] = 0

			response["description"] = u"还未绑定"

	except:

		current_app.logger.error(sys.exc_info())

	finally:

		return jsonify(response)


@main.route("/grade/<open_id>/<flag>", methods=["GET"])
def get_grade(open_id, flag):
	try:

		student = Student.query.filter(Student.open_id == open_id).first()

		if student:

			scores = student.scores

			score = scores[-1] if scores else None

			if flag == "current":

				return render_template("current_grade.html", score=score)

			elif flag == "history":

				return render_template("history_grade.html", scores=scores)

			else:

				return "Flag Error"
		else:

			return "请先绑定"

	except:

		current_app.logger.error(sys.exc_info())

		return "Exception Occur"


@main.route("/input", methods=["GET"])
@login_required
def _input():
	student = current_app.test_client().get(url_for('api.get_student', _external=True))

	if request.args.get('id'):

		results = Score.query.filter_by(exam_id=request.args['id']).order_by(Score.student_id).all()

		scores = []

		for result in results:

			scores.append(result.to_json())

		return render_template('input.html', students=json.loads(student.data), scores=scores, exam=results[0].exam)

	return render_template('input.html', students=json.loads(student.data), scores=None, exam=None)


@main.route("/list", methods=["GET"])
@login_required
def _list():
	exams = current_app.test_client().get(url_for('api.get_exam', _external=True))

	return render_template('list.html', exams=json.loads(exams.data))


@main.app_context_processor
def app_contect_processor():
	def strptime(str):
		return datetime.strptime(str, "%a, %d %b %Y %H:%M:%S GMT")

	return dict(strptime=strptime)


@main.route("/students", methods=["GET"])
@login_required
def students():
	student = current_app.test_client().get(url_for('api.get_student', _external=True))

	return render_template('students.html', students=json.loads(student.data))
