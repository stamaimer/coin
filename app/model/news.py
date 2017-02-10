# -*- coding: utf-8 -*-

"""

    coin.app.model.news
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from app.model import db


class News(db.Model):
    __tablename__ = "news"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    # photo = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    name = db.Column(db.Text())

    news_piece = db.relationship('News_piece', backref='owner_news', lazy='dynamic')

    owner_user = db.relationship('Pip_user', backref='news', lazy='dynamic')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return self.name

    def to_json(self):
        news = dict()

        news['id'] = self.id

        news['name'] = self.name

        news['news_piece'] = list()

        for piece in self.news_piece:

            news['news_piece'].append(piece.to_json())

        return news
