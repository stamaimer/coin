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

    wl_hg_av = db.Column(db.Float())

    hx_hg_av = db.Column(db.Float())

    wl_dj_av = db.Column(db.Float())

    hx_dj_av = db.Column(db.Float())

    sw_av = db.Column(db.Float())

    ls_av = db.Column(db.Float())

    zz_av = db.Column(db.Float())

    dl_av = db.Column(db.Float())

    yw_stand_av = db.Column(db.Float())

    sx_stand_av = db.Column(db.Float())

    yy_stand_av = db.Column(db.Float())

    wl_stand_av = db.Column(db.Float())

    hx_stand_av = db.Column(db.Float())

    sw_stand_av = db.Column(db.Float())

    ls_stand_av = db.Column(db.Float())

    zz_stand_av = db.Column(db.Float())

    dl_stand_av = db.Column(db.Float())

    def __init__(self, name="", create_time=datetime.date.today(), yw_av="0", sx_av="0", yy_av="0", wl_hg_av="0", hx_hg_av="0", wl_dj_av="0", hx_dj_av="0", sw_av="0", ls_av="0", zz_av="0", dl_av="0", yw_stand_av="0", sx_stand_av="0", yy_stand_av="0", wl_stand_av="0", hx_stand_av="0", sw_stand_av="0", ls_stand_av="0", zz_stand_av="0", dl_stand_av="0"):
        self.name = name

        self.create_time = create_time

        self.yw_av = yw_av

        self.sx_av = sx_av

        self.yy_av = yy_av

        self.wl_hg_av = wl_hg_av

        self.hx_hg_av = hx_hg_av

        self.wl_dj_av = wl_dj_av

        self.hx_dj_av = hx_dj_av

        self.sw_av = sw_av

        self.ls_av = ls_av

        self.zz_av = zz_av

        self.dl_av = dl_av

        self.yw_stand_av = yw_stand_av

        self.sx_stand_av = sx_stand_av

        self.yy_stand_av = yy_stand_av

        self.wl_stand_av = wl_stand_av

        self.hx_stand_av = hx_stand_av

        self.sw_stand_av = sw_stand_av

        self.ls_stand_av = ls_stand_av

        self.zz_stand_av = zz_stand_av

        self.dl_stand_av = dl_stand_av

    def to_json(self):
        exam = dict()
        
        exam["id"] = self.id
        
        exam["name"] = self.name
        
        exam["create_time"] = self.create_time

        exam["yw_av"] = self.yw_av

        exam["sx_av"] = self.sx_av

        exam["yy_av"] = self.yy_av

        exam["wl_hg_av"] = self.wl_hg_av

        exam["hx_hg_av"] = self.hx_hg_av

        exam["wl_dj_av"] = self.wl_dj_av

        exam["hx_dj_av"] = self.hx_dj_av

        exam["sw_av"] = self.sw_av

        exam["ls_av"] = self.ls_av

        exam["zz_av"] = self.zz_av

        exam["dl_av"] = self.dl_av

        exam["yw_stand_av"] = self.yw_stand_av

        exam["sx_stand_av"] = self.sx_stand_av

        exam["yy_stand_av"] = self.yy_stand_av

        exam["wl_stand_av"] = self.wl_stand_av

        exam["hx_stand_av"] = self.hx_stand_av

        exam["sw_stand_av"] = self.sw_stand_av

        exam["ls_stand_av"] = self.ls_stand_av

        exam["zz_stand_av"] = self.zz_stand_av

        exam["dl_stand_av"] = self.dl_stand_av

        return exam
