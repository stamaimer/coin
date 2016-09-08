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

    audio = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    photo = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    content = db.Column(db.Text())

    def __init__(self, audio="", photo="", content=""):
        self.audio = audio

        self.photo = photo

        self.content = content

    def to_json(self):
        podcast = dict()

        podcast['id'] = self.id

        podcast['audio'] = self.audio

        podcast['photo'] = self.photo

        podcast['content'] = self.content

        return podcast
