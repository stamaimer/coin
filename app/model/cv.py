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

    content = db.Column(db.Text())

    def __init__(self, name="", content=""):
        self.name = name

        self.content = content

    def __repr__(self):

        return self.name

    def to_json(self):
        cv = dict()

        cv['id'] = self.id

        cv['name'] = self.name

        cv['content'] = self.content

        return cv
