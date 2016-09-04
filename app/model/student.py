# -*- coding: utf-8 -*-

"""

    coin.app.model.student
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from werkzeug.security import check_password_hash, generate_password_hash
from flask_security import UserMixin
from app.model import db


class Student(db.Model):

	__tablename__ = "student"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

	scores = db.relation("Score", backref=db.backref("student"))

	name = db.Column(db.String(255))

	student_id = db.Column(db.Integer())

	open_id = db.Column(db.String(255))

	def __init__(self, name="", student_id=""):

		self.name = name

		self.student_id = student_id


	# def __repr__(self):
	#
	#     return self.email

	def to_json(self):

		student = dict()

		student["id"] = self.id

		student["name"] = self.name

		student["student_id"] = self.student_id

		return student
