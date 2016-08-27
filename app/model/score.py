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

    yw = db.Column(db.Float()) #语文

    sx = db.Column(db.Float()) #数学

    yy = db.Column(db.Float()) #英语

    wl = db.Column(db.Float()) #物理

    hx = db.Column(db.Float()) #化学

    sw = db.Column(db.Float()) #生物

    ls = db.Column(db.Float()) #历史

    zz = db.Column(db.Float()) #政治

    dl = db.Column(db.Float()) #地理

    sum_3 = db.Column(db.Float()) #三门总分

    sum_5 = db.Column(db.Float()) #五门总分

    class_rank_3 = db.Column(db.Integer()) #三门班级排名

    class_rank_5 = db.Column(db.Integer()) #五门班级排名

    grade_rank_3 = db.Column(db.Integer()) #三门年级排名

    grade_rank_5 = db.Column(db.Integer()) #五门年级排名

    student_id = db.Column(db.Integer(), db.ForeignKey("student.id"))

    exam_id = db.Column(db.Integer(), db.ForeignKey("exam.id"))

    # __mapper_args__ = {"order_by": exam.create_time}

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
