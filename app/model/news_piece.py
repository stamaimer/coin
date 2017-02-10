# -*- coding: utf-8 -*-

"""

    coin.app.model.cv
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from app.model import db


class News_piece(db.Model):
    __tablename__ = "news_piece"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    #
    # photo = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    topic = db.Column(db.String())

    time = db.Column(db.String())

    location = db.Column(db.String())

    owner_news_id = db.Column(db.Integer(), db.ForeignKey("news.id"))

    def __init__(self, topic=None, time=None, location=None):
        self.topic = topic

        self.time = time

        self.location = location

    def __repr__(self):

        return self.topic

    def to_json(self):
        piece = dict()

        piece['id'] = self.id

        piece['topic'] = self.topic

        piece['time'] = self.time

        piece['location'] = self.location

        return piece
