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

	# def __init__(self, email="", password=""):

	#     self.email = email

	#     self.password = password

	# def __repr__(self):
	#
	#     return self.email

	# def to_json(self):
	#
	#     user = dict()
	#
	#     user["id"] = self.id
	#
	#     user["email"] = self.email
	#
	#     user["roles"] = self.roles
	#
	#     user["active"] = self.active
	#
	#     user["confirmed_at"] = self.confirmed_at
	#
	#     user["login_count"] = self.login_count
	#
	#     user["last_login_at"] = self.last_login_at
	#
	#     user["last_login_ip"] = self.last_login_ip
	#
	#     user["current_login_at"] = self.current_login_at
	#
	#     user["current_login_ip"] = self.current_login_ip
	#
	#     return user
