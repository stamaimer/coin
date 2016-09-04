from flask import jsonify, request
from app.model.student import Student, db
from . import api


@api.route('/student', methods=['GET'])
def get_student():
	students = Student.query.all()

	response = dict()

	response['students'] = list()

	for student in students:
		response['students'].append(student.to_json())

	# print response

	return jsonify(response)


@api.route('/student', methods=['POST'])
def add_student():
	name = request.form['name']

	student_id = request.form['student_id']

	student = Student(name=name, student_id=student_id)

	db.session.add(student)

	db.session.commit()

	return jsonify(student.to_json())


@api.route('/student', methods=['DELETE'])
def delete_student():
	id = request.form['id']

	try:

		student = Student.query.filter_by(id=int(id)).first();

		db.session.delete(student)

		db.session.commit()

		return '0'

	except:

		return '1'

