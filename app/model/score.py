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

    yw_stand = db.Column(db.Float())  # 语文标准分

    sx = db.Column(db.Float())  # 数学

    sx_stand = db.Column(db.Float())  # 数学标准分

    yy = db.Column(db.Float())  # 英语

    yy_stand = db.Column(db.Float())  # 英语标准分

    wl_hg = db.Column(db.Float())  # 物理合格

    wl_dj = db.Column(db.Float())  # 物理等级

    wl_stand = db.Column(db.Float())  # 物理标准分

    hx_hg = db.Column(db.Float())  # 化学合格

    hx_dj = db.Column(db.Float())  # 化学等级

    hx_stand = db.Column(db.Float())  #化学标准分

    sw = db.Column(db.Float())  # 生物

    sw_stand = db.Column(db.Float())  # 生物标准分

    dl = db.Column(db.Float())  # 地理

    dl_stand = db.Column(db.Float())  # 地理标准分

    ls = db.Column(db.Float())  # 历史

    ls_stand = db.Column(db.Float())  # 历史标准分

    zz = db.Column(db.Float())  # 政治

    zz_stand = db.Column(db.Float())  # 政治标准分

    sum_3 = db.Column(db.Float())  # 三门总分

    class_rank_3 = db.Column(db.Integer())  # 三门班级排名

    grade_rank_3 = db.Column(db.Integer())  # 三门年级排名

    student_id = db.Column(db.Integer(), db.ForeignKey("student.id"))

    exam_id = db.Column(db.Integer(), db.ForeignKey("exam.id"))

    # __mapper_args__ = {"order_by": exam.create_time}

    def __init__(self, yw="", yw_stand="", sx="", sx_stand="", yy="", yy_stand="",
                    wl_hg="", wl_dj="", wl_stand="",
                    hx_hg="", hx_dj="", hx_stand="",
                    sw="", sw_stand="", dl="", dl_stand="", ls="", ls_stand="", zz="", zz_stand="",
                    sum_3="", class_rank_3="", grade_rank_3="", exam_id="", student_id=""):

        self.yw = yw

        self.yw_stand = yw_stand

        self.sx = sx

        self.sx_stand = sx_stand

        self.yy = yy

        self.yy_stand = yy_stand

        self.wl_hg = wl_hg

        self.wl_dj = wl_dj

        self.wl_stand = wl_stand

        self.hx_hg = hx_hg

        self.hx_dj = hx_dj

        self.hx_stand = hx_stand

        self.sw = sw

        self.sw_stand = sw_stand

        self.dl = dl

        self.dl_stand = dl_stand

        self.ls = ls

        self.ls_stand = ls_stand

        self.zz = zz

        self.zz_stand = zz_stand

        self.sum_3 = sum_3

        self.class_rank_3 = class_rank_3

        self.grade_rank_3 = grade_rank_3

        self.student_id = student_id

        self.exam_id = exam_id

    # def __repr__(self):
    #
    #     return self.email

    def to_json(self):

        score = dict()

        score["id"] = self.id

        score["yw"] = self.yw

        score["yw_stand"] = self.yw_stand

        score["sx"] = self.sx

        score["sx_stand"] = self.sx_stand

        score["yy"] = self.yy

        score["yy_stand"] = self.yy_stand

        score["wl_hg"] = self.wl_hg

        score["wl_dj"] = self.wl_dj

        score["wl_stand"] = self.wl_stand

        score["hx_hg"] = self.hx_hg

        score["hx_dj"] = self.hx_dj

        score["hx_stand"] = self.hx_stand

        score["sw"] = self.sw

        score["sw_stand"] = self.sw_stand

        score["dl"] = self.dl

        score["dl_stand"] = self.dl_stand

        score["ls"] = self.ls

        score["ls_stand"] = self.ls_stand

        score["zz"] = self.zz

        score["zz_stand"] = self.zz_stand

        score["sum_3"] = self.sum_3

        score["class_rank_3"] = self.class_rank_3

        score["grade_rank_3"] = self.grade_rank_3

        score["student_id"] = self.student_id

        score["exam_id"] = self.exam_id

        return score
