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

    yw_av = db.Column(db.Float())

    sx_av = db.Column(db.Float())

    yy_av = db.Column(db.Float())

    wl_av = db.Column(db.Float())

    hx_av = db.Column(db.Float())

    sw_av = db.Column(db.Float())

    ls_av = db.Column(db.Float())

    zz_av = db.Column(db.Float())

    dl_av = db.Column(db.Float())

    def __init__(self, name="", create_time=datetime.date.today(), yw_av="0", sx_av="0", yy_av="0", wl_av="0", hx_av="0", sw_av="0", ls_av="0", zz_av="0", dl_av="0"):
        self.name = name

        self.create_time = create_time

        self.yw_av = yw_av

        self.sx_av = sx_av

        self.yy_av = yy_av

        self.wl_av = wl_av

        self.hx_av = hx_av

        self.sw_av = sw_av

        self.ls_av = ls_av

        self.zz_av = zz_av

        self.dl_av = dl_av

    def to_json(self):
        exam = dict()
        
        exam["id"] = self.id
        
        exam["name"] = self.name
        
        exam["create_time"] = self.create_time

        exam["yw_av"] = self.yw_av

        exam["sx_av"] = self.sx_av

        exam["yy_av"] = self.yy_av

        exam["wl_av"] = self.wl_av

        exam["hx_av"] = self.hx_av

        exam["sw_av"] = self.sw_av

        exam["ls_av"] = self.ls_av

        exam["zz_av"] = self.zz_av

        exam["dl_av"] = self.dl_av

        return exam
