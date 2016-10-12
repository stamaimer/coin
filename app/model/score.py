# -*- coding: utf-8 -*-

"""

    coin.app.model.score
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from werkzeug.security import check_password_hash, generate_password_hash
from flask_security import UserMixin
from app.model import db


class Score(db.Model):
	__tablename__ = "score"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

	yw = db.Column(db.Float())  # 语文

	sx = db.Column(db.Float())  # 数学

	yy = db.Column(db.Float())  # 英语

	wl = db.Column(db.Float())  # 物理

	hx = db.Column(db.Float())  # 化学

	sw = db.Column(db.Float())  # 生物

	ls = db.Column(db.Float())  # 历史

	zz = db.Column(db.Float())  # 政治

	dl = db.Column(db.Float())  # 地理

	sum_3 = db.Column(db.Float())  # 三门总分

	sum_5 = db.Column(db.Float())  # 五门总分

	yw_stand = db.Column(db.Float())  # 语文标准分

	sx_stand = db.Column(db.Float())  # 数学标准分

	yy_stand = db.Column(db.Float())  # 英语标准分

	class_rank_3 = db.Column(db.Integer())  # 三门班级排名

	class_rank_5 = db.Column(db.Integer())  # 五门班级排名

	grade_rank_3 = db.Column(db.Integer())  # 三门年级排名

	grade_rank_5 = db.Column(db.Integer())  # 五门年级排名

	student_id = db.Column(db.Integer(), db.ForeignKey("student.id"))

	exam_id = db.Column(db.Integer(), db.ForeignKey("exam.id"))

	# __mapper_args__ = {"order_by": exam.create_time}

	def __init__(self, yw="", sx="", yy="", wl="", hx="", sw="", ls="", zz="", dl="", sum_3="", sum_5="", yw_stand="", sx_stand="", yy_stand="", class_rank_3="", class_rank_5="", grade_rank_3="", grade_rank_5="", exam_id="", student_id=""):

		self.yw = yw

		self.sx = sx

		self.yy = yy

		self.wl = wl

		self.hx = hx

		self.sw = sw

		self.ls = ls

		self.zz = zz

		self.dl = dl

		self.sum_3 = sum_3

		self.sum_5 = sum_5

		self.yw_stand = yw_stand

		self.sx_stand = sx_stand

		self.yy_stand = yy_stand

		self.class_rank_3 = class_rank_3

		self.class_rank_5 = class_rank_5

		self.grade_rank_3 = grade_rank_3

		self.grade_rank_5 = grade_rank_5

		self.student_id = student_id

		self.exam_id = exam_id

	# def __repr__(self):
	#
	#     return self.email

	def to_json(self):
		score = dict()

		score["id"] = self.id

		score["yw"] = self.yw

		score["sx"] = self.sx

		score["yy"] = self.yy

		score["wl"] = self.wl

		score["hx"] = self.hx

		score["sw"] = self.sw

		score["ls"] = self.ls

		score["zz"] = self.zz

		score["dl"] = self.dl

		score["sum_3"] = self.sum_3

		score["sum_5"] = self.sum_5

		score["yw_stand"] = self.yw_stand

		score["sx_stand"] = self.sx_stand

		score["yy_stand"] = self.yy_stand

		score["class_rank_3"] = self.class_rank_3

		score["class_rank_5"] = self.class_rank_5

		score["grade_rank_3"] = self.grade_rank_3

		score["grade_rank_5"] = self.grade_rank_5

		score["student_id"] = self.student_id

		score["exam_id"] = self.exam_id

		return score
