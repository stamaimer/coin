# -*- coding: utf-8 -*-

"""

    coin.app.model.cv
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from app.model import db


class Cv(db.Model):
    __tablename__ = "cv"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    #
    # photo = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    name = db.Column(db.Text())

    skills = db.Column(db.Text())

    experience = db.relationship('Cv_exp', backref='owner_cv', lazy='dynamic')

    education = db.relationship('Cv_edu', backref='owner_cv', lazy='dynamic')

    owner_user = db.relationship('Pip_user', backref='cv', lazy='dynamic')

    def __init__(self, name=None, skills=None):
        self.name = name

        self.skills = skills

    def __repr__(self):

        return self.name

    def to_json(self):
        cv = dict()

        cv['id'] = self.id

        cv['name'] = self.name

        cv['skills'] = self.skills

        cv['experience'] = list()

        for exp in self.experience:

            cv['experience'].append(exp.to_json())

        cv['education'] = list()

        for edu in self.experience:

            cv['education'].append(edu.to_json())

        return cv
