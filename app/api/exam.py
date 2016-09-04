from flask import jsonify,request
from app.model.exam import Exam,db
from . import api

@api.route('/exam', methods=['GET'])
def get_exam():

	exams = Exam.query.all()

	response = dict()

	response['exams'] = list()

	for exam in exams:

		response['exams'].append(exam.to_json())

	# print response

	return jsonify(response)


@api.route('/exam', methods=['POST'])
def add_exam():
	name = request.form['name']

	exam = Exam(name=name)

	db.session.add(exam)

	db.session.commit()

	return jsonify(exam.to_json())


@api.route('/exam/<int:exam_id>', methods=['POST'])
def set_exam(exam_id):

	return exam_id


@api.route('/exam', methods=['DELETE'])
def delete_exam():

	id = request.form['id']

	exam = Exam.query.filter_by(id=id).first()

	db.session.delete(exam)

	db.session.commit()

	return "success"

