# -*- coding: utf-8 -*-

"""

    coin.app.model.podcast
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from app.model import db


class Talks(db.Model):
    __tablename__ = "talks"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    topic = db.Column(db.String())

    location = db.Column(db.String())

    time = db.Column(db.DateTime())

    owner_user_id = db.Column(db.Integer(), db.ForeignKey("pip_user.id"))

    owner_user = db.relationship('Pip_user', foreign_keys=owner_user_id)

    def __init__(self, topic="", time=""):

        self.topic = topic

        self.time = time

    def __repr__(self):
        return self.topic

    def to_json(self):
        interview = dict()

        interview['id'] = self.id

        interview['media_pic_id'] = self.media_pic_id

        interview['topic'] = self.topic

        interview['time'] = self.time

        return interview
