# -*- coding: utf-8 -*-

"""

    coin.app.model.podcast
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from app.model import db


class Interview(db.Model):
    __tablename__ = "interview"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    media_pic_id = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    media_pic = db.relationship('Resource', foreign_keys=media_pic_id)

    # photo = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    topic = db.Column(db.String())

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
