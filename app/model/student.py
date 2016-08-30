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

    # @staticmethod
    # def generate_fake(count=47):
    #
    #     from random import seed
    #     import forgery_py
    #
    #     for i in xrange(count):
    #
    #         s = Student(name=)
