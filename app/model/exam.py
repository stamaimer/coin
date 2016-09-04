# -*- coding: utf-8 -*-

"""

    coin.app.model.exam
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from app.model import db
import datetime
import time


class Exam(db.Model):
	__tablename__ = "exam"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

	scores = db.relation("Score", backref=db.backref("exam"))

	name = db.Column(db.String(255))

	create_time = db.Column(db.Date())

	def __init__(self, name="", create_time=datetime.date.today()):
		self.name = name

		self.create_time = create_time

	# def __repr__(self):
	#
	#     return self.email

	def to_json(self):
		exam = dict()

		exam["id"] = self.id

		exam["name"] = self.name

		exam["create_time"] = self.create_time

		return exam
