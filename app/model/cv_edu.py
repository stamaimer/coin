# -*- coding: utf-8 -*-

"""

    coin.app.model.cv
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from app.model import db


class Cv_edu(db.Model):
    __tablename__ = "cv_edu"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    #
    # photo = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    school = db.Column(db.String())

    major = db.Column(db.String())

    duration = db.Column(db.String())

    owner_cv_id = db.Column(db.Integer(), db.ForeignKey("cv.id"))

    def __init__(self, school=None, major=None, duration=None):
        self.school = school

        self.major = major

        self.duration = duration

    def __repr__(self):

        return self.school

    def to_json(self):
        education = dict()

        education['id'] = self.id

        education['school'] = self.school

        education['major'] = self.major

        education['duration'] = self.duration

        return education
