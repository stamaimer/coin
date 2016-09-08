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

    photo = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    content = db.Column(db.Text())

    def __init__(self, photo="", content=""):
        self.photo = photo

        self.content = content

    def to_json(self):
        news = dict()

        news['id'] = self.id

        news['content'] = self.content

        return news
