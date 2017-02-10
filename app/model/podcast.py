# -*- coding: utf-8 -*-

"""

    coin.app.model.podcast
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from app.model import db


class Podcast(db.Model):
    __tablename__ = "podcast"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    audio_id = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    audio = db.relationship('Resource', foreign_keys=audio_id)

    # photo = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    name = db.Column(db.String())

    content = db.Column(db.Text())

    owner_user = db.relationship('Pip_user', backref='podcast', lazy='dynamic')

    def __init__(self, name="", content=""):

        self.name = name

        self.content = content

    def __repr__(self):
        return self.name

    def to_json(self):
        podcast = dict()

        podcast['id'] = self.id

        podcast['audio_id'] = self.audio_id

        podcast['name'] = self.name

        podcast['content'] = self.content

        return podcast
