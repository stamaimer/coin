from flask import jsonify
from app.model.exam import Exam
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

	return ''


@api.route('/exam/<int:exam_id>', methods=['POST'])
def set_exam(exam_id):

	return exam_id

