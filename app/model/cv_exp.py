# -*- coding: utf-8 -*-

"""

    coin.app.model.cv
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from app.model import db


class Cv_exp(db.Model):
    __tablename__ = "cv_exp"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    #
    # photo = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    title = db.Column(db.String())

    org = db.Column(db.String())

    duration = db.Column(db.String())

    owner_cv_id = db.Column(db.Integer(), db.ForeignKey("cv.id"))

    def __init__(self, title=None, org=None, duration=None):
        self.title = title

        self.org = org

        self.duration = duration

    def __repr__(self):

        return self.title

    def to_json(self):
        experience = dict()

        experience['id'] = self.id

        experience['title'] = self.title

        experience['org'] = self.org

        experience['duration'] = self.duration

        return experience
